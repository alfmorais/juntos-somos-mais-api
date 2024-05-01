# API de Consultores Juntos Somos Mais

Projeto de desenvolvimento de API para a vaga de Engenheiro de Software Pl. Juntos Somos Mais. A descrição do problema e os requisitos estão no [repositório](https://github.com/juntossomosmais/code-challenge).

## Index

- [Pré-requisitos](#Pré-requisitos)
- [Começando](#Começando)
- [Instalação](#Instalação)
- [Testes](#Testes)
- [API](#API)
- [Tecnologias](#Tecnologias)
- [Autor](#Autor)
- [Referências](#Referências)

## Pré-requisitos

- Docker (versão Docker 26.0.0, build 2ae903e)
- Docker Compose (versão Docker Compose v2.26.1-desktop.1)
- Poetry (versão 1.8.2) ou virtualenv 20.26.0

## Começando

Clone o repositório e entre na pasta do projeto:
```bash
git clone git@github.com:alfmorais/juntos-somos-mais-api.git
cd juntos-somos-mais-api/
```

## Instalação

Com o Poetry instalado, execute o seguinte comando:

```bash
poetry install && poetry shell
```

Esse comando é essencial para instalar as dependências do projeto e ativar o ambiente virtual criado pelo gerenciador de pacotes.

## Testes

Existem duas maneiras de executar os testes no projeto:

1) Localmente com o Poetry:

```bash
task test-local
```

2) Rodando os testes com o Docker:
```bash
task test
```

Ao final dos testes, uma tabela com as informações de cobertura dos testes é exibida:

```bash
---------- coverage: platform linux, python 3.11.7-final-0 -----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
src/__init__.py                          0      0   100%
src/api/__init__.py                      0      0   100%
src/api/app.py                          30      0   100%
src/api/cache.py                         2      0   100%
src/api/controllers/__init__.py          0      0   100%
src/api/controllers/consultants.py      15      0   100%
src/api/controllers/csv.py              23      0   100%
src/api/controllers/json.py             21      0   100%
src/api/exceptions/__init__.py           0      0   100%
src/api/exceptions/http.py               5      0   100%
src/api/integrations/__init__.py         0      0   100%
src/api/integrations/client.py          15      0   100%
src/api/schemas/__init__.py              0      0   100%
src/api/schemas/base.py                 88      0   100%
src/api/schemas/bounding_box.py         31      0   100%
src/api/schemas/consultants.py          41      0   100%
src/api/schemas/region.py               31      0   100%
src/api/views/__init__.py                0      0   100%
src/api/views/consultants.py            11      0   100%
--------------------------------------------------------
TOTAL                                  313      0   100%
```

## API

Para executar o projeto, temos duas opções:

1) Rodando a aplicação localmente:

```bash
task run
```

O primeiro endpoint `root` é um easteregg.

Para acessar a API e a documentação em OpenAPI, acesse: `http://127.0.0.1:8000/docs/`

Nesta tela, você encontrará todas as informações do endpoint GET para listar consultores.

2) Rodando a aplicação com o Docker:

```bash
task run-without-cache
```

ou

```bash
task run-with-cache
```

Após executar o projeto com o Docker, o terminal exibirá a seguinte saída:

```bash
[+] Running 0/3
 ⠙ Container juntos-somos-mais-api-api2-1   Recreated                                                                                                                       0.1s
 ⠙ Container juntos-somos-mais-api-api1-1   Recreated                                                                                                                       0.1s
 ⠋ Container juntos-somos-mais-api-nginx-1  Recreated                                                                                                                       0.1s
Attaching to api1-1, api2-1, nginx-1
nginx-1  | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
nginx-1  | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
nginx-1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
nginx-1  | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
nginx-1  | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
nginx-1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-

templates.sh
nginx-1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
nginx-1  | /docker-entrypoint.sh: Configuration complete; ready for start up
api2-1   | INFO:     Started server process [1]
api2-1   | INFO:     Waiting for application startup.
api1-1   | INFO:     Started server process [1]
api1-1   | INFO:     Waiting for application startup.
api2-1   | INFO:     Application startup complete.
api2-1   | INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
api1-1   | INFO:     Application startup complete.
api1-1   | INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

Com o Docker, temos um proxy reverso com duas instâncias da aplicação. Aprendizado do projeto da [Rinha Backend](https://github.com/alfmorais/RinhaBackend2024Q1).

Para acessar a API e a documentação em OpenAPI, acesse: `http://localhost:9999/docs`

## Tecnologias

Para esse projeto, optei por manter a simplicidade da aplicação. Vi que a Juntos Somos Mais utiliza o Django em alguns projetos open source. No entanto, não senti a necessidade de ter um Django com um ORM na aplicação. Por isso, decidi usar o FastAPI por ser simples, async e ter o OpenAPI incluído como padrão.

* [FastAPI](https://fastapi.tiangolo.com/) - O framework web utilizado
* [Poetry](https://python-poetry.org/) - Gerenciador de Dependências
* [Cache](https://cachetools.readthedocs.io/en/latest/) - Usada para armazenar os dados em memória

## Autor

Olá, eu sou Alfredo de Morais Neto. Sou desenvolvedor Python e quero fazer parte do time da Junto Somos Mais.

- [Linkedin](https://www.linkedin.com/in/alfredomneto/)
- [Github](https://github.com/alfmorais)
- [Email](alfredneto.1992@gmail.com)
- [Medium](https://medium.com/@alfredomorais)

## Referências
