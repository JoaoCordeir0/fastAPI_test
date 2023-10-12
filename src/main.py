from typing import Union
from fastapi import FastAPI
from Controllers.UserController import UserController
from Controllers.ProductController import ProductController
from Models.UserModel import UserModel, UserEditModel
from Models.AddressModel import AddressModel
from Models.AuthModel import AuthModel
from Models.CategoryModel import CategoryModel
from Models.ProductModel import ProductModel
from Models.OrderModel import OrderModel
from Models.OrdersUserModel import OrdersUserModel

# Instância da API
app = FastAPI()

"""NOTE Rotas get da API -> """
#
# Rota de informações da API
#
@app.get("/")
def main() -> object:
    return {"Prova": "Prática Desenvolvedor Backend Python - Pleno", "Versão": "1.0", "Dev by": "João Victor Cordeiro", "Data": "16/04/2023"}

#
# Rota da API que retorna o endereço através do cep
#
@app.get("/CEPConsult/{cep}")
async def cepConsult(cep: str) -> object:
    return UserController.getInfoCep(cep)

#
# Rota da API que lista todos os usuários
#
@app.get("/ListUsers")
async def listUsers() -> object:
    return UserController.getUsers()

#
# Rota da API que lista todos os produtos
#
@app.get("/ListProducts")
async def listProducts() -> object:
    return ProductController.getProducts()

#
# Rota da API que lista todos os endereços de um determinado usuário
#
@app.get("/ConsultAddressUser/{user_id}")
async def consultAddressUser(user_id: int) -> object:
    return UserController.getAddressUser(user_id)


"""NOTE Rotas post da API -> """
#
# Rota da API que adiciona um novo usuário
#
@app.post("/NewUser")
async def newUser(data: UserModel) -> object:
    return UserController.insertUser(data)

#
# Rota da API autentica um usuário
#
@app.post("/AuthUser")
async def AuthUser(data: AuthModel) -> object:
    return UserController.authUser(data)

#
# Rota da API que registra um endereço para um determinado usuário
#
@app.post("/RegisterUserAddress")
async def registerUserAddress(data: AddressModel) -> object:
    return UserController.insertUserAddress(data)

#
# Rota da API que adiciona uma nova categoria de produtos
#
@app.post("/NewCategory")
async def newCategory(data: CategoryModel) -> object:
    return ProductController.insertCategory(data)

#
# Rota da API que adiciona um novo produto
#
@app.post("/NewProduct")
async def newProduct(data: ProductModel) -> object:
    return ProductController.insertProduct(data)

#
# Rota da API que adiciona um pedido para um usuário
#
@app.post("/NewOrderUser")
async def newOrderUser(data: OrderModel) -> object:
    return ProductController.insertOrderUser(data)

#
# Rota da API que adiciona um pedido para um usuário
#
@app.post("/ConsultOrdersUser")
async def consultOrdersUser(data: OrdersUserModel) -> object:
    return UserController.getOrdersUser(data)


"""NOTE Rotas delete da API -> """
#
# Funcionalidades adicionais desenvolvidos apenas para agregar na API
#

#
# Rota da API que deleta os pedidos de um usuário caso o status seja "cancelado"
#
@app.delete("/DelOrderUser/{user_id}")
async def delOrderUser(user_id: int) -> object:
    return UserController.deleteOrderUser(user_id)

#
# Rota da API que deleta categorias de produto que não estejam sendo usadas
#
@app.delete("/DelCategory")
async def delCategory() -> object:
    return ProductController.deleteCategory()


"""NOTE Rotas put da API -> """
#
# Rota da API que edita um usuário
#
@app.put("/EditUser")
async def editUser(data: UserEditModel) -> object:
    return UserController.updateUser(data)

