# LEA-RECORD-SHOP

## Proposta

O Lea Record Shop é uma API que simula as atividades básicas de uma loja música, onde é possível realizar as seguintes operações:

- CRUD de Usuários
- CRUD de Discos para venda
- Criação de pedidos vinculando um cliente a um disco/quantidade

## Tecnologias utilizadas:

Apesar da aplicação ser simples, ela precisa lidar com um volume grande de usuários tentando realizar compras ao mesmo tempo, pensando nisso foram utilizadas as seguintes tecnologias:

- Flask
    - Um dos microframeworks Python mais bem estalecidos, oferece uma forma simples e rápida de criar uma API com as principais funcionalidades, além da facilidade e segurança o Flas ainda conta com uma comunidade enorme que está sempre criando e dando manutenção a nova libs. Ele pode não ser o mais performático dos atuais frameworks Python, porém ele cumpre muito bem o seu papel
- AWS Lambda / API Gateway
    - Considerando que iremos ter um grande volume de usuários em momentos chave como lançamentos de discos, adotamos aqui uma arquitetura serverless, onde realizamos o deploy da nossa aplicação Flask em um Lambda (que pode ser escalado conforme a quantidade de usuários acessando a aplicação ao mesmo tempo) e utilizamos o API Gateway para fazer o roteamento para nossa API.
- Zappa
    - Como tivemos um tempo curto de desenvolvimento, utilizamos o Zappa para cuidar da parte do deploy da aplicação na AWS, ele realiza toda a criação de lambdas e regras de proxy do API Gateway para a nossa aplicação.
- PostgresSQL
    - Além de ser open source, o Postgres oferece diversos recursos de validação de dados e sua performance é superior se comparada a outros bancos. Esse projeto inicialmente utiliza ele por precisarmos de uma relação muito clara na hora de realizar a venda dos discos, mas a ideia para o futuro é otimizar algumas partes do processo utilizando o NoSQL.
    - Nas tabelas onde os dados não são inseridos de forma constante como a tabela de Customers/Disks foram criados indexes para os campos mais utilizados para pesquisa.
- SQLAlchemy
    - Com o SQLAlchemy temos todo o poder dos bancos relacionais, sem precisar se prender a um provedor só, com ele é possível realizar todo o mapeamento/modelagem das tabelas e utilizar as mesmas em qualquer banco de dados e de forma muito facilitada.
- Locust
    - O Locust é uma ferramente de testes poderosa que permite ao usuário criar uma massa de testes e configurá-los de forma com que simulem um usuário real utilizando a aplicação.

