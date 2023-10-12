from pydantic import BaseModel

class OrderModel(BaseModel):
    
    """NOTE: Classe que armazena as informações do pedido de um usuário"""

    user_id: int
    status: str
    order_date: str
    products: object
    address_id: str


    