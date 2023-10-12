import psycopg2

class DataBase():
    
    """NOTE: Classe de conexão com o banco de dados Postgress"""

    def __init__(self) -> None:
        pass

    def conn():
        con = psycopg2.connect(
            host='localhost', 
            database='prova',
            user='postgres', 
            password='postgres'
        )
        cur = con.cursor()

        return con, cur


