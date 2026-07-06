# 🧱 통합 클라이언트(client.py) 조립 및 유닛 테스트 구현 계획서

이 구현 계획서는 개발된 개별 퍼즐 조각들(인증 매니저, 유량 제어기, 자동생성된 API 명세)을 하나로 통합하는 **최종 진입점 클라이언트** 구현과 전체 연동 유닛 테스트 단계를 다룹니다.

---

## 🛠️ 세부 구현 설계

### 1. 통합 비동기 클라이언트 (`kiwoom/client.py`)
사용자가 패키지 로드 후 직접 다루게 될 메인 리모컨 클래스들을 조립합니다.

* **`AsyncKiwoomClient` (비동기 클라이언트)**:
  * 생성자 인자: `appkey`, `secretkey`, `is_mock=False`
  * 인증기(`TokenManager`) 및 속도한도 지연기(`RateLimiter`)를 내부 멤버로 자동 생성 및 연동.
  * 자동 생성된 API 모듈들을 각각 멤버 프로퍼티로 주입:
    * `self.auth = AuthAPI(self)`
    * `self.domestic = DomesticAPI(self)`
    * `self.overseas = OverseasAPI(self)`
  * 베이스 API 모듈(`base.py`)이 토큰이 필요할 때 호출하는 `get_valid_token()` 메서드를 래핑 제공.

* **`KiwoomClient` (동기식 래퍼)**:
  * 비동기(`asyncio`)에 익숙하지 않은 사용자나 동기식 퀀트 백테스팅 엔진과의 연동을 위해 비동기 코루틴 호출을 동기식으로 일괄 처리할 수 있는 이벤트 루프 러너(`run()`) 및 동기 호출 구조 제공.

### 2. 클라이언트 통합 연동 테스트 (`tests/test_client.py`)
* 모킹(Mocking)을 적용해 `AsyncKiwoomClient` 생성 후 실제 국내 주식 조회 TR(`ka10001`) 함수를 호출해 봅니다.
* 이 과정에서 `get_valid_token()` 갱신과 `RateLimiter` 딜레이 제어기가 유기적으로 협력하여 성공적인 응답 모델을 리턴하는지 전체 흐름을 테스트합니다.

---

## Proposed Changes

### [NEW] [client.py](file:///c:/workdir/space-cap/kiwoom-rest-trade/kiwoom/client.py)
* `AsyncKiwoomClient` 및 `KiwoomClient` 클래스를 정의하고 관련 모듈들을 임포트하여 조립합니다.

### [NEW] [test_client.py](file:///c:/workdir/space-cap/kiwoom-rest-trade/tests/test_client.py)
* 클라이언트 연동 유닛 테스트 코드를 작성합니다.

---

## Verification Plan

### Automated Tests
* 통합 클라이언트 테스트 실행: `uv run pytest tests/test_client.py -v`
* 전체 테스트 일괄 수행: `uv run pytest -v` (전체 8종 이상 테스트 통과 확인)
* Ruff 린터 및 Mypy 타입 정적 분석 검사 실행
