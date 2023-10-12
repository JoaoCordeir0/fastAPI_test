from pydantic import BaseModel

class ProductModel(BaseModel):
    
    """NOTE: Classe que armazena as informações dos produtos que serão inseridos"""

    name: str
    description: str
    price: float
    category_id: int

    