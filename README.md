# 📈 kiwoom-rest-trade

> **키움증권 신형 REST API를 위한 차세대 비동기(Async) / 동기(Sync) 통합 파이썬 SDK**

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/kiwoom-rest-trade/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black.svg)](https://github.com/astral-sh/ruff)

본 라이브러리는 키움증권에서 새롭게 출시한 REST API 규격을 파이썬 환경에서 안전하고 신속하게 사용할 수 있도록 돕는 SDK입니다. 337개의 국내주식, 해외(미국)주식, 계좌/예수금 관련 조회를 완벽한 타입 안전성(Type-safe)과 비동기 최적화로 지원합니다.

---

## ✨ 핵심 기능 (Features)

* 🚀 **Async-First (비동기 우선)**: 모든 통신은 `httpx[http2]` 기반의 비동기 코루틴으로 처리되어 고속 자동매매 I/O에 최적화되어 있습니다.
* 🧱 **동기식 래퍼(KiwoomClient) 지원**: 비동기 문법이 낯선 초보자나 백테스팅 환경을 위해 동적 프록시 패턴을 활용한 완전한 동기식 즉시 호출을 함께 제공합니다.
* 🤖 **337개 API 완벽 자동생성 (CodeGen)**: 키움 REST TR 명세를 100% 반영하여 복잡한 중첩 배열 구조까지 정밀한 Pydantic v2 데이터 모델로 완벽 복원했습니다.
* 🔐 **스마트 토큰 관리**: 비동기 Lock을 적용하여 토큰 만료 임박 시 동시 호출 상태에서도 백그라운드에서 오직 1회만 토큰을 안전하게 갱신합니다.
* ⚡ **스마트 유량 제어 (Rate Limiter)**: 국내주식(초당 5회), 미국주식(초당 10회, 피크타임 동적 지연보정) 등 가혹한 호출 한도를 지키도록 미세 대기(`asyncio.sleep`)를 자동 수행합니다.

---

## 🛠️ 설치 방법 (Installation)

파이썬 3.10 이상 환경에서 초고속 파이썬 패키지 매니저인 `uv` 또는 `pip`를 사용해 쉽게 설치할 수 있습니다.

```bash
# pip를 사용하는 경우
pip install kiwoom-rest-trade

# uv를 사용하는 경우
uv add kiwoom-rest-trade
```

---

## ⚡ 빠른 시작 (Quick Start)

사용 전 프로젝트 루트에 `.env` 파일을 만들고 키를 설정하십시오. (샘플 가이드는 `.env.example`을 참고하세요.)

### 1. 비동기식 호출 예시 (`AsyncKiwoomClient`)

```python
import asyncio
from kiwoom import AsyncKiwoomClient
from kiwoom.models.domestic import Ka10001Request

async def main():
    # 클라이언트 초기화 (.env에 저장된 키 또는 직접 인자 전달)
    client = AsyncKiwoomClient(
        appkey="YOUR_APP_KEY", 
        secretkey="YOUR_SECRET_KEY", 
        is_mock=True  # 모의투자 모드
    )
    
    # 삼성전자(005930) 주가 조회
    req = Ka10001Request(stk_cd="005930")
    resp = await client.domestic.ka10001(req)
    
    print(f"종목명: {resp.stk_nm}")
    print(f"현재가: {resp.cur_prc}원")
    print(f"등락률: {resp.flu_rt}%")

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. 동기식 호출 예시 (`KiwoomClient`)

```python
from kiwoom import KiwoomClient
from kiwoom.models.domestic import Ka10001Request

# 동기 클라이언트는 내부적으로 비동기 통신을 변환 처리합니다.
client = KiwoomClient(
    appkey="YOUR_APP_KEY", 
    secretkey="YOUR_SECRET_KEY", 
    is_mock=True
)

# await 없이 바로 동기식으로 데이터를 조회합니다.
req = Ka10001Request(stk_cd="005930")
resp = client.domestic.ka10001(req)

print(f"종목명: {resp.stk_nm}")
print(f"현재가: {resp.cur_prc}원")
```

---

## 📅 로드맵 & 마일스톤 (Roadmap)

* **v0.1.0 (현재)**: REST API 기반 구축, 337개 조회 API 자동 생성, 토큰 자동 갱신 및 비동기 유량 제어기 구현 완료. (E2E 실서버 연동 검증 통과)
* **v0.2.0 (향후)**: 국내주식/해외주식 비동기 실주문(Order) 및 체결 정합성 검증 추가.
* **v0.3.0 (향후)**: WebSocket 기반 실시간 호가/체결 스트리밍 수신 모듈(`websocket.py`) 탑재.

---

## 📄 라이선스 (License)

본 라이브러리는 [MIT License](LICENSE) 하에 배포됩니다.
