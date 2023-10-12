from Core.DataBase import DataBase
from Controllers.JWTController import JWT
import psycopg2
import requests
import hashlib
import json

class UserController():
    
    """NOTE: Classe que controla as informações do usuário"""

    def __init__(self) -> None:
        pass

    # Função que insere o usuário no banco de dados 
    def insertUser(data) -> object:           
        try:
            conn, cursor = DataBase.conn()

            query_sql = """INSERT INTO users(name, email, password_hash) VALUES (%s,%s,%s)"""
            query_params = (data.name, data.email, hashlib.sha1(data.password_hash.encode()).hexdigest())

            cursor.execute(query_sql, query_params)
            conn.commit()
            
            message = 'Usuário inserido com sucesso!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}          


    # Função que verifica se o usuário está cadastrado no banco e retorna um código JWT caso o login esteja correto
    def authUser(data) -> object:
        auth = False
        try:
            conn, cursor = DataBase.conn()

            query_sql = """SELECT * FROM users WHERE email = %s AND password_hash = %s"""
            query_params = (data.email, hashlib.sha1(data.password_hash.encode()).hexdigest())            

            cursor.execute(query_sql, query_params)
            conn.commit()

            if cursor.rowcount > 0:
                jwt = JWT.jwt_generate(data.email)
                auth = True
            else:
                message = "Usuário ou senha incorretos"
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)            
        finally:
            if conn:
                cursor.close()
                conn.close()

        if auth:
            return {'jwt': jwt}  
        return {'message': message}


    # Função que insere um endereço para um determinado usuário
    def insertUserAddress(data) -> object:
        try:
            conn, cursor = DataBase.conn()

            query_sql = """INSERT INTO addresses(user_id, description, postal_code, street, complement, neighborhood, city, state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            query_params = (data.user_id, data.description, data.postal_code, data.street, data.complement, data.neighborhood, data.city, data.state)

            cursor.execute(query_sql, query_params)
            conn.commit()

            message = 'Endereço atrelado ao usuário com sucesso!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}   
    

    # Função responsável por consultar a API viacep e retornar as informações de endereço do CEP passado. 
    def getInfoCep(cep) -> object:        
        request = requests.get(f'https://viacep.com.br/ws/{cep.replace("-", "").replace(" ", "")}/json')    
        return json.loads(request.content)


    # Função que lista todos os usuários cadastrados no banco de dados
    def getUsers() -> object:
        flag = False
        users_list = list()
        try:
            conn, cursor = DataBase.conn()

            cursor.execute("""SELECT name, email FROM users""")
            users = cursor.fetchall()
            conn.commit()

            if cursor.rowcount > 0:
                flag = True
                for item in users:
                    users_list.append({'name': item[0], 'email': item[1]})
                
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        if flag:
            return {'users': users_list}
        return {'message': message}  

    # Função que lista todos os endereços de um determinado usuário
    def getAddressUser(user_id) -> object:
        flag = False
        address_user_list = list()
        try:
            conn, cursor = DataBase.conn()

            cursor.execute("""SELECT description, postal_code, street, complement, neighborhood, city, state FROM addresses WHERE user_id = %s""", (user_id, ))
            address = cursor.fetchall()
            conn.commit()

            if cursor.rowcount > 0:
                flag = True
                for item in address:
                    address_user_list.append({'description': item[0], 'postal_code': item[1], 'street': item[2], 'complement': item[3], 'neighborhood': item[4], 'city': item[5], 'state': item[6]})
            else:    
                message = "Nenhum endereçõ atrelado a este usuário!"

        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        if flag:
            return {'address': address_user_list}
        return {'message': message}  


    # Função que seleciona todas os pedidos de um usuário no banco de dados
    def getOrdersUser(data) -> object:
        flag = False
        orders_user_list = list()
        query_date = ""
        try:
            conn, cursor = DataBase.conn()

            if len(data.start_date) > 7 and len(data.end_date) > 7:
                query_date = f" AND o.order_date >= '{data.start_date}' AND o.order_date <= '{data.end_date}'"

            # Seleciona todos os pedidos do usuário
            query_sql_products = """SELECT o.id, p.name, p.description, p.price FROM order_items as oi 
                                    INNER JOIN orders as o on oi.order_id = o.id
                                    INNER JOIN products as p on oi.product_id = p.id
                                    WHERE o.user_id = %s""" + query_date
            query_params_products = (data.user_id, )

            # Seleciona o endereço do usuário
            query_sql_address = """SELECT distinct(a.id), a.* FROM order_items as oi 
                                   INNER JOIN orders as o on oi.order_id = o.id
                                   INNER JOIN products as p on oi.product_id = p.id
                                   INNER JOIN addresses as a on o.address_id = a.id
                                   WHERE o.user_id = %s""" + query_date
            query_params_address = (data.user_id, )

            # Seleciona o preco total dos pedidos
            query_sql_price_total = """SELECT sum(p.price) FROM order_items as oi 
                                       INNER JOIN orders as o on oi.order_id = o.id
                                       INNER JOIN products as p on oi.product_id = p.id
                                       WHERE o.user_id = %s""" + query_date
            query_params_price_total = (data.user_id, )

            cursor.execute(query_sql_products, query_params_products)
            orders = cursor.fetchall()
            conn.commit()            

            # Adiciona todas as informações na lista que será retornada
            if cursor.rowcount > 0:
                flag = True
                for item in orders:
                    orders_user_list.append({'order_id': item[0], 'name': item[1], 'description': item[2], 'price': item[3]})
                
                cursor.execute(query_sql_address, query_params_address)
                address = cursor.fetchall()[0]
                conn.commit()

                orders_user_list.append({'address': {'description': address[3], 'postal_code': address[4], 'street': address[5], 'complement': address[6], 'neighborhood': address[7], 'city': address[8], 'state': address[9]}})

                cursor.execute(query_sql_price_total, query_params_price_total)
                price_total = cursor.fetchall()[0]
                conn.commit()

                orders_user_list.append({'price_total': price_total})

            else:    
                message = "Nenhum pedido registrado para este usuário!"

        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        if flag:
            return {'orders': orders_user_list}
        return {'message': message}  

    
    # Função que deleta os pedidos cancelados de um usuário
    def deleteOrderUser(user_id) -> object:
        try:
            conn, cursor = DataBase.conn()

            query_sql = """DELETE FROM orders WHERE user_id = %s AND status = 'Cancelado'"""
            query_params = (user_id, )

            cursor.execute(query_sql, query_params)
            conn.commit()

            if cursor.rowcount > 0:
                message = f'{cursor.rowcount} pedidos apagados com sucesso!'
            else:
                message = 'Nenhum pedido apto a ser apagado!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}  
    

    # Função responsável por editar um usuário
    def updateUser(data) -> object:
        try:
            conn, cursor = DataBase.conn()

            query_sql = """UPDATE users SET name = %s, email = %s, password_hash = %s WHERE id = %s"""
            query_params = (data.name, data.email, hashlib.sha1(data.password_hash.encode()).hexdigest(), data.user_id)

            cursor.execute(query_sql, query_params)
            conn.commit()

            if cursor.rowcount > 0:
                message = f'Usuário editado com sucesso!'
            else:
                message = 'Usuário não existe!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}  