import pytest
import json
from app.services import convert
from app.exceptions import UnsupportedFormatError, InvalidPathError

def test_input_format_not_supported():
    with pytest.raises(UnsupportedFormatError):
        convert(
            input_path="input.csv",
            output_path="output.json",
            input_format="txt",
            output_format="json",
        )
        
def test_output_format_not_supported():
    with pytest.raises(UnsupportedFormatError):
        convert(
            input_path="input.csv",
            output_path="output.json",
            input_format="csv",
            output_format="exe",
        )
        
def test_input_path_not_valid():
    with pytest.raises(InvalidPathError):
        convert(
            input_path="",
            output_path="output.json",
            input_format="csv",
            output_format="json",
        )
        
def test_output_path_not_valid():
    with pytest.raises(InvalidPathError):
        convert(
            input_path="input.csv",
            output_path="",
            input_format="csv",
            output_format="json",
        )

def test_csv_to_json_success(tmp_path):
    csv_file = tmp_path / "input.csv"

    csv_file.write_text(
        "name,age\nAna,30\nJoão,25\n",
        encoding="utf-8"
    )
    
    json_file = tmp_path / "output.json"
    
    convert(
        input_path=str(csv_file),
        output_path=str(json_file),
        input_format="csv",
        output_format="json",
    )

    assert json_file.exists()
    
    data = json.loads(json_file.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert data[0]["name"] == "Ana"
    assert data[1]["age"] == "25"
    
@pytest.mark.parametrize(
    "input_format, output_format, output_filename",
    [
        ("csv", "json", "output.json"),
        ("csv", "xml", "output.xml")
    ]
)
def test_csv_conversions(
    tmp_path, input_format, output_format, output_filename
):
    input_file = tmp_path / "input.csv"
    input_file.write_text(
        "name,age\nAna,30\nJoão,25\n",
        encoding="utf-8"
    )
    
    output_file = tmp_path / output_filename
    
    convert(
        input_path=str(input_file),
        output_path=str(output_file),
        input_format=input_format,
        output_format=output_format,
    )
    
    assert output_file.exists()
    
    if output_format == "json":
        data = json.loads(output_file.read_text(encoding="utf-8"))
        assert isinstance(data, list)
        assert data[0]["name"] == "Ana"
        assert data[1]["age"] == "25"
        
    if output_format == "xml":
        text = output_file.read_text(encoding="utf-8")
        assert "<item>" in text
        assert "<name>Ana</name>" in text
