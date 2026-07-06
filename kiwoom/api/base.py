from typing import Any, Dict, Optional, cast

import httpx

from kiwoom.exceptions import (
    KiwoomAPIError,
    KiwoomAuthError,
    KiwoomError,
    KiwoomRateLimitError,
    KiwoomValidationError,
)


class BaseAPI:
    """
    모든 키움 REST API 래퍼 클래스의 기반이 되는 클래스입니다.
    HTTPX AsyncClient를 활용하여 실제 통신 및 공통 에러 핸들링을 수행합니다.
    """

    def __init__(self, client: Any) -> None:
        # 통합 클라이언트(AsyncKiwoomClient) 인스턴스 참조 저장
        self.client = client

    @property
    def base_url(self) -> str:
        """클라이언트 설정(실전/모의)에 따른 기본 도메인 URL을 반환합니다."""
        if getattr(self.client, "is_mock", False):
            return "https://mockapi.kiwoom.com"
        return "https://api.kiwoom.com"

    async def _request(
        self,
        method: str,
        path: str,
        api_id: str,
        headers: Optional[Dict[str, str]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        키움증권 서버로 HTTP 비동기 요청을 전송하고, 공통 오류 검사 및 응답 처리를 수행합니다.
        """
        url = f"{self.base_url}{path}"
        req_headers = {
            "content-type": "application/json;charset=UTF-8",
            "api-id": api_id,
        }

        # 인증 API(au10001, au10002)가 아닌 경우에만 Authorization 헤더에 토큰 자동 주입
        if api_id not in ("au10001", "au10002"):
            token = await self.client.get_valid_token()
            req_headers["authorization"] = f"Bearer {token}"

        if headers:
            req_headers.update(headers)

        # Rate Limiting: 유량 제어가 필요한 경우 대기 처리
        if hasattr(self.client, "limiter") and self.client.limiter:
            await self.client.limiter.wait(api_id)

        async with httpx.AsyncClient(http2=True) as http_client:
            try:
                response = await http_client.request(
                    method=method,
                    url=url,
                    headers=req_headers,
                    json=json_data,
                    timeout=10.0,
                )

                # HTTP 에러 체크 (4xx, 5xx)
                response.raise_for_status()

            except httpx.HTTPStatusError as e:
                # HTTP 인증 실패나 서버 에러의 경우 예외 번역
                status_code = e.response.status_code
                if status_code in (401, 403):
                    raise KiwoomAuthError(
                        f"HTTP {status_code}: API 접근 권한이 없거나 토큰 인증 실패"
                    ) from e
                raise KiwoomError(f"HTTP 통신 오류 발생 (상태 코드: {status_code})") from e
            except httpx.RequestError as e:
                raise KiwoomError(f"키움 서버 연결 실패: {e}") from e

            # 응답 데이터 파싱
            try:
                resp_json = cast(Dict[str, Any], response.json())
            except ValueError as e:
                raise KiwoomError("키움 서버로부터 올바르지 않은 JSON 응답을 받았습니다.") from e

            # 키움 비즈니스 에러 검사 (에러 코드 필드 감지 시)
            # 예: {"rtn_cd": "7", "err_code": "1511", "err_msg": "필수 입력값 누락..."}
            err_code = resp_json.get("err_code")
            if err_code:
                err_msg = resp_json.get("err_msg", "알 수 없는 API 에러")
                self._handle_business_error(str(err_code), str(err_msg))

            return resp_json

    def _handle_business_error(self, code: str, message: str) -> None:
        """
        키움 서버에서 반환한 특정 에러 코드 번호에 매핑되는 예외를 던집니다.
        """
        # 에러 코드 대역별 예외 세분화
        if code.startswith("8"):
            # 8xxx 번대: 토큰 인증 / 단말기 미등록 관련
            raise KiwoomAuthError(code, message)
        elif code in ("1700", "1701", "1702", "1687"):
            # 17xx 번대: 유량 제한 초과
            raise KiwoomRateLimitError(code, message)
        elif code.startswith("15"):
            # 15xx 번대: 필수값 누락, 타입 에러 등 입력 유효성 검사 실패
            raise KiwoomValidationError(code, message)
        else:
            # 기타 오류
            raise KiwoomAPIError(code, message)
