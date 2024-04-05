from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from db.database import Base

# class URL(Base):
#     __tablename__ = "urls"
    
#     id = Column(Integer, primary_key=True, index=True)
#     original_url = Column(String, unique=True, index=True)
#     short_url = Column(String, unique=True, index=True)
#     created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
#     expired_at = Column(TIMESTAMP, nullable=True)
#     last_visited = Column(TIMESTAMP, nullable=True)
#     clicks = Column(Integer, default=0)