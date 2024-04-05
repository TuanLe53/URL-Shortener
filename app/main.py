from fastapi import FastAPI, HTTPException
# from schemas import URLBase
# import validators
from routers.user_route import router as auth_route

from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_route)

@app.get("/")
async def root():
    return {"message": "URL Shortener"}


# @app.post("/create-url")
# async def create_short_url(url: URLBase):
#     url_dict = url.model_dump()
    
#     if not validators.url(url_dict["target_url"]):
#         raise HTTPException(status_code=400, detail="URL is not valid")
    
#     return url