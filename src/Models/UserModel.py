from pydantic import BaseModel

class UserModel(BaseModel):
    
    """NOTE: Classe que armazena as informações que são coletadas do usuário"""

    name: str
    email: str
    password_hash: str


class UserEditModel(BaseModel):
    
    """NOTE: Classe que armazena as informações que são coletadas do usuário para edição"""

    user_id: int
    name: str
    email: str
    password_hash: str