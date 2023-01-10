import random

from fastapi import APIRouter, Query

from .models import User, Item

posts = APIRouter()


@posts.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@posts.post("/user")
async def create_user(user: User, test: str=Query(default='test')) -> dict:
    """
    Creates a user, and returns an ID
    :param user:
    :param email:
    :return:
    """
    userid = random.randint(1, 1000)
    return {
        "Message": 'User Successfully created',
        "user_id": userid,
        "name": user.name,
        "email": user.email,
        "test": test
    }

@posts.put("/user/{user_id}")
async def create_user(user_id: int, user: User, test: str=Query(default='test')) -> dict:
    """
    Creates a user, and returns an ID
    :param user:
    :param email:
    :return:
    """
    # userid = random.randint(1, 1000)
    return {
        "Message": 'User Successfully created',
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "test": test
    }