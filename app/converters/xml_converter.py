import xml.etree.ElementTree as ET
from typing import List, Dict

def xml_to_dicts(file_path: str) -> list[Dict]:
    tree = ET.parse(file_path)
    root = tree.getroot()
    items = root.findall("item")
    
    if not items:
        raise ValueError("XML não contém elementos <item>")
    
    data = []
    
    for item in items:
        record = {}
        for child in item:
            record[child.tag] = child.text
            
        data.append(record)

    return data

def dicts_to_xml(data: List[Dict], file_path:str) -> None:
    if not isinstance(data, list) or not data:
        raise ValueError("Dados devem ser uma lista de dicionários")

    root = ET.Element("items")

    for record in data:
        if not isinstance(record, dict):
            raise ValueError("Cada item deve ser um dicionário")
            
        item_el = ET.SubElement(root, "item")
        
        for key, value in record.items():
            child = ET.SubElement(item_el, key)
            child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
