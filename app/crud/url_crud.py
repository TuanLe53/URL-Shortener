from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from models.url_model import URL
from models.user_model import User
from schemas.url_schema import URLBase
from datetime import timedelta, datetime, timezone
import secrets
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def get_url_by_long(long_url: str, session: Session) -> URL:
    return session.query(URL).filter_by(long_url=long_url).first()

def get_url_by_short(short_url: str, session: Session) -> URL:
    return session.query(URL).filter_by(short_url=short_url).first()

def create_short_url(request: URLBase, user: User, session: Session) -> URL:
    long_url = str(request.long_url)
    expired_at = datetime.now(timezone.utc) + timedelta(days=1)
    short_url = secrets.token_urlsafe(8)
    created_by_id = user.id
    
    new_url = URL(long_url=long_url, short_url=short_url, expired_at=expired_at, created_by_id=created_by_id)

    session.add(new_url)
    session.commit()
    session.refresh(new_url)
    
    return new_url

def update_on_click(url: URL, session: Session) -> None:
    url.clicks += 1
    url.last_visited = func.now()
    
    session.commit()