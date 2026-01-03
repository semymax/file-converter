[English](README.md) | Português

# Serviço de Conversão de Arquivos

Projeto em Python com foco em backend para conversão de arquivos entre os formatos
CSV, JSON e XML, utilizando uma arquitetura em camadas e testes automatizados.

## Funcionalidades

### Implementadas

- Conversão CSV ↔ JSON ↔ XML
- Arquitetura orientada a serviços
- Exceções de domínio customizadas
- Testes de integração e parametrizados com pytest
- Interface de Linha de Comando (CLI)

### Planejadas

- API REST com FastAPI

## Estrutura do projeto

```markdown
├── app/
│  ├── converters/
│  ├── services/
│  ├── exceptions/
|  └── cli/
└── tests/
```

Esta estrutura separa domínio lógico, serviços e interfaces, fazendo com que este projeto seja de fácil extensão com APIs ou novas interfaces.

## Interface de Linha de Comando

Este projeto oferece uma Interface de Linha de Comando (Command Line Interface - CLI) para conversão de arquivos direto pelo terminal.

### Uso

```bash
python -m app.cli convert \
    --input input.csv \
    --output output.json \
    --input-format csv \
    --output-format json
```

### Argumentos

- `--input`: Caminho para o arquivo de entrada
- `--output`: Caminho para o arquivo de saída
- `--input-format`: Formato do arquivo de entrada (csv, json, xml)
- `--output-format`: Formato do arquivo de saída (csv, json, xml)

### Exemplo

```bash
python -m app.cli convert \
    --input dados/usuarios.csv \
    --output dados/usuarios.json \
    --input-format csv \
    --output-format json
```

⚠️ Esta interface cli está sob desenvolvimento ativo e poderá evoluir conforme novos recursos sejam adicionados.
