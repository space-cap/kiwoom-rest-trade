import time

import pytest

from kiwoom.limiter import RateLimiter


@pytest.mark.asyncio
async def test_domestic_rate_limiting() -> None:
    """국내주식 API의 1초 5회(0.2초 간격) 유량 제한이 올바르게 보장되는지 테스트합니다."""
    limiter = RateLimiter(is_mock=False)

    start_time = time.time()
    # 5회 연속 대기 실행 (첫 호출은 딜레이가 없고, 2번째부터 0.2초씩 총 4번 대기하므로 약 0.8초 소요)
    tasks = [limiter.wait("ka10001") for _ in range(5)]

    # 순차적으로 비동기 실행되도록 대기
    for task in tasks:
        await task

    elapsed = time.time() - start_time
    print(f"Domestic rate limit elapsed: {elapsed:.4f}s")

    # 0.8초 이상 소요되었는지 검증 (오차 감안하여 최소 0.75초 이상)
    assert elapsed >= 0.75


@pytest.mark.asyncio
async def test_mock_rate_limiting() -> None:
    """모의투자 모드에서 1초 1회(1.0초 간격) 유량 제한이 보장되는지 테스트합니다."""
    limiter = RateLimiter(is_mock=True)

    start_time = time.time()
    # 2회 연속 대기 실행 (1번 대기하므로 약 1.0초 소요)
    await limiter.wait("ka10001")
    await limiter.wait("ka10001")

    elapsed = time.time() - start_time
    print(f"Mock rate limit elapsed: {elapsed:.4f}s")

    # 1.0초 이상 소요되었는지 검증 (오차 감안하여 최소 0.95초 이상)
    assert elapsed >= 0.95


@pytest.mark.asyncio
async def test_independent_categories() -> None:
    """국내주식과 미국주식 카테고리가 서로 간섭 없이 독립적으로 제어되는지 테스트합니다."""
    limiter = RateLimiter(is_mock=False)

    start_time = time.time()

    # 국내 1회 호출 후 즉시 미국 1회 호출 (락이 분리되어 있으므로 두 카테고리 간의 지연은 발생하지 않음)
    await limiter.wait("ka10001")
    await limiter.wait("oa10001")

    elapsed = time.time() - start_time
    print(f"Independent category elapsed: {elapsed:.4f}s")

    # 두 개의 카테고리가 다르고 첫 호출들이므로 대기 시간 없이 즉시 반환되어야 함 (0.05초 미만)
    assert elapsed < 0.05
