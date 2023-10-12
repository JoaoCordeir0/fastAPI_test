from pydantic import BaseModel

class CategoryModel(BaseModel):
    
    """NOTE: Classe que armazena o nome das categorias que serão inseridas"""

    name: str

    