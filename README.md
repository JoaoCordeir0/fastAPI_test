## Descrição

API capaz de receber requisições HTTP e retornar respostas no formato JSON. 

API permite a criação, leitura, atualização e exclusão (CRUD) de recursos em um banco de dados PostgreSQL.

## Banco de dados

Banco de dados PostgreSQL. 

## Requisitos funcionais

- A API deve permitir o cadastro de usuários com nome, e-mail e senha. A senha deve ser armazenada de forma segura no banco de dados.
- A API deve permitir a autenticação de usuários cadastrados, retornando um token JWT válido.
- A API deve permitir que seja cadastrado um ou mais endereços para um mesmo usuário. Os campos do endereço são: descrição, cep, logradouro, complemento, bairro, cidade e estado.
- A API deve possuir um endpoint que retorne os dados de endereço a partir do número do CEP. Utilizar a API https://viacep.com.br/ como base para buscar os dados.
- A API deve permitir o cadastro de categorias de produtos com nome.
- A API deve permitir o cadastro de produtos com nome, descrição e preço. Um produto pode ter uma ou mais categorias associadas.
- A API deve permitir a criação de pedidos associados a um usuário. Cada pedido terá status, data e conterá um ou mais produtos com seu respectivo preço e quantidade. Além disso, cada pedido será vinculado a um dos endereços do usuário.
- A API deve permitir a consulta de usuários cadastrados.
- A API deve permitir a consulta de produtos cadastrados.
- A API deve permitir a consulta de endereços de um usuário.
- A API deve permitir a consulta de pedidos de um usuário, retornando uma lista dos produtos, seus preços e o valor total do pedido e o endereço do usuário. Também deverá permitir consultar por período de datas.

## Requisitos não funcionais

- A API deve ser documentada usando o padrão OpenAPI/Swagger. Deve ser possível listar e testar os endpoints.
- A API deve ser testada usando o framework de teste unittest ou pytest.
- A API deve ser implementada seguindo as boas práticas de desenvolvimento em Python, incluindo a utilização de padrões de projeto e a organização do código em módulos e pacotes.
- A API deve se comunicar com o banco de dados PostgreSQL
- A API deve ter uma camada de segurança com JWT
- A API deve ser desenvolvida de forma que tenha boa performance
- A API deve possuir tratamento e validação dos dados
- A API deve fornecer códigos de status em conformidade com o padrão do protocolo HTTP.

