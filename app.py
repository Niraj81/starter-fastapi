from fastapi import FastAPI
from fastapi.responses import FileResponse
import re
from pydantic import BaseModel
from typing import List
app = FastAPI()


class Item(BaseModel):
    item_id: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def list_items():
    return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


@app.post("/items/")
async def create_item(item: Item):
    return item

class InputData(BaseModel):
    data: List[str]

class OutputData(BaseModel):
    is_success: bool = True
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str] = []  # Default to an empty list
    highest_alphabet: List[str]


class getOutput(BaseModel):
    operation_code = 1


@app.get("/bfhl")
async def bfhl_get():
    return getOutput()

@app.post("/bfhl")
async def bfhl_post(input_data: InputData):
    # Process the input_data and extract numbers using regex
    numbers = [value for value in input_data.data if re.match(r'^\d+$', value)]

    # Extract alphabets if they exist
    alphabets = [value for value in input_data.data if re.match(r'^[A-Za-z]$', value)]

    # Calculate the highest alphabet if alphabets exist
    highest_alphabet = [max(alphabets)] if alphabets else []

    response_data = {
        "user_id" : "Niraj_Patidar_10012001",
        "email" : "Niraj.patidar2020@vitbhopal.ac.in",
        "roll_number" : "20BAI10273",
        "numbers" : numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

    return OutputData(**response_data)
