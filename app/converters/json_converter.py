import json
from typing import List, Dict

def json_to_dicts(file_path: str) -> List[Dict]:
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON deve ser uma lista de objetos")
    
    return data
    
def dicts_to_json(data: List[Dict], file_path: str) -> None:
    if not isinstance(data, list):
        raise ValueError("Dados devem ser um lista de dicionários")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
