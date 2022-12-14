import random

from fastapi import FastAPI
from .get import gets
from .post import posts
'''
Initializing the FastAPI Application
'''
app = FastAPI()
app.include_router(gets)
app.include_router(posts)
