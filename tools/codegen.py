import json
import re
from pathlib import Path
from typing import Any, Dict, List, Set


def to_camel_case(snake_str: str) -> str:
    """snake_case 또는 하이픈이 포함된 문자열을 PascalCase로 변환하되 원본 대소문자 구분을 유지합니다."""
    components = re.split(r"[-_]", snake_str)
    return "".join(x[0].upper() + x[1:] for x in components if x)


def to_python_field_name(field_name: str) -> str:
    """키움 API 필드명을 파이썬 식별자 규칙에 맞게 언더바로 치환하고 예약어 충돌을 피합니다."""
    if not field_name:
        return "empty_field"

    # 하이픈 및 공백을 언더바로 변경
    name = field_name.replace("-", "_").replace(" ", "_")

    # 숫자로 시작하는 경우 앞에 fid_ 붙이기 (예: '9001' -> 'fid_9001')
    if name[0].isdigit():
        name = f"fid_{name}"

    # 파이썬 예약어 목록
    reserved = {
        "class",
        "finally",
        "is",
        "return",
        "continue",
        "for",
        "lambda",
        "try",
        "def",
        "from",
        "nonlocal",
        "while",
        "del",
        "global",
        "not",
        "with",
        "elif",
        "if",
        "or",
        "yield",
        "else",
        "import",
        "pass",
        "except",
        "in",
        "raise",
        "true",
        "false",
        "none",
        "type",
        "id",
    }
    if name in reserved:
        return f"{name}_"
    return name


def get_api_names(api_id: str) -> tuple[str, str]:
    """
    api_id에 대응하는 파이썬 안전한 함수(메서드)명과 클래스명 프리픽스를 반환합니다.
    숫자로 시작하는 api_id(예: '00')에 접두사(tr_, Tr)를 붙집니다.
    """
    if not api_id:
        return "tr_unknown", "TrUnknown"

    if api_id[0].isdigit():
        return f"tr_{api_id}", f"Tr{to_camel_case(api_id)}"
    return api_id, to_camel_case(api_id)


def get_python_type(kiwoom_type: Any) -> str:
    """키움 스펙 타입을 파이썬 타입 힌트 문자열로 매핑합니다."""
    if not kiwoom_type:
        return "str"

    t_str = str(kiwoom_type).lower()
    if "number" in t_str or "integer" in t_str or "long" in t_str:
        return "int"
    elif "float" in t_str or "double" in t_str:
        return "float"
    elif "array" in t_str or "list" in t_str:
        return "List[Any]"
    else:
        return "str"


class Codegen:
    def __init__(self, spec_path: Path) -> None:
        self.spec_path = spec_path
        self.spec: Dict[str, Any] = {}

        # 카테고리별 데이터 수집 버퍼
        self.categories = {
            "auth": [],  # OAuth 인증
            "domestic": [],  # 주식
            "overseas": [],  # 미국주식
        }

        # 각 카테고리별 중첩 클래스 정의 버퍼 (재귀 생성용)
        self.nested_models_buffer: Dict[str, List[str]] = {
            "auth": [],
            "domestic": [],
            "overseas": [],
        }

    def load_spec(self) -> None:
        with open(self.spec_path, encoding="utf-8") as f:
            self.spec = json.load(f)

        for api_id, val in self.spec.items():
            cat_large = val.get("category_large", "")
            if cat_large == "OAuth 인증":
                self.categories["auth"].append(val)
            elif cat_large == "국내주식":
                self.categories["domestic"].append(val)
            elif cat_large == "미국주식":
                self.categories["overseas"].append(val)
            else:
                # 정의되지 않은 카테고리는 로그 출력 후 스킵
                print(f"Unknown category '{cat_large}' for API ID: {api_id}")

    def clean_description(self, desc: Any) -> str:
        if not desc:
            return ""
        # 개행문자 정리 및 따옴표 이스케이프
        s = str(desc).strip().replace("\n", " ").replace('"', '\\"')
        return s

    def build_pydantic_field(
        self,
        field_info: Dict[str, Any],
        parent_class_name: str,
        cat_key: str,
        seen_fields: Set[str],
    ) -> str:
        """단일 필드에 대한 Pydantic 필드 선언 코드를 빌드합니다 (중첩 구조 포함, 중복 필드 제외)."""
        field_raw = field_info.get("field", "")
        field_py = to_python_field_name(field_raw)

        # 이미 렌더링된 필드명인 경우 중복 정의 방지를 위해 건너뜀 (Mypy [no-redef] 오류 해결)
        if field_py in seen_fields:
            return ""
        seen_fields.add(field_py)

        name_kr = self.clean_description(field_info.get("name_kr", ""))
        desc = self.clean_description(field_info.get("description", ""))
        required = field_info.get("required", "N") == "Y"

        # 설명 조합
        full_desc = f"{name_kr} - {desc}" if desc else name_kr

        # 중첩 배열 자식(children)이 존재하는 경우 재귀 파싱
        children = field_info.get("children", [])
        if children:
            # 중첩 클래스명 생성
            child_class_name = f"{parent_class_name}{to_camel_case(field_raw)}"
            self.generate_nested_model(child_class_name, children, cat_key)

            # 타입 매핑
            field_type = f"List[{child_class_name}]"
        else:
            field_type = get_python_type(field_info.get("type"))

        # Alias 처리
        alias_str = f', alias="{field_raw}"' if field_raw != field_py else ""

        if required:
            return (
                f'    {field_py}: {field_type} = Field(..., description="{full_desc}"{alias_str})\n'
            )
        else:
            return f'    {field_py}: Optional[{field_type}] = Field(None, description="{full_desc}"{alias_str})\n'

    def generate_nested_model(
        self, class_name: str, fields: List[Dict[str, Any]], cat_key: str
    ) -> None:
        """중첩 배열 구조를 위한 별도의 Pydantic 서브클래스 코드를 생성합니다 (중복 제거 포함)."""
        field_lines = []
        seen_fields: Set[str] = set()
        for f in fields:
            line = self.build_pydantic_field(f, class_name, cat_key, seen_fields)
            if line:
                field_lines.append(line)

        fields_str = "".join(field_lines) if field_lines else "    pass\n"

        model_code = f"""
class {class_name}(KiwoomBaseModel):
    \"\"\"중첩 데이터 구조 모델\"\"\"
{fields_str}
"""
        self.nested_models_buffer[cat_key].append(model_code)

    def run(self) -> None:
        self.load_spec()

        for cat_key, apis in self.categories.items():
            models_code = [
                "# Auto-generated by tools/codegen.py. DO NOT EDIT.\n",
                "from typing import Any, List, Optional\n",
                "from pydantic import Field\n",
                "from kiwoom.models.base import KiwoomBaseModel\n\n",
            ]

            api_methods = []

            for api in apis:
                api_id_raw = api.get("api_id")
                name = api.get("name", "")
                method = api.get("method", "POST")
                url = api.get("url", "")

                # 안전한 함수명과 클래스 프리픽스 가져오기
                api_method_name, class_prefix = get_api_names(api_id_raw)

                # 1. Request Model 생성
                req_fields = api.get("request", {}).get("body", [])
                req_lines = []
                seen_req: Set[str] = set()
                for f in req_fields:
                    line = self.build_pydantic_field(f, f"{class_prefix}Request", cat_key, seen_req)
                    if line:
                        req_lines.append(line)

                req_fields_str = "".join(req_lines) if req_lines else "    pass\n"
                req_model = f"""
class {class_prefix}Request(KiwoomBaseModel):
    \"\"\"{name} ({api_id_raw}) 요청 모델\"\"\"
{req_fields_str}
"""
                models_code.append(req_model)

                # 2. Response Model 생성
                resp_fields = api.get("response", {}).get("body", [])
                resp_lines = []
                seen_resp: Set[str] = set()
                for f in resp_fields:
                    line = self.build_pydantic_field(
                        f, f"{class_prefix}Response", cat_key, seen_resp
                    )
                    if line:
                        resp_lines.append(line)

                resp_fields_str = "".join(resp_lines) if resp_lines else "    pass\n"
                resp_model = f"""
class {class_prefix}Response(KiwoomBaseModel):
    \"\"\"{name} ({api_id_raw}) 응답 모델\"\"\"
{resp_fields_str}
"""
                models_code.append(resp_model)

                # 3. API Method 생성
                api_methods.append(
                    f"""
    async def {api_method_name}(self, request: {class_prefix}Request, headers: Optional[dict] = None) -> {class_prefix}Response:
        \"\"\"
        {name} ({api_id_raw})

        URL: {url} ({method})
        \"\"\"
        response_json = await self._request(
            method="{method}",
            path="{url}",
            api_id="{api_id_raw}",
            headers=headers,
            json_data=request.model_dump(by_alias=True, exclude_none=True)
        )
        return {class_prefix}Response.model_validate(response_json)
"""
                )

            # 중첩 클래스 정의들을 최상위에 삽입 (정의가 선행되어야 메인 클래스에서 사용 가능하므로)
            if self.nested_models_buffer[cat_key]:
                # 임포트 선언 뒤에 삽입
                models_code = models_code[:4] + self.nested_models_buffer[cat_key] + models_code[4:]

            # Models 파일 쓰기
            models_file = Path(f"kiwoom/models/{cat_key}.py")
            with open(models_file, "w", encoding="utf-8") as f:
                f.write("".join(models_code))
            print(f"Created model file: {models_file}")

            # APIs 파일 쓰기
            api_class_name = f"{cat_key.title()}API"
            api_code = f"""# Auto-generated by tools/codegen.py. DO NOT EDIT.
from typing import Optional
from kiwoom.api.base import BaseAPI
from kiwoom.models.{cat_key} import (
"""
            # 모델 임포트 리스트
            import_names = []
            for api in apis:
                _, prefix = get_api_names(api.get("api_id"))
                import_names.append(f"    {prefix}Request,")
                import_names.append(f"    {prefix}Response,")
            api_code += "\n".join(import_names) + "\n)\n\n"

            api_code += f"""class {api_class_name}(BaseAPI):
    \"\"\"
    키움 {cat_key} API 관련 엔드포인트를 제공하는 클래스입니다.
    \"\"\"
"""
            api_code += "\n".join(api_methods)

            api_file = Path(f"kiwoom/api/{cat_key}.py")
            with open(api_file, "w", encoding="utf-8") as f:
                f.write(api_code)
            print(f"Created API wrapper file: {api_file}")


if __name__ == "__main__":
    codegen = Codegen(Path("data/kiwoom_api_spec.json"))
    codegen.run()
    print("API & Models Codegen Success!")
