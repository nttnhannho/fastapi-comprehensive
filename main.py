from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    is_published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your post"}


@app.post("/posts")
async def create_post(post: Post):
    return {"data": post}
