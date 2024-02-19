Claro, aqui está o Readme.md atualizado com todas as informações de comandos incluídas:

---

# Projeto de Criação de Tag com Código de Barras em PNG

Este repositório contém todo o código e recursos necessários para o projeto de criação de uma tag com código de barras em formato PNG, desenvolvido como parte da Next Level Week (NLW). O projeto utiliza validação com Pytest, estrutura de código do Pylint, e é executado em um ambiente virtual.

## Bibliotecas Instaladas

As seguintes bibliotecas foram instaladas para o desenvolvimento do projeto:

- Flask: Para o desenvolvimento de aplicativos web em Python.
- Cerberus: Para validação de dados.
- Pillow: Para manipulação de imagens.
- Python-barcode: Para geração de códigos de barras.
- Pylint: Para análise de código e garantia de qualidade.
- Pre-commit: Para execução de tarefas automáticas antes do commit.
- Virtualenv: Para criação de ambientes virtuais.

## Ferramentas Utilizadas

- **Postman**: Instalado para simular a execução do programa, realizando requisições POST.

## Comandos Utilizados no Git Bash

```bash
source .venv/Scripts/activate
git status
git add .
git commit -m 'feat: Descrição do commit'
python run.py
pip3 freeze > requirements.txt
pre-commit install
```

## Comandos Utilizados no Terminal do VSCode (PowerShell)

```powershell
.venv\Scripts\activate
# Caso necessário:
# Set-ExecutionPolicy Unrestricted -Force
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
python run.py
.venv\Scripts\pip3 freeze > requirements.txt
pytest
pytest -s -v
```

---

Esse texto fornecerá uma visão geral do seu projeto, incluindo informações sobre as bibliotecas instaladas e os comandos necessários para configurar e executar o projeto.
