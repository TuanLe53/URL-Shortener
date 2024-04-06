from pydantic import BaseModel, constr

class LoginRequest(BaseModel):
    email: str
    password: str
    
class RegisterRequest(BaseModel):
    username: constr(min_length=6)
    email: str
    password: constr(min_length=6)
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: str | None = None