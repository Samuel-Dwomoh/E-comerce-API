from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: str
    password: str
    
class ProductModel(BaseModel):
    name: str
    desciption: str
    price: int
    quantity: int
    
class LoginModel(BaseModel):
    username: str
    password: str
    
class CartModel(BaseModel):
    user_id: int
    product_id: int
    quantity: int