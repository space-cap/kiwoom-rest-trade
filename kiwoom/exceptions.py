class KiwoomError(Exception):
    """kiwoom-rest-trade 패키지의 모든 예외의 부모가 되는 최상위 예외 클래스입니다."""

    pass


class KiwoomAuthError(KiwoomError):
    """인증 실패, 토큰 만료, 잘못된 App Key/Secret Key 등으로 인한 오류 예외 클래스입니다."""

    pass


class KiwoomRateLimitError(KiwoomError):
    """키움 서버의 초당 호출 제한(Rate Limit)을 초과했을 때 발생하는 예외 클래스입니다."""

    pass


class KiwoomValidationError(KiwoomError):
    """API 요청 필드 유효성 검사 실패 또는 잘못된 입력값 관련 오류 예외 클래스입니다."""

    pass


class KiwoomAPIError(KiwoomError):
    """
    키움 API 서버가 비즈니스 로직 상의 에러를 반환했을 때 발생하는 예외 클래스입니다.
    """

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")
