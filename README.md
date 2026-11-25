# PyDefender Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Dependencies](https://img.shields.io/badge/dependencies-standard%20library-blue)

## 🇺🇸 English

Lightweight local defensive utilities for file integrity, log reporting and inventory. No network connections or third-party dependencies.

## 🇧🇷 Português

Ferramentas defensivas em Python para verificação de integridade, análise de registros e inventário local.

### Project history / Histórico do projeto

Previously maintained in another personal account, this project has been revisited and updated for inclusion in my professional portfolio. Its migration to this repository consolidates my studies and practical development work in a dedicated professional profile.

Anteriormente mantido em outra conta pessoal, este projeto foi revisado e atualizado para integrar meu portfólio profissional. Sua migração para este repositório consolida meus estudos e atividades práticas de desenvolvimento em um perfil dedicado à minha trajetória profissional.


## Commands / Comandos

| Command | Purpose |
|---|---|
| hash | Calculate SHA-256 |
| verify | Compare against a trusted SHA-256 |
| log-summary | Count severity labels in JSONL |
| inventory | List immediate regular files |

```bash
python pydefender.py hash examples/events.jsonl
python pydefender.py log-summary examples/events.jsonl
python pydefender.py inventory examples
python -m unittest discover -s tests
```

Python 3.10+. Verification returns 1 for mismatch; invalid input returns 2.

See [usage guide](docs/usage.md). Author: Pablo Sousa Ribeiro — [sousaa-dev](https://github.com/sousaa-dev).
