"""
GET Requests:
GET Requests are used to retrieve something from the server/database.
"""
from fastapi import APIRouter, Query
from rp_fastapi.blob import BlobClient
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
gets = APIRouter()
connection_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container = os.getenv("CONTAINER")
blob_client = BlobClient(connection_str, container)

@gets.get("/")
async def root():
    """
    Simple GET request.
    Returns a basic json object, and expects no parameters
    :return : Json object
    """
    return {"message": "Hello World"}

@gets.get("/test")
async def root():
    """
    Simple GET request.
    Returns a basic json object, and expects no parameters
    :return : Json object
    """
    return {"message": "test"}


@gets.get("/blobclient")
async def get_file_from_blob():
    test_file = blob_client.download(
        blob='export.csv'
    )
    test = pd.read_csv(test_file)
    return {"data": test.to_dict('records')}