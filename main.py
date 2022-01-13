from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    is_published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "Title of post 1",
        "content": "Content of post 1",
        "id": 1
    },
    {
        "title": "favorite food",
        "content": "pizza",
        "id": 2
    }
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_posts(post: Post):
    return {"data": post}
