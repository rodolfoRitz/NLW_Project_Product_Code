Este repositório contempla todo o projeto para a criação de uma tag com o código de barras em '.png', pela plataforma NLW.
Utilizando validação em 'Pytest', a estrutura de código do 'Pylint', tudo dentro de um ambiente virtual.

Foram instaladas as bibliotecas: 
Flask, cerberus, pillow, python-barcode, pylint, pre-commit, virtualenv.

O programa 'Postman' foi instalado para simular a execução do programa, realizando a requisição POST.

Comandos utilizados no terminal do 'Git Bash':
source .venv/Scripts/activate
git status
git add.
git commit -m 'feat: Descrição do commit'
python run.py
pip3 freeze > requirements.txt
pre-commit install

Comandos utilizados no terminal do VScode(powershell):
.venv\Scripts\activate
Caso necessário: ( Set-ExecutionPolicy Unrestricted -Force, Set-ExecutionPolicy  -Scope CurrentUser  -ExecutionPolicy RemoteSigned )
python run.py
.venv\Scripts\pip3 freeze > requirements.txt
pytest
pytest -s -v
