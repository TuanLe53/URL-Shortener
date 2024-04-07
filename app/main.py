from fastapi import FastAPI
from routers.user_route import router as auth_routes
from routers.url_route import router as url_routes

from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes)
app.include_router(url_routes)

@app.get("/")
async def root():
    return {"message": "URL Shortener"}