English | [Português](README.pt-BR.md)

# File Converter Service

A backend-oriented Python project for converting files between CSV, JSON, and XML formats,
designed with a clean service-based architecture and strong test coverage.

## Features

### Implemented

- CSV ↔ JSON ↔ XML conversion
- Service-oriented architecture
- Custom domain-specific exceptions
- Integration and parametrized tests using pytest
- Command Line Interface (CLI)

### Planned

- REST API using FastAPI

## Project Structure

```markdown
├── app/
│  ├── converters/
│  ├── services/
│  ├── exceptions/
|  └── cli/
└── tests/
```

This structure separarates domain logic, services, and interfaces, making this project easy to extend with APIs or new interfaces.

## Command Line Interface (CLI)

This project provides a Command Line Interface for converting files directly from the terminal.

### Usage

```bash

python -m app.cli convert \
    --input input.csv \
    --output output.json \
    --input-format csv \
    --output-format json
```

### Arguments

- `--input`: Path to the input file
- `--output`: Path to the output file
- `--input-format`: Input file format (csv, json, xml)
- `--output-format`: Output file format (csv, json, xml)

### Example

```bash
python -m app.cli convert \
    --input data/users.csv \
    --output data/users.json \
    --input-format csv \
    --output-format json
```

⚠️ The CLI is under active development and may evolve as new features are added.
