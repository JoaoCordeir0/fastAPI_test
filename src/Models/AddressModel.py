from pydantic import BaseModel

class AddressModel(BaseModel):
    
    """NOTE: Classe que armazena as informações de endereço de um usuário"""

    user_id: int
    description: str
    postal_code: str
    street: str
    complement: str
    neighborhood: str
    city: str
    state: str