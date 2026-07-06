import asyncio
from typing import Any, Coroutine, cast

from kiwoom.api.auth import AuthAPI
from kiwoom.api.domestic import DomesticAPI
from kiwoom.api.overseas import OverseasAPI
from kiwoom.auth import TokenManager
from kiwoom.limiter import RateLimiter


class AsyncKiwoomClient:
    """
    키움증권 REST API의 비동기 통합 클라이언트 클래스입니다.
    인증 모듈, 유량 제한, 카테고리별 API를 내장하여 일괄 제어합니다.
    """

    def __init__(self, appkey: str, secretkey: str, is_mock: bool = False) -> None:
        self.is_mock = is_mock

        # 인증 매니저 및 유량 제어기 초기화
        self.token_manager = TokenManager(appkey, secretkey, is_mock)
        self.limiter = RateLimiter(is_mock)

        # 각 카테고리별 API 인터페이스 바인딩
        self.auth = AuthAPI(self)
        self.domestic = DomesticAPI(self)
        self.overseas = OverseasAPI(self)

    async def get_valid_token(self) -> str:
        """내부 토큰 매니저로부터 유효한 접근 토큰을 비동기 획득합니다."""
        return await self.token_manager.get_valid_token()


class SyncAPIProxy:
    """
    비동기 API 메서드를 가로채서 이벤트 루프 상에서 동기식으로 실행해주는 프록시 클래스입니다.
    """

    def __init__(self, async_api: Any, loop: asyncio.AbstractEventLoop) -> None:
        self._async_api = async_api
        self._loop = loop

    def __getattr__(self, name: str) -> Any:
        async_attr = getattr(self._async_api, name)
        if callable(async_attr):

            def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
                coro = cast(Coroutine[Any, Any, Any], async_attr(*args, **kwargs))
                if self._loop.is_running():
                    # Jupyter Notebook 등 이미 이벤트 루프가 돌고 있는 환경에서의 대응
                    future = asyncio.run_coroutine_threadsafe(coro, self._loop)
                    return future.result()
                else:
                    return self._loop.run_until_complete(coro)

            return sync_wrapper
        return async_attr


class KiwoomClient:
    """
    비동기 처리에 익숙하지 않은 사용자를 위한 동기식 통합 클라이언트 클래스입니다.
    내부적으로 비동기 클라이언트를 프록시하여 동기 호출 방식으로 자동 변환합니다.
    """

    def __init__(self, appkey: str, secretkey: str, is_mock: bool = False) -> None:
        self._async_client = AsyncKiwoomClient(appkey, secretkey, is_mock)

        # 이벤트 루프 초기화
        try:
            self._loop = asyncio.get_event_loop()
        except RuntimeError:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)

        # 동기식 API 프록시 바인딩
        self.auth = SyncAPIProxy(self._async_client.auth, self._loop)
        self.domestic = SyncAPIProxy(self._async_client.domestic, self._loop)
        self.overseas = SyncAPIProxy(self._async_client.overseas, self._loop)
