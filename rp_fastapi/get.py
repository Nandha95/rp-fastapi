"""
GET Requests:
GET Requests are used to retrieve something from the server/database.
"""
from fastapi import APIRouter

from .models import User, Item

gets = APIRouter()


@gets.get("/")
async def root():
    """
    Simple GET request.
    Returns a basic json object, and expects no parameters
    :return : Json object
    """
    return {"message": "Hello World"}


@gets.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Get request with path validation. Takes a parameter at the end of the
    request path, and uses that parameter as the request parameter
    :param item_id:
    :return:
    """
    return {"item_id": item_id}


@gets.get("/user")
async def get_user(user: str) -> dict:
    """
    GET Request with Query validation
    :return:
    """
    return {"User": user}
