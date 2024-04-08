from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from schemas.url_schema import URLBase
from sqlalchemy.orm import Session
from typing import Annotated
from dependencies import get_current_user
from db.database import get_db
from models.user_model import User
from crud.url_crud import get_url_by_long, create_short_url, get_url_by_short, update_on_click

router = APIRouter(prefix="/url")

@router.post("/new")
async def create_url(url: URLBase, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    existing_url = get_url_by_long(str(url.long_url), db)

    if existing_url:
        raise HTTPException(status_code=400, detail="URL already registered")
    
    new_url = create_short_url(url, current_user, db)
    
    return new_url

@router.get("/r/{url_id}")
async def go_to_url(url_id: str, db: Session = Depends(get_db)):
    url = get_url_by_short(url_id, db)
    if not url:
        raise HTTPException(status_code=404, detail="Not Found")
    
    update_on_click(url, db)
    
    return RedirectResponse(url.long_url, status_code=302)