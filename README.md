# Backend - Desafio CodeLeap

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST-A30000?style=for-the-badge&logo=django&logoColor=white)

## Descrição

API RESTful desenvolvida com Django e Django REST Framework como solução para o desafio de backend proposto no processo seletivo da CodeLeap. A aplicação implementa um CRUD (Create, Read, Update, Delete) básico de posts.

## Funcionalidades

* Listagem de todos os posts.
* Criação de um novo post.
* Atualização parcial de um post existente (título e conteúdo).
* Exclusão de um post.

## Pré-requisitos

* Python 3.8+
* Pip

## Instalação e Execução

Siga os passos abaixo para executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/josiasdev/codeleap-backend
    cd codeleap-backend
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar ambiente
    python -m venv venv

    # Ativar no Windows
    # venv\Scripts\activate

    # Ativar no Linux/macOS
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Documentação da API

A seguir estão os endpoints disponíveis na aplicação.

**URL Base:** `http://127.0.0.1:8000/`

| Método | Endpoint           | Descrição                                 | Corpo (Payload) Exemplo                                               |
| :----- | :----------------- | :---------------------------------------- | :-------------------------------------------------------------------- |
| `GET`    | `/careers/`        | Retorna uma lista com todos os posts.     | N/A                                                                   |
| `POST`   | `/careers/`        | Cria um novo post.                        | `{"username": "string", "title": "string", "content": "string"}`      |
| `PATCH`  | `/careers/{id}/`   | Atualiza o título e/ou conteúdo de um post existente. | `{"title": "string", "content": "string"}` (ambos são opcionais) |
| `DELETE` | `/careers/{id}/`   | Deleta um post específico.                | N/A                                                                   |

### Exemplo de Retorno (GET /careers/)

```json
[
    {
        "id": 1,
        "username": "John Doe",
        "created_datetime": "2025-10-03T01:30:00Z",
        "title": "Primeiro Post",
        "content": "Conteúdo do primeiro post."
    },
    {
        "id": 2,
        "username": "Jane Doe",
        "created_datetime": "2025-10-03T01:35:00Z",
        "title": "Outro Post",
        "content": "Mais um conteúdo interessante."
    }
]
```