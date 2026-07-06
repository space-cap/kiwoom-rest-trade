import time
from datetime import datetime
from unittest.mock import AsyncMock, patch
import pytest
import httpx
from kiwoom import AsyncKiwoomClient, KiwoomClient
from kiwoom.models.domestic import Ka10001Request, Ka10001Response

def get_mock_expires_dt(offset_seconds: int = 3600) -> str:
    """현재 시각 기준 offset_seconds만큼의 미래 만료 일시를 YYYYMMDDHHMMSS 포맷으로 반환합니다."""
    dt = datetime.fromtimestamp(time.time() + offset_seconds)
    return dt.strftime("%Y%m%d%H%M%S")

# 모의 갱신 토큰 정보 (token, expires_dt 키 구성)
MOCK_TOKEN_RESPONSE = httpx.Response(
    status_code=200,
    json={"token": "client_mock_token_abc", "expires_dt": get_mock_expires_dt(3600)},
    request=httpx.Request("POST", "https://api.kiwoom.com/oauth2/token")
)

# 모의 ka10001 응답 정보 (실제 필드명 cur_prc 및 stk_nm 적용)
MOCK_API_RESPONSE = httpx.Response(
    status_code=200,
    json={
        "cur_prc": "84500",
        "stk_nm": "삼성전자"
    },
    request=httpx.Request("POST", "https://api.kiwoom.com/api/dostk/stkinfo")
)

@pytest.mark.asyncio
async def test_async_client_flow() -> None:
    """AsyncKiwoomClient를 이용한 비동기 API 호출 전체 연동 흐름을 테스트합니다."""
    client = AsyncKiwoomClient(appkey="test_app", secretkey="test_secret")
    
    # httpx.AsyncClient.post (토큰 획득용) 및 request (API 호출용) 모킹
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_request:
            mock_post.return_value = MOCK_TOKEN_RESPONSE
            mock_request.return_value = MOCK_API_RESPONSE
            
            # API 요청 객체 생성 (실제 필수 필드 stk_cd)
            req = Ka10001Request(
                stk_cd="005930"
            )
            
            # API 호출
            resp = await client.domestic.ka10001(req)
            
            # 검증
            assert isinstance(resp, Ka10001Response)
            assert resp.cur_prc == "84500"
            assert resp.stk_nm == "삼성전자"
            
            # 토큰 발급 1회, API 요청 1회 호출되었는지 확인
            assert mock_post.call_count == 1
            assert mock_request.call_count == 1


def test_sync_client_flow() -> None:
    """KiwoomClient를 이용한 동기식 API 호출 프록시 연동 흐름을 테스트합니다."""
    client = KiwoomClient(appkey="test_app", secretkey="test_secret")
    
    # 동기 클라이언트 내부의 _async_client 통신 모킹
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_request:
            mock_post.return_value = MOCK_TOKEN_RESPONSE
            mock_request.return_value = MOCK_API_RESPONSE
            
            req = Ka10001Request(
                stk_cd="005930"
            )
            
            # 동기식 API 호출 (await 없이 직접 호출)
            resp = client.domestic.ka10001(req)
            
            # 검증
            assert isinstance(resp, Ka10001Response)
            assert resp.cur_prc == "84500"
            assert resp.stk_nm == "삼성전자"
            
            assert mock_post.call_count == 1
            assert mock_request.call_count == 1
