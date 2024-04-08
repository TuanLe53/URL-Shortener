from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    long_url: HttpUrl