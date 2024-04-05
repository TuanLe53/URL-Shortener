from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import LoginRequest, RegisterRequest
from sqlalchemy.orm import Session
from datetime import timedelta
from db.database import get_db
from crud.user_crud import create_user, get_user
from utils import verify_password, create_access_token
import validators

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    if not validators.email(request.email):
        raise HTTPException(status_code=400, detail=f"Email is not valid.")
    
    existing_user = get_user(request.email, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = create_user(request, db)
    
    return {
        "message": "Registration successful",
        "user_id": new_user.id
        }

@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = get_user(request.email, db)
    if not user:
        raise HTTPException(status_code=400, detail="There is no account registered with this email address.")
    
    hashed_pw =  user.password
    if not verify_password(request.password, hashed_pw):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token_expire = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email}, expired_delta=access_token_expire)
    
    return {"access_token": access_token}