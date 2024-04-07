from pydantic import BaseModel, constr, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    
class RegisterRequest(BaseModel):
    username: constr(min_length=6)
    email: EmailStr
    password: constr(min_length=6)
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: str | None = None