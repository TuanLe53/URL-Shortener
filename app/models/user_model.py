from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql import func
from db.database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    last_login = Column(TIMESTAMP, nullable=True)