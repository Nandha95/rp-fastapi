from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str


class Item(BaseModel):
    user: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None