from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship
from db.database import Base

class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, unique=True, index=True)
    short_url = Column(String, unique=True, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    expired_at = Column(TIMESTAMP, nullable=True)
    last_visited = Column(TIMESTAMP, nullable=True)
    clicks = Column(Integer, default=0)
    created_by_id = Column(UUIDType(binary=False), ForeignKey("users.id"))
    
    created_by = relationship("User", back_populates='urls')