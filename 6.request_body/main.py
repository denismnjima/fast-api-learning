from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# creating pydantic validation model
class Book(BaseModel):
    title:str
    author:str


@app.post('/create_book')
async def create_book(book_data:Book):
    return {
        "title":book_data.title,
        "author":book_data.author
    }