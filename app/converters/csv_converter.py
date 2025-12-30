import csv
from typing import List, Dict

def csv_to_dicts(file_path: str) -> List[Dict]:
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def dicts_to_csv(data: List[Dict], file_path: str) -> None:
    if not data:
        raise ValueError("Dados Vazios")
    
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
