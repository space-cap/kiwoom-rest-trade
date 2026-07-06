import asyncio
import os
import sys
from dotenv import load_dotenv

# 패키지 로드 경로 설정 (프로젝트 루트 임포트 보장)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kiwoom import AsyncKiwoomClient, KiwoomClient
from kiwoom.models.domestic import Ka10001Request
from kiwoom.exceptions import KiwoomError

def get_env_credentials() -> tuple[str, str, bool]:
    """.env 파일에서 환경변수를 로드하여 검증한 뒤 반환합니다."""
    # .env 파일 수동 지정 로드
    load_dotenv(override=True)
    
    appkey = os.getenv("KIWOOM_APPKEY", "").strip()
    secretkey = os.getenv("KIWOOM_SECRETKEY", "").strip()
    is_mock_str = os.getenv("KIWOOM_IS_MOCK", "True").strip().lower()
    is_mock = is_mock_str in ("true", "1", "yes")

    if not appkey or appkey == "your_actual_app_key_here":
        print("[FAIL] 에러: .env 파일에 올바른 KIWOOM_APPKEY를 기입해 주세요.")
        sys.exit(1)
        
    if not secretkey or secretkey == "your_actual_secret_key_here":
        print("[FAIL] 에러: .env 파일에 올바른 KIWOOM_SECRETKEY를 기입해 주세요.")
        sys.exit(1)

    return appkey, secretkey, is_mock

async def run_async_test(appkey: str, secretkey: str, is_mock: bool) -> None:
    """비동기 클라이언트를 사용해 실서버 API 연동을 검증합니다."""
    print("\n--------------------------------------------------")
    print("[-] [1/2] AsyncKiwoomClient (비동기) 실서버 테스트 시작...")
    print("--------------------------------------------------")
    
    client = AsyncKiwoomClient(appkey=appkey, secretkey=secretkey, is_mock=is_mock)
    
    try:
        # 1. 토큰 테스트
        print("1. 토큰 발급 시도 중...")
        token = await client.get_valid_token()
        print(f"[OK] 토큰 발급 성공! (앞 15자리: {token[:15]}...)")
        
        # 2. 국내주식 시세 테스트 (삼성전자: 005930)
        print("2. 삼성전자(005930) 주식기본정보 조회 시도 중...")
        req = Ka10001Request(stk_cd="005930")
        resp = await client.domestic.ka10001(req)
        
        print("\n[SUCCESS] [비동기 테스트 성공 결과]")
        print(f"   - 종목코드: {resp.stk_cd}")
        print(f"   - 종목명  : {resp.stk_nm}")
        print(f"   - 현재가  : {resp.cur_prc}원")
        print(f"   - 대비기호: {resp.pre_sig or ''}")
        print(f"   - 등락률  : {resp.flu_rt or '0.0'}%")
        
    except KiwoomError as e:
        print(f"[FAIL] 키움 API 연동 실패 (비동기): {e}")
    except Exception as e:
        print(f"[FAIL] 예상치 못한 시스템 오류 발생 (비동기): {e}")

def run_sync_test(appkey: str, secretkey: str, is_mock: bool) -> None:
    """동기식 래퍼 클라이언트를 사용해 실서버 API 연동을 검증합니다."""
    print("\n--------------------------------------------------")
    print("[-] [2/2] KiwoomClient (동기) 실서버 테스트 시작...")
    print("--------------------------------------------------")
    
    client = KiwoomClient(appkey=appkey, secretkey=secretkey, is_mock=is_mock)
    
    try:
        # 1. 국내주식 시세 테스트 (삼성전자: 005930)
        print("1. 삼성전자(005930) 주식기본정보 동기 조회 시도 중...")
        req = Ka10001Request(stk_cd="005930")
        
        # 동기식 API 호출
        resp = client.domestic.ka10001(req)
        
        print("\n[SUCCESS] [동기 테스트 성공 결과]")
        print(f"   - 종목코드: {resp.stk_cd}")
        print(f"   - 종목명  : {resp.stk_nm}")
        print(f"   - 현재가  : {resp.cur_prc}원")
        
    except KiwoomError as e:
        print(f"[FAIL] 키움 API 연동 실패 (동기): {e}")
    except Exception as e:
        print(f"[FAIL] 예상치 못한 시스템 오류 발생 (동기): {e}")

if __name__ == "__main__":
    appkey, secretkey, is_mock = get_env_credentials()
    
    mode_name = "모의투자" if is_mock else "실전투자"
    print(f"[START] 실서버 연동 테스트 환경 감지 성공 (접속 모드: {mode_name})")
    
    # 1. 비동기 테스트 실행
    asyncio.run(run_async_test(appkey, secretkey, is_mock))
    
    # 2. 동기 테스트 실행
    run_sync_test(appkey, secretkey, is_mock)
    
    print("\n================ E2E 테스트 프로세스 종료 ================")
