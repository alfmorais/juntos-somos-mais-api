# Documentação dos Comandos

Taskipy é uma ferramenta que permite definir e executar tarefas repetitivas em projetos Python. Para esse projeto, estamos usando com o objetivo de simplificar os comandos para build, testar e rodar o projeto.

1. [shell](#shell)
2. [remove-pycache](#remove-pycache)
3. [remove-pytest-cache](#remove-pytest-cache)
4. [generate-requirements](#generate-requirements)
5. [install](#install)
6. [test-local](#test-local)
7. [run](#run)
8. [run-without-cache](#run-without-cache)
9. [run-with-cache](#run-with-cache)
10. [test](#test)
11. [build-no-cache](#build-no-cache)
12. [test-pipeline](#test-pipeline)
13. [heroku](#heroku)

## shell
- **Objetivo**: Acessar o shell interativo do Python.
- **Comando**: ``` export PYTHONDONTWRITEBYTECODE=1 && ipython```
- **Atalho**: `task shell`

## remove-pycache
- **Objetivo**: Remover arquivos `__pycache__` e arquivos `.pyc`.
- **Comando**: ```find . -type d -name '__pycache__' -exec rm -r {} + && find . -type f -name '*.pyc' -exec rm {} +```
- **Atalho**: `task remove-pycache`

## remove-pytest-cache
- **Objetivo**: Remover o diretório `.pytest_cache`.
- **Comando**: ```rm -rf .pytest_cache```
- **Atalho**: `task remove-pytest-cache`

## generate-requirements
- **Objetivo**: Gerar o arquivo `requirements.txt` a partir do Poetry.
- **Comando**: ```export PYTHONDONTWRITEBYTECODE=1 && poetry export --format=requirements.txt > requirements.txt```
- **Atalho**: `task generate-requirements`

## install
- **Objetivo**: Instalar pacotes com pip a partir do `requirements.txt`.
- **Comando**: ```export PYTHONDONTWRITEBYTECODE=1 &&  pip install -r requirements.txt```
- **Atalho**: `task install`

## test-local
- **Objetivo**: Executar todos os testes unitários.
- **Comando**: ```export PYTHONDONTWRITEBYTECODE=1 && pytest -vvv --disable-warnings --cov src```
- **Atalho**: `task test-local`

## run
- **Objetivo**: Executar o projeto sem usar Docker.
- **Comando**: ```uvicorn src.api.app:app --reload```
- **Atalho**: `task run`

## run-without-cache
- **Objetivo**: Construir e executar o projeto sem usar o cache.
- **Comando**: ```docker-compose build --no-cache && docker-compose up```
- **Atalho**: `task run-without-cache`

## run-with-cache
- **Objetivo**: Construir e executar o projeto com Docker.
- **Comando**: ```docker-compose up --build```
- **Atalho**: `task run-with-cache`

## test
- **Objetivo**: Executar os testes dentro do Docker.
- **Comando**: ```docker-compose run api1 pytest -vvv --disable-warnings --cov src```
- **Atalho**: `task test`

## build-no-cache
- **Objetivo**: Buildar e rodar o projeto sem usar cache.
- **Comando**: ```docker-compose --project-name juntos-somos-mais build --no-cache```
- **Atalho**: `task build-no-cache`

## test-pipeline
- **Objetivo**: Executar os testes no pipeline do Docker.
- **Comando**: ```docker-compose -p juntos-somos-mais-api run api1 pytest -vvv --disable-warnings --cov src```
- **Atalho**: `task test-pipeline`

## heroku
- **Objetivo**: Instalar o Heroku CLI para uso no Github Actions.
- **Comando**: ```curl https://cli-assets.heroku.com/install-ubuntu.sh | sh```
- **Atalho**: `task heroku`
