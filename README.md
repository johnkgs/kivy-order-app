# Projeto para a disciplina de Programação Distribuida e Paralela relacionado a filas e serviços web

## Requerimentos

-   [Poetry](https://python-poetry.org/) >= 1.1.12
-   [Python](https://www.python.org/) >= 3.9

<br />

## Poetry via PIP

Instalação

```bash
pip install poetry
```

Verificar a versão do poetry

```bash
poetry --version
```

<br />

## Como executar o projeto

Renomear o arquivo [`.env.example`](./.env.example) para `.env`:

Instalar dependências:

```bash
poetry install
```

Executar em ambiente de desenvolvimento:

```bash
poetry run start
```

Executar formatador de código:

```bash
poetry run black order_app/
```

Executar ordenação de importações:

```bash
poetry run isort order_app/
```
