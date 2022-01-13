from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange


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


def find_post(id_):
    for p in my_posts:
        if p["id"] == id_:
            return p


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id_}")
async def get_post(id_: int):
    post = find_post(id_)
    return {"post_detail": post}


@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
