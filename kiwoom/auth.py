import asyncio
import time
from typing import Optional

import httpx

from kiwoom.exceptions import KiwoomAuthError


class TokenManager:
    """
    키움증권 API 토큰의 수명(Expires)을 관리하고, 만료 임박 시 비동기 락을 이용하여
    안전하게 백그라운드 갱신을 담당하는 토큰 매니저 클래스입니다.
    """

    def __init__(self, appkey: str, secretkey: str, is_mock: bool = False) -> None:
        self.appkey = appkey
        self.secretkey = secretkey
        self.is_mock = is_mock

        # 내부 토큰 정보 상태 캐시
        self._access_token: Optional[str] = None
        self._expires_at: float = 0.0

        # 동시성 방지를 위한 비동기 락
        self._lock = asyncio.Lock()

    @property
    def base_url(self) -> str:
        """실전/모의투자에 따른 토큰 발급 기본 도메인 반환"""
        if self.is_mock:
            return "https://mockapi.kiwoom.com"
        return "https://api.kiwoom.com"

    async def get_valid_token(self) -> str:
        """
        현재 캐싱된 토큰이 유효한지 검사한 뒤 유효한 토큰 문자열을 반환합니다.
        토큰이 없거나 만료 임박 시 자동으로 갱신 프로세스(비동기 락 제어)를 수행합니다.
        """
        now = time.time()
        # 토큰 유효 시간 체크 (만료 10분 전부터 갱신 대상으로 판단)
        if self._access_token and (self._expires_at - now > 600):
            return self._access_token

        # 비동기 락을 통한 중복 토큰 갱신 요청 제어 (Double-Checked Locking)
        async with self._lock:
            # 락을 획득한 후 다시 한 번 체크 (대기하던 중 다른 코루틴이 먼저 갱신을 마쳤을 수 있으므로)
            now = time.time()
            if self._access_token and (self._expires_at - now > 600):
                return self._access_token

            # 실제 갱신 프로세스 진행
            await self._refresh_token()

            if not self._access_token:
                raise KiwoomAuthError("접근 토큰 갱신에 실패하여 유효한 토큰을 획득할 수 없습니다.")

            return self._access_token

    async def _refresh_token(self) -> None:
        """키움 OAuth 인증 서버에 토큰 발급을 비동기 요청합니다."""
        url = f"{self.base_url}/oauth2/token"
        headers = {"content-type": "application/json;charset=UTF-8", "api-id": "au10001"}
        data = {
            "grant_type": "client_credentials",
            "appkey": self.appkey,
            "secretkey": self.secretkey,
        }

        async with httpx.AsyncClient(http2=True) as http_client:
            try:
                response = await http_client.post(url, headers=headers, json=data, timeout=10.0)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                status_code = e.response.status_code
                raise KiwoomAuthError(
                    f"OAuth 서버가 HTTP 에러 코드를 반환했습니다. (상태 코드: {status_code})"
                ) from e
            except httpx.RequestError as e:
                raise KiwoomAuthError(f"OAuth 서버에 연결하지 못했습니다: {e}") from e

            try:
                resp_json = response.json()
            except ValueError as e:
                raise KiwoomAuthError("OAuth 응답 본문이 올바른 JSON 형식이 아닙니다.") from e

            # 키움 에러 코드 검사
            err_code = resp_json.get("err_code")
            if err_code:
                err_msg = resp_json.get("err_msg", "알 수 없는 토큰 발급 오류")
                raise KiwoomAuthError(f"[{err_code}] {err_msg}")

            access_token = resp_json.get("access_token")
            expires_in = resp_json.get("expires_in")  # 보통 86400초 (24시간)

            if not access_token or not expires_in:
                raise KiwoomAuthError("토큰 응답에 access_token 또는 expires_in 필드가 없습니다.")

            # 상태 업데이트
            self._access_token = str(access_token)
            self._expires_at = time.time() + float(expires_in)
