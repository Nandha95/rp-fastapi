import os
import pickle
import random

from fastapi import FastAPI, status, HTTPException
from typing import Optional
from pydantic import BaseModel

from .utils import get_user_id_generator
class User(BaseModel):
    name: str
    email: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()
itemsdb = {}
usersdb = {}
useritemsdb = {}

user_id = get_user_id_generator()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user")
async def create_user(user: User) -> dict:
    """
    Creates a user, and returns an ID
    :param user:
    :param status_code:
    :return:
    """
    id = next(user_id)
    print(id)

    usersdb.update({
        id: {
            "name": user.name,
            "email": user.email
        }
    })
    return {
        "Message": 'User Successfully created',
        "user_id": id
    }


@app.get("/users")
async def get_all_users() -> dict:
    """
    Returns all the users created
    :return:
    """
    return usersdb

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
