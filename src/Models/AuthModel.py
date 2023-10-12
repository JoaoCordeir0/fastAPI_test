from pydantic import BaseModel

class AuthModel(BaseModel):
    
    """NOTE: Classe que armazena as informações que são coletadas do usuário"""

    email: str
    password_hash: str

    