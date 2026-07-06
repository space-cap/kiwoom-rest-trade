import csv
import re
from pathlib import Path

def to_camel_case(snake_str: str) -> str:
    components = re.split(r'[-_]', snake_str)
    return "".join(x[0].upper() + x[1:] for x in components if x)

def get_api_names(api_id: str) -> tuple[str, str]:
    if not api_id:
        return "tr_unknown", "TrUnknown"
    if api_id[0].isdigit():
        return f"tr_{api_id}", f"Tr{to_camel_case(api_id)}"
    return api_id, to_camel_case(api_id)

def generate():
    csv_path = Path("data/kiwoom_api_index.csv")
    md_path = Path("docs/API_LIST.md")
    
    # 디렉토리 생성 보장
    md_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# 키움증권 REST API 매핑 및 지원 목록 (API_LIST.md)\n",
        "본 문서는 `kiwoom-rest-trade` SDK가 지원하는 전체 **337개 API**와 파이썬 메서드 간의 1대1 매핑 인덱스 가이드입니다.\n",
        "| 대분류 | 중분류 | 키움 API ID | 파이썬 호출 메서드 | API 기능명 | HTTP 요청 |",
        "|---|---|---|---|---|---|"
    ]
    
    with open(csv_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            api_id = row.get("\ufeffapi_id") or row.get("api_id")
            name = row.get("name", "").strip()
            cat_large = row.get("category_large", "").strip()
            cat_medium = row.get("category_medium", "").strip() or "-"
            method = row.get("method", "").strip()
            url = row.get("url", "").strip()
            
            # 메서드명 맵핑 규칙 적용
            api_method_name, _ = get_api_names(api_id)
            
            # 클라이언트 그룹 분류
            if cat_large == "OAuth 인증":
                client_path = f"client.auth.{api_method_name}"
            elif cat_large == "국내주식":
                client_path = f"client.domestic.{api_method_name}"
            elif cat_large == "미국주식":
                client_path = f"client.overseas.{api_method_name}"
            else:
                client_path = f"client.domestic.{api_method_name}"
                
            line = f"| {cat_large} | {cat_medium} | `{api_id}` | `{client_path}` | {name} | `{method} {url}` |"
            lines.append(line)
            
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Successfully generated API list document: {md_path}")

if __name__ == "__main__":
    generate()
