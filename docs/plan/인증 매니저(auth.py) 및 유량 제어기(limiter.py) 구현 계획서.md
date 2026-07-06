# 🔐 인증 매니저(auth.py) 및 ⚡ 유량 제어기(limiter.py) 구현 계획서

이 구현 계획서는 키움 REST API의 안정적인 구동에 가장 중요한 **토큰 자동 갱신** 및 **비동기 유량 제어** 로직의 구현 단계를 다룹니다.

---

## 🛠️ 세부 구현 설계

### 1. 토큰 자동 갱신 인증 매니저 (`kiwoom/auth.py`)
키움 Access Token의 유효 기간(보통 24시간) 만료에 안전하게 대비하기 위해, 비동기 환경에서 동작하는 토큰 관리자를 구현합니다.

* **동작 시나리오**:
  * API 호출 시 매번 `get_valid_token()`을 호출합니다.
  * 토큰이 아예 없거나 만료 임박 상태(만료 10분 전)인 경우, 비동기 락(`asyncio.Lock`)을 활용하여 다중 코루틴 환경에서도 **단 한 번만 토큰 갱신 API를 호출**하도록 동시성을 제어합니다.
  * 갱신된 토큰과 만료 시간을 메모리에 안전하게 캐싱합니다.
* **사용 엔드포인트**:
  * `au10001` (접근토큰 발급, POST `/oauth2/token`)

### 2. 스마트 비동기 유량 제어기 (`kiwoom/limiter.py`)
비동기 환경에서 다수의 주문/조회 코루틴들이 실행될 때, 키움의 유량 제한 정책(1초당 5회 등)을 초과하여 차단되지 않도록 조율하는 역할을 합니다.

* **동작 시나리오**:
  * API ID 또는 카테고리에 대응하는 각각의 비동기 속도 제한(Rate Limiter)을 둡니다.
  * **속도 제한 정책**:
    * 모의투자: 카테고리 무관 1초당 1회 (`1.0초` 딜레이)
    * 국내주식 (조회/주문): 1초당 5회 (`0.2초` 딜레이)
    * 미국주식 (조회/주문): 1초당 10회 (`0.1초` 딜레이) 단, 피크타임(한국시각 09:00 ~ 10:00)에는 1초당 3회 (`0.33초` 딜레이)
  * 비동기 `wait(api_id)` 메서드는 호출 주기 차이를 계산해 필요 시 자동으로 `await asyncio.sleep(diff)`를 수행합니다.

---

## Proposed Changes

### [NEW] [auth.py](file:///c:/workdir/space-cap/kiwoom-rest-trade/kiwoom/auth.py)
* `TokenManager` 클래스를 작성하여 AppKey/SecretKey 관리 및 비동기 토큰 갱신 로직을 구현합니다.

### [NEW] [limiter.py](file:///c:/workdir/space-cap/kiwoom-rest-trade/kiwoom/limiter.py)
* `RateLimiter` 클래스를 구현하여 동시성 세마포어/락 기반 속도 지연 처리를 담당하게 합니다.

---

## Verification Plan

### Automated Tests
* 유량 제어기 작동 유닛 테스트 작성 (`tests/test_limiter.py`)
  * 예: 1초당 5회 제한 상황에서 10회 연속 호출 시 총 소요 시간이 최소 1.8초 이상 걸리는지 검증.
* 임시 Mock 토큰 서버를 활용하여 토큰 갱신 테스트 코드 작성 (`tests/test_auth.py`)
