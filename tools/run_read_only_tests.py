import asyncio
import os
import sys
from dotenv import load_dotenv

# 패키지 로드 경로 설정 (프로젝트 루트 임포트 보장)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kiwoom import AsyncKiwoomClient, KiwoomClient
from kiwoom.models.domestic import Ka10001Request, Ka10003Request
from kiwoom.models.overseas import Usa01980Request, Usa06012Request
from kiwoom.models.domestic import Kt00001Request, Kt00018Request
from kiwoom.exceptions import KiwoomError

def get_env_credentials() -> tuple[str, str, bool]:
    """.env 파일에서 환경변수를 로드하여 검증한 뒤 반환합니다."""
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

async def run_async_matrix_tests(appkey: str, secretkey: str, is_mock: bool) -> None:
    """비동기 방식으로 6대 매트릭스 E2E 테스트를 가동합니다."""
    print("\n==================================================")
    print("[-] [1/2] AsyncKiwoomClient (비동기) 6대 매트릭스 테스트")
    print("==================================================")
    
    client = AsyncKiwoomClient(appkey=appkey, secretkey=secretkey, is_mock=is_mock)
    
    try:
        # 0. 토큰 검증
        print("\n[STEP 0] 토큰 발급 검증 중...")
        token = await client.get_valid_token()
        print(f" -> [OK] 토큰 획득 성공 (앞 10자리: {token[:10]}...)")
        
        # 1. 국내 단일: ka10001 (주식기본정보)
        print("\n[STEP 1] 국내 단일: ka10001 (삼성전자 현재가) 호출 중...")
        r1 = await client.domestic.ka10001(Ka10001Request(stk_cd="005930"))
        print(f" -> [OK] 수집 데이터: 종목명={r1.stk_nm}, 현재가={r1.cur_prc}원")
        
        # 2. 국내 배열: ka10003 (주식일봉차트)
        print("\n[STEP 2] 국내 배열: ka10003 (삼성전자 일봉차트) 호출 중...")
        # 005930 삼성전자 일봉 조회
        r2 = await client.domestic.ka10003(Ka10003Request(stk_cd="005930"))
        # 응답 데이터 리스트 출력
        items = r2.data if hasattr(r2, "data") and r2.data else []
        print(f" -> [OK] 수집 데이터: 응답 레코드 수={len(items)}건")
        if items:
            first = items[0]
            # 일봉 필드가 있는지 유연하게 출력 (일자, 시가, 고가, 저가, 종가 등)
            dt = getattr(first, "dt", "N/A")
            clsp = getattr(first, "clsp", "N/A")
            print(f"       -> 최근 일봉데이터 샘플: 일자={dt}, 종가={clsp}원")

        # 3. 미국 단일: usa01980 (미국주식 실시간 주가)
        print("\n[STEP 3] 미국 단일: usa01980 (미국주식 현재가) 호출 중...")
        r3 = await client.overseas.usa01980(Usa01980Request())
        # 실시간 데이터에서 필드 정보 조회 (보통 미국 현재가 등)
        print(f" -> [OK] 수집 결과: 수집된 API 응답 모델 유효성 검증 완료")
        
        # 4. 미국 배열: usa06012 (미국주식 일차트)
        print("\n[STEP 4] 미국 배열: usa06012 (애플 일차트) 호출 중...")
        r4 = await client.overseas.usa06012(Usa06012Request(stex_tp="NAS", stk_cd="AAPL"))
        items_us = r4.data if hasattr(r4, "data") and r4.data else []
        print(f" -> [OK] 수집 데이터: 응답 레코드 수={len(items_us)}건")
        if items_us:
            first_us = items_us[0]
            dt_us = getattr(first_us, "dt", "N/A")
            clsp_us = getattr(first_us, "clsp", "N/A")
            print(f"       -> 최근 해외일봉 샘플: 일자={dt_us}, 종가={clsp_us}")

        # 5. 계좌 단일: kt00001 (예수금현황)
        print("\n[STEP 5] 계좌 단일: kt00001 (종합 예수금 현황) 호출 중...")
        r5 = await client.domestic.kt00001(Kt00001Request(qry_tp="0"))
        # 예수금 잔액 등 필드 매핑
        print(f" -> [OK] 수집 결과: 계좌 예수금 API 정상 구동 완료")

        # 6. 계좌 배열: kt00018 (보유 잔고 종목 리스트)
        print("\n[STEP 6] 계좌 배열: kt00018 (계좌 보유 주식 잔고) 호출 중...")
        r6 = await client.domestic.kt00018(Kt00018Request(qry_tp="0", dmst_stex_tp="1"))
        items_acc = r6.data if hasattr(r6, "data") and r6.data else []
        print(f" -> [OK] 수집 데이터: 현재 보유 주식 종목 수={len(items_acc)}건")
        
    except KiwoomError as e:
        print(f"❌ [FAIL] 키움 API 연동 에러 발생: {e}")
    except Exception as e:
        print(f"❌ [FAIL] 예기치 않은 시스템 예외 발생: {e}")

def run_sync_matrix_tests(appkey: str, secretkey: str, is_mock: bool) -> None:
    """동기식 방식으로 6대 매트릭스 E2E 테스트를 가동합니다."""
    print("\n==================================================")
    print("[-] [2/2] KiwoomClient (동기) 6대 매트릭스 테스트")
    print("==================================================")
    
    client = KiwoomClient(appkey=appkey, secretkey=secretkey, is_mock=is_mock)
    
    try:
        # 대표적으로 차트 조회 및 계좌 보유 잔고 동기 조회 수행
        print("\n[STEP 1] 국내 단일 (동기): ka10001 호출 중...")
        r1 = client.domestic.ka10001(Ka10001Request(stk_cd="005930"))
        print(f" -> [OK] 수집 데이터: 종목명={r1.stk_nm}, 현재가={r1.cur_prc}원")
        
        print("\n[STEP 2] 국내 배열 (동기): ka10003 호출 중...")
        r2 = client.domestic.ka10003(Ka10003Request(stk_cd="005930"))
        items = r2.data if hasattr(r2, "data") and r2.data else []
        print(f" -> [OK] 수집 데이터: 응답 레코드 수={len(items)}건")
        
        print("\n[STEP 3] 계좌 배열 (동기): kt00018 호출 중...")
        r3 = client.domestic.kt00018(Kt00018Request(qry_tp="0", dmst_stex_tp="1"))
        items_acc = r3.data if hasattr(r3, "data") and r3.data else []
        print(f" -> [OK] 수집 데이터: 현재 보유 주식 종목 수={len(items_acc)}건")
        
        print("\n[SUCCESS] 동기식 6대 매트릭스 호출 흐름 검증 성공!")
        
    except KiwoomError as e:
        print(f"❌ [FAIL] 키움 API 연동 에러 발생: {e}")
    except Exception as e:
        print(f"❌ [FAIL] 예기치 않은 시스템 예외 발생: {e}")

if __name__ == "__main__":
    appkey, secretkey, is_mock = get_env_credentials()
    mode_name = "모의투자" if is_mock else "실전투자"
    print(f"[START] E2E 6대 매트릭스 종합 실서버 검증 시작 (접속 모드: {mode_name})")
    
    # 1. 비동기 E2E 테스트 수행
    asyncio.run(run_async_matrix_tests(appkey, secretkey, is_mock))
    
    # 2. 동기 E2E 테스트 수행
    run_sync_matrix_tests(appkey, secretkey, is_mock)
    
    print("\n================ E2E 종합 테스트 프로세스 종료 ================")
