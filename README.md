# Django Weight Recorde

Aplicação desenvolvida para finalidades de estudo sobre a framework Django e sobre gerenciamento de dependências com Poetry.

A aplicação em questão serve para registar pesagens de uma pessoa e exigir um gráfico com o histórico dos cadastros realizados.

![UML](uml/uml/Django Weight Recorde.png?raw=true)

## Bibliotecas utilizadas

- Djnago
- Django-Widget-Tweaks

## Requisitos

- Python 3.6 ou superior
- Poetry

## Como começar

Clone este repositório e ente na pasta do projeto

```sh
git clone https://github.com/CleysonPH/django-weight-recorde.git
cd django-weight-recorde
```

Instale os requisitos do projeto com o Poetry

```sh
poetry install
```

## Como rodar esse projeto

Inicie o ambiente virtual

```sh
poetry shell
```

Em seguida rode as migrações para a criação do banco de dados

```sh
python manage.py migrate
```

E por ultimo basta executar o servidor de desenvolvimento do Django

```sh
python manage.py runserver
```

E então acessar a aplicação em http://localhost:8000/dashboard/
