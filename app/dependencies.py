import os
from typing import Annotated
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from schemas.user_schema import TokenData
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from db.database import get_db
from models.user_model import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                           db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("sub")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter_by(id=token_data.id).first()
    if user is None:
        raise credentials_exception
    
    return user