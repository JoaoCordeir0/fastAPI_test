## Manual de uso

#
Instale as dependências do arquivo requirements.txt

> Comando: pip install -r requirements.txt

#
Para rodar local acesse a pasta src e rode o seguinte comando:

> Comando: uvicorn main:app

#
Documentação swagger:

> URL: http://127.0.0.1:8000/docs/

É possível realizar todos os teste na API pela própria documentação

#
Testes na api

> Comando: pytest .\test\test_newUser_api.py

#
Postman

Na pasta test/postman deixei a coleção usada também no postman para teste, basta importar para realizar tais testes.