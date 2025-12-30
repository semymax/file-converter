from app.converters.csv_converter import csv_to_dicts, dicts_to_csv
from app.converters.json_converter import json_to_dicts, dicts_to_json
from app.converters.xml_converter import xml_to_dicts, dicts_to_xml
from app.exceptions import InvalidPathError, UnsupportedFormatError

loaders = {
    "csv": csv_to_dicts,
    "json": json_to_dicts,
    "xml": xml_to_dicts,
}

dumpers = {
    "csv": dicts_to_csv,
    "json": dicts_to_json,
    "xml": dicts_to_xml,
}

def convert(
    input_path: str,
    output_path: str,
    input_format: str,
    output_format: str,
) -> None:
    if not input_path or not output_path:
        raise InvalidPathError("Caminho de arquivo inválido")

    input_format = input_format.lower()
    output_format = output_format.lower()
    
    if input_format not in loaders:
        raise UnsupportedFormatError("Formato de entrada não suportado")
    
    if output_format not in dumpers:
        raise UnsupportedFormatError("Formato de saída não suportado")
    
    data = loaders[input_format](input_path)
    dumpers[output_format](data, output_path)
