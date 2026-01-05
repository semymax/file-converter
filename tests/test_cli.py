from click.testing import CliRunner
from app.cli import cli
import json

def cmd_cli_helper(input_path, output_path, input_format, output_format):
    runner = CliRunner()
    
    return runner.invoke(
        cli,[
            "convert",
            "--input", str(input_path),
            "--output", str(output_path),
            "--input-format", input_format,
            "--output-format", output_format
        ]
    )

def test_csv_to_json_success(tmp_path):
    # runner = CliRunner()
    
    input_file = tmp_path / "input.csv"
    input_file.write_text(
        "name,age\nAna,30\nJoão,25\n",
        encoding="utf-8"
    )
    
    output_file = tmp_path / "output.json"

    result = cmd_cli_helper(input_file, output_file, "csv", "json")
    # runner.invoke(
    #     cli, [
    #         "convert",
    #         "--input", str(input_file),
    #         "--output", str(output_file),
    #         "--input-format", "csv",
    #         "--output-format", "json"
    #     ]
    # )
    
    assert result.exit_code == 0
    assert output_file.exists()
    
    data = json.loads(output_file.read_text(encoding="utf-8"))
    assert data[0]["name"] == "Ana"
    assert data[1]["age"] == "25"

def test_cli_unsupported_input_format():
    # runner = CliRunner()
    
    result = cmd_cli_helper("input.txt", "output.csv", "txt", "csv")
    # runner.invoke(
    #     cli, [
    #         "convert",
    #         "--input", "input.txt",
    #         "--output", "output.csv",
    #         "--input-format", "txt",
    #         "--output-format", "csv",
    #     ]
    # )
    
    assert result.exit_code != 0
    assert "unsupported" in result.output.lower()
    
def test_cli_missing_required_argument():
    runner = CliRunner()
    
    result = runner.invoke(
        cli, [
            "convert",
            "--input", "input.csv",
            "--input-format", "csv",
            "--output-format", "json",
        ]
    )
    
    assert result.exit_code != 0
    assert "missing option" in result.output.lower()
