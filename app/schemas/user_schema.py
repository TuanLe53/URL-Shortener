from pydantic import BaseModel, constr

class LoginRequest(BaseModel):
    email: str
    password: str
    
class RegisterRequest(BaseModel):
    username: constr(min_length=6)
    email: str
    password: constr(min_length=6)