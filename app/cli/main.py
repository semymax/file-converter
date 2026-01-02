import cli
from app.services import convert
from app.exceptions import ConverterError

@click.group()
def cli():
    """ File Converter CLI """
    pass

@click.option("--input", "input_path", required=True, help="Input file path")
@click.option("--output", "output_path", required=True, help="Output file path")
@click.option("--from", "input_format", required=True, help="Input format (CSV, JSON, XML)")
@click.option("--to", "output_format", required=True, help="Output format (CSV, JSON, XML)")

def convert_cmd(input_path, output_path, input_format, output_format):
    """ Convert files between formats """
    try:
        convert(
            input_path=input_path,
            output_path=output_path,
            input_format=input_format,
            output_format=output_format
        )
        click.echo("✅ Conversion completed successfully")
    except ConverterError as exc:
        click.echo(f"❌ Error: {exc}", err=True)
