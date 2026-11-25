# PyDefender Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-green)

## 🇺🇸 English

A lightweight Python toolkit for local defensive security operations: integrity verification, log severity reporting and file inventory. It is designed for reproducible learning and routine review using authorized local data. No external dependencies or network features.

## 🇧🇷 Português

Conjunto de utilitários defensivos para verificar integridade de arquivos, consolidar registros em formato JSON Lines e inventariar arquivos locais. A interface de linha de comando facilita tarefas recorrentes e o uso de exemplos sintéticos.

## Features / Funcionalidades

| Comando | Entrada | Saída |
|---|---|---|
| hash | Arquivo local | SHA-256 hexadecimal |
| verify | Arquivo e referência confiável | MATCH ou MISMATCH |
| log-summary | Arquivo JSONL | Contagens por nível e linhas inválidas |
| inventory | Diretório | Nome, tamanho e data UTC dos arquivos imediatos |

## Getting started

```bash
git clone https://github.com/sousaa-dev/pydefender-toolkit.git
cd pydefender-toolkit
python pydefender.py --help
python pydefender.py hash examples/events.jsonl
python pydefender.py log-summary examples/events.jsonl
python pydefender.py inventory examples
python -m unittest discover -s tests
```

Python 3.10 ou superior. Não é necessário instalar bibliotecas externas.

## Behavior and architecture

- `pydefender.py`: CLI, funções de processamento e tratamento de erros.
- `examples/`: registros sintéticos para demonstração.
- `tests/`: testes unitários de hash, resumo de logs e inventário.
- `docs/`: guias e limites operacionais.

O código de saída 0 indica sucesso, 1 indica divergência de integridade, 2 indica entrada inválida ou falha de leitura. O resultado é exibido na saída padrão. O inventário não percorre subdiretórios nem segue links simbólicos. O resumo de registros conta níveis declarados, sem inferir incidentes.

## Documentation

- [Usage guide](docs/usage.md)
- [Practical scenarios](docs/scenarios.md)

## Roadmap

Comparação de inventários, relatórios CSV e ampliação dos testes.

## Project history / Histórico do projeto

Previously maintained in another personal account, the project was revised and migrated to consolidate my professional portfolio.

Anteriormente mantido em outra conta pessoal, o projeto foi revisado e migrado para consolidar meu portfólio profissional.

**Autor:** Pablo Sousa Ribeiro — [sousaa-dev](https://github.com/sousaa-dev).
