# Backend - Desafio CodeLeap

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST-A30000?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)


## Descrição

API RESTful desenvolvida com Django e Django REST Framework como solução para o desafio de backend proposto no processo seletivo da CodeLeap. A aplicação implementa um CRUD (Create, Read, Update, Delete) básico de posts e está implantada na plataforma Render.

## API Online

A API está implantada e pode ser acessada através da seguinte URL base:

**`https://codeleap-backend-uyrt.onrender.com`**


## Endpoints da Documentação

* **Swagger UI:** [`/swagger-ui/`](https://codeleap-backend-uyrt.onrender.com/swagger-ui/)
* **ReDoc:** [`/redoc/`](hhttps://codeleap-backend-uyrt.onrender.com/redoc/)


## Funcionalidades

* Documentação interativa da API com Swagger UI e ReDoc.
* Endpoints CRUD completos para gerenciamento de posts.
* Deploy automatizado através do Render.


## Execução Local (Desenvolvimento)

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

### Exemplos de Respostas da API
Abaixo estão exemplos do que a API retorna para cada tipo de requisição bem-sucedida.

## GET /careers/

Retorna um array de objetos, contendo todos os posts no banco de dados.

Status: 200 OK

```json
[
    {
        "id": 1,
        "username": "Josias",
        "created_datetime": "2025-10-03T01:30:00Z",
        "title": "Desenvolvedor BackEnd Django",
        "content": "Sobre desenvolvimento backend com django."
    },
    {
        "id": 2,
        "username": "João",
        "created_datetime": "2025-10-03T01:35:00Z",
        "title": "Desenvolvedor FrontEnd",
        "content": "Sobre desenvolvimento frontend com React."
    }
]
```

## POST /careers/

Após a criação de um novo post, a API retorna o objeto completo que foi criado, incluindo o id e a data de criação (created_datetime) gerados pelo servidor.

Status: 201 Created

```json
{
    "id": 3,
    "username": "Maria",
    "created_datetime": "2025-10-02T22:14:00.987654Z",
    "title": "Receita de bolo de chocolate:",
    "content": "Maria gosta de receitas de bolo de chocolate."
}
```

## PATCH /careers/{id}/

Após a atualização bem-sucedida de um post (por exemplo, o post com id: 1), a API retorna o objeto completo com os dados modificados.

Status: 200 OK

```json
{
    "id": 1,
    "username": "Josias",
    "created_datetime": "2025-10-02T22:10:00.123456Z",
    "title": "Desenvolvedor Web3",
    "content": "Desenvolvimento Web3 cresce no Brasil."
}
```

## DELETE /careers/{id}/

Se o item for deletado com sucesso, a API retornará uma resposta sem conteúdo no corpo.

Status: 204 No Content

```json
[]
```