from pydantic import BaseModel, ConfigDict


class KiwoomBaseModel(BaseModel):
    """
    kiwoom-rest-trade 패키지 내의 모든 Pydantic 데이터 모델이 상속받는 공통 베이스 클래스입니다.
    """

    model_config = ConfigDict(
        # 필드 대입 시 별칭(Alias)이나 실제 필드명 모두 허용
        populate_by_name=True,
        # 알 수 없는 임의의 타입 허용 (디버그 및 확장성 대비)
        arbitrary_types_allowed=True,
        # 입력 문자열 양 끝의 공백(Whitespace) 자동 트리밍
        str_strip_whitespace=True,
    )
