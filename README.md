# LEA-RECORD-SHOP

## Proposta

O Lea Record Shop é uma API que simula as atividades básicas de uma loja música, onde é possível realizar as seguintes operações:

- CRUD de Usuários
- CRUD de Discos para venda
- Criação de pedidos vinculando um cliente a um disco/quantidade

## 🧱 Tecnologias utilizadas:

Apesar da aplicação ser simples, ela precisa lidar com um volume grande de usuários tentando realizar compras ao mesmo tempo, pensando nisso foram utilizadas as seguintes tecnologias:

- Flask
    - Um dos microframeworks Python mais bem estalecidos, oferece uma forma simples e rápida de criar uma API com as principais funcionalidades, além da facilidade e segurança o Flas ainda conta com uma comunidade enorme que está sempre criando e dando manutenção a nova libs. Ele pode não ser o mais performático dos atuais frameworks Python, porém ele cumpre muito bem o seu papel
- AWS Lambda / API Gateway
    - Considerando que iremos ter um grande volume de usuários em momentos chave como lançamentos de discos, adotamos aqui uma arquitetura serverless, onde realizamos o deploy da nossa aplicação Flask em um Lambda (que pode ser escalado conforme a quantidade de usuários acessando a aplicação ao mesmo tempo) e utilizamos o API Gateway para fazer o roteamento para nossa API.
- Zappa
    - Como tivemos um tempo curto de desenvolvimento, utilizamos o Zappa para cuidar da parte do deploy da aplicação na AWS, ele realiza toda a criação de lambdas e regras de proxy do API Gateway para a nossa aplicação.
- SQLAlchemy
    - Com o SQLAlchemy temos todo o poder dos bancos relacionais, sem precisar se prender a um provedor só, com ele é possível realizar todo o mapeamento/modelagem das tabelas e utilizar as mesmas em qualquer banco de dados e de forma muito facilitada.
- PostgresSQL
    - Além de ser open source, o Postgres oferece diversos recursos de validação de dados e sua performance é superior se comparada a outros bancos. Esse projeto inicialmente utiliza ele por precisarmos de uma relação muito clara na hora de realizar a venda dos discos, mas a ideia para o futuro é otimizar algumas partes do processo utilizando o NoSQL.
    - Nas tabelas onde os dados não são inseridos de forma constante como a tabela de Customers/Disks foram criados indexes para os campos mais utilizados para pesquisa.
- Amazon RDS
    - Aproveitando a arquitetura em nuvem, utilizamos o Amazon RDS para hostear o banco de dados tornando possível escalar o servidor de forma fácil e eficiente além de termos diversos recursos de monitoramento/performance
- Locust
    - O Locust é uma ferramente de testes poderosa que permite ao usuário criar uma massa de testes e configurá-los de forma com que simulem um usuário real utilizando a aplicação.

## 🚀 Como executar o projeto

Ë preciso ter o Python3.9 instalado e executar o seguinte comando:

    python -m venv venv

Após isso, basta ativar o ambiente virtual e instalar as dependências:

    source venv/bin/activate
    pip install -r requirements.txt

Agora é só executar o comando e um servidor de testes será iniciado:

    flask run


## 🎲 AWS

Esse projeto também está rodando na AWS, nele é possível realizar todas as operações citadas acima, a url é a seguinte:

https://pqg5jyv6rl.execute-api.us-east-1.amazonaws.com/dev/v1

## 🧭 Documentação da API

É possível realizar a importação da collection do Insomnia com todos os endpoints/requests através do link abaixo:

https://lea-record-shop.s3.amazonaws.com/insomnia_collection.json

Para realizar a importação, basta abrir o Insomnia, clicar no botão de Criar e escolher a opção "Import from > URL" e colar a URL do S3.

Referência: https://docs.insomnia.rest/insomnia/import-export-data
