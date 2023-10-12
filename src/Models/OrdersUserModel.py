from pydantic import BaseModel

class OrdersUserModel(BaseModel):
    
    """NOTE: Classe que armazena as variaveis usadas para consultar os pedidos de um usuário"""

    user_id: int
    start_date: str
    end_date: str