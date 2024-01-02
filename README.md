# API REST - Teste Bluestorm

API REST solicitada no processo seletivo da Bluestorm, para a vaga de desenvolvedor Python. Sua funcionalidade consiste na consulta de três tabelas em um banco de dados, todos relacionados a farmácia, paciente e transações entre ambos e com necessidade de autenticação para tal. Teste realizado por: Paulo S. Garcia.

## Índice

- [Requisitos de Instalação](#requisitos-de-instalação)
- [Instalação](#instalação)
- [Executando Localmente](#executando-localmente)
- [Endpoints e Exemplos de Requisição](#endpoints-e-exemplos-de-requisição)
- [Documentação da API](#documentação-da-api)
- [IMPORTANTE: observações](#importante-observações)

## Requisitos de Instalação

Principais requisitos necessários para a execução da API. Ao serem instaladas pelo command line, as subdependências trazidas por estas, serão instaladas automaticamente.

- Python 3.10+
- Flask
- Flask-JWT-Extended
- flask-restx
- Flask-SQLAlchemy
- python-dotenv

## Instalação

Para a instalação das dependências e das subdependências, basta digitar a seguinte command line com o terminal aberto na raiz do projeto e possuindo Python instalado e devidamente referenciado no PATH das variáveis de ambiente.

```bash
pip install -r requirements.txt
```

## Executando Localmente

Para a execução local, após a instalação das dependências, utilize, pelo terminal o comando flask_run na raiz do projeto.

```bash
flask run
```

## Autenticação e Uso

Para utilizar a maioria das rotas da API, por exceção das envolvidas na resource de Pharmacy, é necessária autenticação com login, senha e Bearer token. Para isso, basta seguir os seguintes passos:

- Crie um usuário com a rota register.
- Faça o login no usuário com a rota login.
- Clique no cadeado indicado em qualquer uma das rotas que peça autenticação.
- Digite Bearer <seu_jwt_token> e faça o login.

A partir disso, você poderá utilizar quaisquer rotas, até que faça logout ou feche o aplicativo.

## Endpoints e Exemplos de Requisição

### Patients

#### List all patients

- **URL:** `/patients`
- **Descrição:** Retorna informações sobre todos os pacientes.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
  ```json
  {
    "method": "GET",
    "url": "http://localhost:5000/api/patients",
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer <seu_token_jwt>"
    }
  }
  ```

#### Get a patient by id

- **URL:** `/patients/patient/id:<string:uuid>`
- **Descrição:** Retorna informações sobre um paciente com base no ID.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
        "method": "GET",
        "url": "http://localhost:5000/patients/patient/id:PATIENT0001",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <seu_token_jwt>"
        }
    }
    ```

#### Get patients by first name

- **URL:** `/patients/patient/first_name:<string:fName>`
- **Descrição:** Retorna informações sobre pacientes com base no primeiro nome.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
        "method": "GET",
        "url": "http://localhost:5000/patients/patient/first_name:PAULO",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <seu_token_jwt>"
        }
    }
    ```


#### Get patients by full name

- **URL:** `/patients/patient/full_name:<string:fName>&<string:lName>`
- **Descrição:** Retorna informações sobre pacientes com base no nome completo.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ``` json
    {
        "method": "GET",
        "url": "http://localhost:5000/patients/patient/full_name:PAULO&GARCIA",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <seu_token_jwt>"
        }
    }
    ```

### Pharmacies

#### List all pharmacies

- **URL:** `/pharmacies`
- **Descrição:** Retorna informações sobre todas as farmácias.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ``` json
    {
        "method": "GET",
        "url": "http://localhost:5000/pharmacies",
        "headers": {
            "Content-Type": "application/json"
        }
    }
    ```
 

### Get a pharmacy by id

- **URL:** `/pharmacies/pharmacy/id:<string:uuid>`
- **Descrição:** Retorna informações sobre uma farmácia com base no ID.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/pharmacies/pharmacy/id:PHARM0001",
      "headers": {
        "Content-Type": "application/json"
      }
    }
    ```

### Get pharmacies by name

- **URL:** `/pharmacies/pharmacy/name:<string:name>`
- **Descrição:** Retorna informações sobre farmácias com base no nome.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/pharmacies/pharmacy/name:DROGASIL",
      "headers": {
        "Content-Type": "application/json"
      }
    }
    ```

### List pharmacies by city

- **URL:** `/pharmacies/city:<string:city>`
- **Descrição:** Retorna informações sobre farmácias com base na cidade.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/pharmacies/city:CAMPINAS",
      "headers": {
        "Content-Type": "application/json"
      }
    }
    ```

### Transactions

### List all transactions

- **URL:** `/transactions`
- **Descrição:** Retorna informações sobre todas as transações.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get a transaction by UUID

- **URL:** `/transactions/id:<string:uuid>`
- **Descrição:** Retorna informações sobre uma transação com base no UUID.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/id:TRAN0001",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by amount

- **URL:** `/transactions/amount/lower_than:<float:amount>`
- **Descrição:** Retorna transações com valor maior ou igual ao especificado.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/amount/lower_than:3.5",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by amount

- **URL:** `/transactions/amount/higher_than:<float:amount>`
- **Descrição:** Retorna transações com valor menor ou igual ao especificado.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/amount/higher_than:3.5",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by patient name

- **URL:** `/transactions/patient/name:<string:fName>`
- **Descrição:** Retorna transações por nome do paciente.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/patient/name:PAULO",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by patient ID

- **URL:** `/transactions/patient/id:<string:uuid>`
- **Descrição:** Retorna transações pelo id do paciente.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/patient/id:PATIENT0001",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by pharmacy ID

- **URL:** `/transactions/pharmacy/id:<string:uuid>`
- **Descrição:** Retorna transações por ID da farmácia.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/pharmacy/id:PHARM0001",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by pharmacy name

- **URL:** `/transactions/pharmacy/name:<string:name>`
- **Descrição:** Retorna transações por nome da farmácia.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/pharmacy/name:DROGASIL",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Get transactions by pharmacy city

- **URL:** `/transactions/pharmacy/city:<string:city>`
- **Descrição:** Retorna transações por cidade da farmácia.
- **Autenticação:** Requer token JWT.
- **Método:** `GET`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "GET",
      "url": "http://localhost:5000/transactions/pharmacy/city:CAMPINAS",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer <seu_token_jwt>"
      }
    }
    ```

### Users

#### Register User

- **URL:** `/users/register`
- **Descrição:** Registra um novo usuário.
- **Método:** `POST`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "POST",
      "url": "http://localhost:5000/users/register",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "USERNAME": "novousuario",
        "PASSWORD": "novasenha"
      }
    }
    ```

#### User Login

- **URL:** `/users/login`
- **Descrição:** Realiza login do usuário.
- **Método:** `POST`
- **Exemplo de Requisição:**
    ```json
    {
      "method": "POST",
      "url": "http://localhost:5000/users/login",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "USERNAME": "usuarioexistente",
        "PASSWORD": "senhacorreta"
      }
    }
    ```

## Documentação da API
Para acessá-la, basta utilizar também o flask run na raiz do projeto, uma vez que a API foi desenvolvida para abrir diretamente o swagger.

```bash
flask run
```

## IMPORTANTE: observações

- O .flaskenv propositalmente foi enviado, uma vez que o intuito é um teste, portanto eu gostaria de deixar as configurações presentes. Também possuo ciêncai de que poderia ter criado um .env para o banco de dados, mas como é de uso comum entre eu e os avaliadores, mantive-o disponível.
- Mantive o pharmacies propositalmente sem necessidade de autenticação, a partir dos seguintes critérios: 1) diferenciar a utilização da API com e sem autenticação e 2) escolhi especificamente este resource para ser acessado, pois simulando em uma lógica real, é menos sensível ID, cidade e nome de farmácias do que transações e pacientes.
