import asyncio
import time
from datetime import datetime
from typing import Dict


class RateLimiter:
    """
    비동기 환경에서 키움증권 API 호출 속도를 제어하는 스마트 속도 제한기입니다.
    카테고리별(국내주식, 미국주식, 인증, 모의투자)로 독립된 락(Lock)을 사용하여 호출 주기를 정밀하게 강제합니다.
    """

    def __init__(self, is_mock: bool = False) -> None:
        self.is_mock = is_mock

        # 각 카테고리별 마지막 호출 타임스탬프 저장소
        self._last_called: Dict[str, float] = {
            "mock": 0.0,
            "domestic": 0.0,
            "overseas": 0.0,
            "auth": 0.0,
        }

        # 카테고리별 독립 비동기 락
        self._locks: Dict[str, asyncio.Lock] = {
            "mock": asyncio.Lock(),
            "domestic": asyncio.Lock(),
            "overseas": asyncio.Lock(),
            "auth": asyncio.Lock(),
        }

    def _determine_category(self, api_id: str) -> str:
        """API ID를 분석하여 유량 카테고리를 결정합니다."""
        if self.is_mock:
            return "mock"

        api_id_lower = api_id.lower()
        if api_id_lower.startswith("au"):
            return "auth"
        elif api_id_lower.startswith(("ka", "kt")) or api_id_lower[0].isdigit():
            # 국내주식 (ka: 시세/조회, kt: 주문/계좌, 숫자로 시작하는 실시간 코드)
            return "domestic"
        elif api_id_lower.startswith(("oa", "ot")):
            # 미국주식 (oa: 해외시세, ot: 해외주문/환전)
            return "overseas"
        else:
            # 기본적으로는 국내주식 보수적 기준으로 설정
            return "domestic"

    def _get_delay(self, category: str) -> float:
        """카테고리에 부합하는 호출 주기 딜레이(초 단위)를 반환합니다."""
        if category == "mock":
            # 모의투자: 1초 1회
            return 1.0
        elif category == "auth":
            # 인증 API: 속도 제한이 비교적 너그러우나 안전하게 0.1초 적용
            return 0.1
        elif category == "domestic":
            # 국내주식 실전투자: 1초 5회 (0.2초 간격)
            return 0.2
        elif category == "overseas":
            # 미국주식 실전투자: 1초 10회 (0.1초 간격)
            # 단, 피크타임(한국시각 오전 9시 ~ 10시)에는 1초 3회 제한 (0.33초 간격)
            now_hour = datetime.now().hour
            if now_hour == 9:
                return 0.33
            return 0.1
        return 0.2

    async def wait(self, api_id: str) -> None:
        """
        API 호출 전 실행되며, 해당 API ID의 카테고리 한도에 맞춰 자동으로 비동기 대기 처리를 수행합니다.
        """
        category = self._determine_category(api_id)
        delay = self._get_delay(category)
        lock = self._locks[category]

        async with lock:
            now = time.time()
            last = self._last_called[category]
            elapsed = now - last

            # 이전 호출 이후 대기해야 하는 시간 계산
            sleep_time = delay - elapsed
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)

            # 마지막 호출 완료 시점을 현재 시점으로 업데이트
            self._last_called[category] = time.time()
