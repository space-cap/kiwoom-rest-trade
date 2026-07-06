# 🛠️ kiwoom-rest-trade 개발 환경 설정 가이드 (DEVELOPMENT_ENV.md)

본 문서는 `kiwoom-rest-trade` 라이브러리를 개발하기 위해 차세대 초고속 파이썬 패키지 매니저인 **`uv`**를 사용하여 개발 환경을 구축하고, 정적 분석 및 테스트 도구를 설정하는 가이드입니다.

---

## 1. 개발 도구 및 기술 스택

* **Python**: `>=3.10` (최신 비동기 문법 및 패턴 매칭 활용을 위해 Python 3.10 이상 권장)
* **패키지 및 의존성 관리**: `uv` (Rust 기반의 초고속 올인원 파이썬 패키지 및 프로젝트 매니저)
* **린터 & 포맷터**: `Ruff` (매우 빠른 속도와 다양한 린트 룰셋 통합 제공)
* **타입 체커**: `Mypy` (엄격한 타입 체크를 통한 버그 방지)
* **테스트 도구**: `Pytest` + `pytest-asyncio` (비동기 유닛/통합 테스트 최적화)

---

## 2. 프로젝트 초기화 및 가상환경 설정 (`uv` 기반)

`uv`는 파이썬 설치부터 가상환경 생성, 의존성 동기화까지 번개처럼 빠르게 처리합니다.

### 2.1. `uv` 설치 (설치되어 있지 않은 경우)
```bash
# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2.2. 파이썬 가상환경 생성 및 활성화
`uv`를 사용하면 프로젝트 폴더에 바로 가상환경을 생성하고, 자동으로 파이썬 버전까지 다운로드하여 적용해 줍니다.
```bash
# 프로젝트 폴더 내부에 파이썬 3.10 기반 가상환경(.venv) 생성
uv venv --python 3.10

# 가상환경 활성화 (Windows PowerShell)
.venv\Scripts\activate

# 가상환경 활성화 (Mac / Linux)
source .venv/bin/activate
```

### 2.3. 의존성 패키지 동기화 (설치)
`uv.lock`과 `pyproject.toml`에 기재된 모든 개발/런타임 패키지를 초고속으로 설치합니다.
```bash
uv sync
```

---

## 3. pyproject.toml 표준 템플릿 (PEP 621 준수)

`uv`는 특정 도구 전용 포맷 대신, 파이썬 공식 표준 스펙인 **PEP 621** 기반의 `pyproject.toml`을 기본으로 사용합니다. 빌드 백엔드로는 가볍고 현대적인 `hatchling`을 권장합니다.

```toml
[project]
name = "kiwoom-rest-trade"
version = "0.1.0"
description = "키움증권 신형 REST/WebSocket API 비동기 파이썬 SDK"
readme = "README.md"
requires-python = ">=3.10"
license = { text = "MIT" }
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
dependencies = [
    "httpx[http2]>=0.27.0",
    "websockets>=12.0",
    "pydantic>=2.6.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# 개발용 의존성 정의 (uv 전용 dependency-groups 또는 기본 optional-dependencies)
[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "ruff>=0.2.0",
    "mypy>=1.8.0",
]

# Ruff 설정 (린터 & 포맷터)
[tool.ruff]
target-version = "py310"
line-length = 100

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (임포트 정렬)
    "B",   # flake8-bugbear (잠재적 버그)
    "RUF", # Ruff 고유 규칙
]

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

# Hatch 빌드 대상 패키지 경로 명시
[tool.hatch.build.targets.wheel]
packages = ["kiwoom"]
```

---

## 4. 품질 관리 및 린트 검사 방법

`uv`를 사용하면 가상환경 내에 설치된 실행 도구들을 `uv run`을 통해 격리되어 안전하고 빠르게 실행할 수 있습니다.

### 4.1. 린트 및 임포트 정리 (Ruff)
```bash
# 코드 검사 및 자동 수정(Auto-fix)
uv run ruff check . --fix

# 코드 포맷팅
uv run ruff format .
```

### 4.2. 정적 타입 검사 (Mypy)
```bash
uv run mypy kiwoom
```

---

## 5. 테스트 환경 및 검증 전략 (Testing)

### 5.1. 유닛 테스트 실행
```bash
uv run pytest
```

### 5.2. 비동기 테스트 기본 예시 (`tests/test_client.py`)
```python
import pytest
from kiwoom import AsyncKiwoomClient

@pytest.mark.asyncio
async def test_get_balance(mock_kiwoom_server):
    client = AsyncKiwoomClient(appkey="test_key", secretkey="test_secret")
    balance = await client.domestic.get_balance(acnt_no="1234567890")
    
    assert balance.acnt_no == "1234567890"
    assert balance.tot_evlu_amt > 0

---

## 6. 패키지 빌드 및 배포 방법 (Packaging & Publishing)

본 라이브러리는 `uv`와 `hatchling` 빌드 백엔드를 표준으로 채택하고 있으므로, 빌드 및 PyPI 업로드 과정 또한 단순하고 직관적입니다.

### 6.1. 배포 패키지 빌드 (Build)
`pyproject.toml` 스펙에 따라 휠(whl)과 소스 배포판(tar.gz)을 컴파일 및 생성합니다.
```bash
# dist/ 폴더 하위에 빌드 아티팩트 생성
uv build
```

### 6.2. PyPI 패키지 릴리즈 및 배포 (Publish)
빌드된 패키지 파일을 PyPI(Python Package Index) 공식 저장소에 업로드(배포)합니다. 
```bash
# 공식 PyPI 배포 실행 (PyPI API Token 필요)
uv publish
```

* 💡 **TestPyPI에 테스트 배포 해보기**:
  실제 배포 전에 패키지 형식이 잘 맞는지 TestPyPI 임시 서버에 먼저 배포해 볼 수 있습니다.
  ```bash
  uv publish --publish-url https://test.pypi.org/legacy/
  ```

```
