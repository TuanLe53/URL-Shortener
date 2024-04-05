from schemas.user_schema import RegisterRequest
from sqlalchemy.orm import Session
from models.user_model import User
from utils import hash_password

def get_user(email: str, session: Session) -> User:
    return session.query(User).filter_by(email=email).first()

def create_user(request: RegisterRequest, session: Session) -> User:
    hash = hash_password(request.password)
    request_dict = request.model_dump()
    request_dict.update({"password": hash})
    
    user = User(**request_dict)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user