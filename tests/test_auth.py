import asyncio
import time
from datetime import datetime
from typing import Any
from unittest.mock import AsyncMock, patch
import pytest
import httpx
from kiwoom.auth import TokenManager
from kiwoom.exceptions import KiwoomAuthError

# 공통 모의 Request 객체
MOCK_REQUEST = httpx.Request("POST", "https://api.kiwoom.com/oauth2/token")

def get_mock_expires_dt(offset_seconds: int = 3600) -> str:
    """현재 시각 기준 offset_seconds만큼의 미래 만료 일시를 YYYYMMDDHHMMSS 포맷으로 반환합니다."""
    dt = datetime.fromtimestamp(time.time() + offset_seconds)
    return dt.strftime("%Y%m%d%H%M%S")

@pytest.mark.asyncio
async def test_token_caching_and_expiry() -> None:
    """최초 토큰 발급 후 캐싱 및 유효 기간 내 동일 토큰 반환을 검증합니다."""
    manager = TokenManager(appkey="test_app", secretkey="test_secret")
    
    mock_response = httpx.Response(
        status_code=200,
        json={"token": "cached_token_123", "expires_dt": get_mock_expires_dt(3600)},
        request=MOCK_REQUEST
    )
    
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        
        # 1. 최초 토큰 획득
        token1 = await manager.get_valid_token()
        assert token1 == "cached_token_123"
        assert mock_post.call_count == 1
        
        # 2. 유효 기간 내 재호출 (캐시에서 즉시 반환되므로 API 호출이 발생하지 않아야 함)
        token2 = await manager.get_valid_token()
        assert token2 == "cached_token_123"
        assert mock_post.call_count == 1  # 여전히 1회

@pytest.mark.asyncio
async def test_token_auto_refresh_on_expiry() -> None:
    """토큰 만료 임박 시 자동으로 갱신 API를 호출하는지 검증합니다."""
    manager = TokenManager(appkey="test_app", secretkey="test_secret")
    
    # 임의로 만료된 토큰 상태 설정 (만료 타임스탬프를 5분 전으로 수동 조정)
    manager._access_token = "expired_token"
    manager._expires_at = time.time() - 300  # 이미 5분 전 만료됨

    mock_response = httpx.Response(
        status_code=200,
        json={"token": "new_refreshed_token", "expires_dt": get_mock_expires_dt(3600)},
        request=MOCK_REQUEST
    )

    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        
        # 호출 시 만료를 감지하고 새로 갱신해와야 함
        token = await manager.get_valid_token()
        assert token == "new_refreshed_token"
        assert mock_post.call_count == 1

@pytest.mark.asyncio
async def test_token_lock_prevents_duplicate_calls() -> None:
    """다중 코루틴 동시 호출 시 락에 의해 토큰 발급 API가 단 1회만 호출되는지 검증합니다."""
    manager = TokenManager(appkey="test_app", secretkey="test_secret")
    
    # 딜레이를 주어 응답하는 Mock Response
    async def slow_post(*args: Any, **kwargs: Any) -> httpx.Response:
        await asyncio.sleep(0.1)  # 0.1초 딜레이
        return httpx.Response(
            status_code=200,
            json={"token": "single_refreshed_token", "expires_dt": get_mock_expires_dt(3600)},
            request=MOCK_REQUEST
        )

    with patch("httpx.AsyncClient.post", new=slow_post):
        with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_count_post:
            # 실 주입
            mock_count_post.side_effect = slow_post
            
            # 5개의 코루틴이 동시에 토큰을 요청
            tokens = await asyncio.gather(
                manager.get_valid_token(),
                manager.get_valid_token(),
                manager.get_valid_token(),
                manager.get_valid_token(),
                manager.get_valid_token()
            )
            
            # 모든 코루틴이 동일한 새로운 토큰을 얻었는지 검증
            for token in tokens:
                assert token == "single_refreshed_token"
                
            # 동시 호출임에도 불구하고 API 호출 횟수는 단 1회여야 함
            assert mock_count_post.call_count == 1

@pytest.mark.asyncio
async def test_token_failure_exception() -> None:
    """토큰 발급 실패 시 적절한 KiwoomAuthError를 발생시키는지 테스트합니다."""
    manager = TokenManager(appkey="invalid_app", secretkey="invalid_secret")
    
    # 에러 바디 모의 응답
    mock_response = httpx.Response(
        status_code=200,
        json={"err_code": "8001", "err_msg": "App Key 인증 실패"},
        request=MOCK_REQUEST
    )
    
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        
        with pytest.raises(KiwoomAuthError) as exc_info:
            await manager.get_valid_token()
            
        assert "[8001]" in str(exc_info.value)
