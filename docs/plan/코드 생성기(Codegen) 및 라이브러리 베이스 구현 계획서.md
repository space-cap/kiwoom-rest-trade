# 코드 생성기(Codegen) 및 라이브러리 베이스 구현 계획서

이 구현 계획서는 `kiwoom-rest-trade` 라이브러리의 핵심 기능을 담당할 코드 생성기(`tools/codegen.py`) 및 공통 부모 클래스들(`kiwoom/models/base.py`, `kiwoom/api/base.py`)의 구현 단계를 다룹니다.

---

## 🛠️ 핵심 작업 범위

### 1. 베이스 모델 및 API 구현
* **`kiwoom/models/base.py`**:
  * 공통 Pydantic 베이스 모델 작성 (예: snake_case 변환 및 직렬화 헬퍼 등)
* **`kiwoom/api/base.py`**:
  * `httpx.AsyncClient`를 품고 있는 `BaseAPI` 클래스 구현
  * OAuth 토큰 자동 첨부 및 유량 제어(Rate Limit) 대기 처리 연동
  * 응답 헤더/바디 내의 에러 코드가 발견될 시 커스텀 예외로 번역하여 `raise` 하는 공통 에러 핸들러 연동

### 2. 코드 생성기 구현 (`tools/codegen.py`)
* `data/kiwoom_api_spec.json`을 열어 데이터 분류 및 필터링
* 키움의 필드 타입(String, Number 등)을 Python 표준 힌팅으로 안전하게 전환하는 맵핑 함수 개발
* Pydantic 클래스 정의용 f-string 템플릿 기반 코드 생성 로직 개발
* REST API 호출 비동기 메서드 정의용 f-string 템플릿 기반 코드 생성 로직 개발
* 생성 결과를 `kiwoom/models/{category}.py` 및 `kiwoom/api/{category}.py` 로 각각 출력 및 저장

### 3. 코드젠 실행 및 정적 분석 정규화
* `uv run python tools/codegen.py` 실행
* `ruff` 포맷터 및 `mypy` 검사를 통한 코드 결함 검증

---

## Proposed Changes

### [NEW] [codegen.py](file:///c:/workdir/space-cap/kiwoom-rest-trade/tools/codegen.py)
* 337개 API 스펙을 파싱하여 코드 생성을 수행하는 메인 스크립트입니다.

### [MODIFY] [base.py (models)](file:///c:/workdir/space-cap/kiwoom-rest-trade/kiwoom/models/base.py)
* Pydantic 공통 모델 설정을 담습니다.

### [MODIFY] [base.py (api)](file:///c:/workdir/space-cap/kiwoom-rest-trade/kiwoom/api/base.py)
* 공통 HTTP 요청 발송 및 오류 처리를 전담하는 Base API 클래스입니다.

---

## Verification Plan

### Automated Tests
* 코드 생성기 실행: `uv run python tools/codegen.py`
* 생성된 코드에 대해 린트 및 포맷 정렬: `uv run ruff format kiwoom/`
* 타입 정적 분석 수행: `uv run mypy kiwoom/`
