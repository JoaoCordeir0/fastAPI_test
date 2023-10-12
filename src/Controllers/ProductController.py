from Core.DataBase import DataBase
import psycopg2

class ProductController():
    
    """NOTE: Classe que controla as informações dos produtos"""

    def __init__(self) -> None:
        pass

    # Função que insere uma nova categoria de produtos no banco de dados
    def insertCategory(data) -> object:          
        try:
            conn, cursor = DataBase.conn()

            query_sql = """INSERT INTO categories(name) VALUES (%s)"""
            query_params = (data.name, )
            cursor.execute(query_sql, query_params)
            conn.commit()
            
            message = 'Categoria inserida com sucesso!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}          


    # Função que insere um novo produto no banco de dados
    def insertProduct(data) -> object:
        try:
            conn, cursor = DataBase.conn()

            query_sql = """INSERT INTO products(name, description, price) VALUES (%s,%s,%s) RETURNING id """
            query_params = (data.name, data.description, data.price)
            cursor.execute(query_sql, query_params)
            product_id = cursor.fetchone()[0]
            conn.commit()
            
            query_sql = """INSERT INTO products_categories(product_id, category_id) VALUES (%s,%s) """
            query_params = (product_id, data.category_id)
            cursor.execute(query_sql, query_params)            
            conn.commit()
            
            message = 'Produto inserido com sucesso!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}      
    

    # Função que adiciona um pedido para um determinado usuário
    def insertOrderUser(data) -> object:        
        try:
            conn, cursor = DataBase.conn()

            len_product_id, list_product_id = len(data.products['product_id']), data.products['product_id']
            len_quantity, list_quantity = len(data.products['quantity']), data.products['quantity']
            len_price, list_price = len(data.products['price']), data.products['price']

            # Verifica se o tamanhos das listas são iguais para não haver problemas no insert
            if len_product_id == len_quantity == len_price:
                query_sql = """INSERT INTO orders(user_id, address_id, status, order_date) VALUES (%s,%s,%s,%s) RETURNING id"""
                query_params = (int(data.user_id), int(data.address_id), data.status, data.order_date)
                cursor.execute(query_sql, query_params)
                order_id = cursor.fetchone()[0]
                conn.commit()                    
            
                for index in range(len_product_id):
                    query_sql = """INSERT INTO order_items(order_id, product_id, price, quantity) VALUES (%s,%s,%s,%s) RETURNING id"""
                    query_params = (int(order_id), int(list_product_id[index]), list_price[index], list_quantity[index])
                    cursor.execute(query_sql, query_params)                
                    conn.commit()                

                message = 'Pedido inserido com sucesso!'
            else:
                message = 'Não foi possível inserir o pedido pois a lista de pedidos não tem todas as informações corretas!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message}   


    # Função que lista todos os produtos cadastrados no banco de dados
    def getProducts() -> object:
        flag = False
        products_list = list()
        try:
            conn, cursor = DataBase.conn()

            cursor.execute("""SELECT name, description, price FROM products""")
            products = cursor.fetchall()
            conn.commit()

            if cursor.rowcount > 0:
                flag = True
                for item in products:
                    products_list.append({'name': item[0], 'description': item[1], 'price': item[2]})
                
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        if flag:
            return {'products': products_list}
        return {'message': message}  


    # Função que apaga categoria que não estejam em uso 
    def deleteCategory() -> object:
        try:
            conn, cursor = DataBase.conn()

            cursor.execute("""DELETE FROM categories WHERE id not in (SELECT category_id FROM products_categories)""")
            conn.commit()

            if cursor.rowcount > 0:
                message = f'{cursor.rowcount} categoria(as) apagada(as) com sucesso!'
            else:
                message = 'Nenhuma categoria disponível para exclusão!'
        except (Exception, psycopg2.Error, psycopg2.DataError) as e:      
            message = str(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

        return {'message': message} 