# 🛠️ kiwoom-rest-trade 개발 환경 설정 가이드 (DEVELOPMENT_ENV.md)

본 문서는 `kiwoom-rest-trade` 라이브러리를 개발하기 위해 개발 환경을 구축하고, 정적 분석 및 테스트 도구를 설정하는 가이드입니다. 이 패키지는 최신 파이썬 패키징 표준 및 개발 툴체인을 따릅니다.

---

## 1. 개발 도구 및 기술 스택

* **Python**: `^3.10` (최신 비동기 문법 및 패턴 매칭 활용을 위해 Python 3.10 이상 권장)
* **패키지 및 의존성 관리**: `Poetry` (의존성 잠금 및 PyPI 배포의 사실상 표준)
* **린터 & 포맷터**: `Ruff` (매우 빠른 속도와 다양한 린트 룰셋 통합 제공)
* **타입 체커**: `Mypy` (엄격한 타입 체크를 통한 버그 방지)
* **테스트 도구**: `Pytest` + `pytest-asyncio` (비동기 유닛/통합 테스트 최적화)

---

## 2. 프로젝트 초기화 및 가상환경 설정

이 프로젝트는 `Poetry`를 사용하여 패키지를 구성합니다. 프로젝트 루트 디렉토리(`kiwoom-rest-trade`)에서 가상환경 및 의존성 설치를 진행합니다.

### 2.1. Poetry 설치 (설치되어 있지 않은 경우)
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Mac / Linux
curl -sSL https://install.python-poetry.org | python3 -
```

### 2.2. 프로젝트 내 가상환경 설정 (`.venv` 활성화)
Poetry가 가상환경을 프로젝트 내부 폴더(`.venv`)에 생성하도록 설정하여 VS Code 등 IDE와의 연동성을 높입니다.
```bash
poetry config virtualenvs.in-project true
```

### 2.3. 의존성 설치
개발용 패키지와 런타임 필수 패키지를 모두 설치합니다.
```bash
poetry install
```

---

## 3. pyproject.toml 기본 템플릿

프로젝트의 빌드 정의, 의존성, 린터/포맷터 도구 설정을 일괄적으로 관리하는 `pyproject.toml` 설정 파일 가이드입니다.

```toml
[tool.poetry]
name = "kiwoom-rest-trade"
version = "0.1.0"
description = "키움증권 신형 REST/WebSocket API 비동기 파이썬 SDK"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"
license = "MIT"
packages = [{include = "kiwoom"}]

[tool.poetry.dependencies]
python = "^3.10"
httpx = {extras = ["http2"], version = "^0.27.0"}
websockets = "^12.0"
pydantic = "^2.6.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.0.0"
pytest-asyncio = "^0.23.0"
ruff = "^0.2.0"
mypy = "^1.8.0"
black = "^24.1.0"  # 필요 시 추가 사용

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

# Ruff 설정 (린터 & 포맷터)
[tool.ruff]
target-version = "py310"
line-length = 100
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (임포트 정렬)
    "B",   # flake8-bugbear (잠재적 버그)
    "RUF", # Ruff 고유 규칙
]
ignore = []

# Mypy 설정 (타입 체크)
[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true  # 엄격한 타입 정의 강제
disallow_incomplete_defs = true
ignore_missing_imports = true

# Pytest 설정
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

---

## 4. 품질 관리 및 린트 검사 방법

코드를 작성하거나 자동 생성한 뒤, 빌드/커밋 전 품질 도구를 실행하여 코드 일관성을 유지합니다.

### 4.1. 린트 및 임포트 정리 (Ruff)
Ruff를 이용해 정적 분석 및 임포트 자동 정렬을 수행합니다.
```bash
# 코드 검사 및 자동 수정(Auto-fix)
poetry run ruff check . --fix

# 코드 포맷팅 검사
poetry run ruff format .
```

### 4.2. 정적 타입 검사 (Mypy)
패키지 모듈에 대해 완벽한 타입 안전성을 유지하는지 검사합니다.
```bash
poetry run mypy kiwoom
```

---

## 5. 테스트 환경 및 검증 전략 (Testing)

모의(Mock) 통신 환경을 구축하여 키움 실서버 없이도 테스트가 가능하도록 비동기 Mock 테스트 체계를 구성합니다.

### 5.1. 유닛 테스트 실행
```bash
poetry run pytest
```

### 5.2. 비동기 테스트 기본 예시 (`tests/test_client.py`)
```python
import pytest
from kiwoom import AsyncKiwoomClient

@pytest.mark.asyncio
async def test_get_balance(mock_kiwoom_server):
    # Mock 서버 컨텍스트 하에서 동작 테스트
    client = AsyncKiwoomClient(appkey="test_key", secretkey="test_secret")
    # API 요청
    balance = await client.domestic.get_balance(acnt_no="1234567890")
    
    assert balance.acnt_no == "1234567890"
    assert balance.tot_evlu_amt > 0
```
