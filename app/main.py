from typing import Optional
from fastapi import FastAPI, status, HTTPException, Response
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


def find_index_post(id_):
    for i, p in enumerate(my_posts):
        if p["id"] == id_:
            return i


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id_}")
async def get_post(id_: int):
    post = find_post(id_)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id_} was not found")

    return {"post_detail": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.delete("/posts/{id_}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id_: int):
    index = find_index_post(id_)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id_} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id_}")
def update_post(id_: int, post: Post):
    index = find_index_post(id_)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id_} does not exist")

    post_dict = post.dict()
    post_dict["id"] = id_
    my_posts[index] = post_dict

    return {"data": post_dict}
