from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/greet')
async def greet_name(name:Optional[str]="user",age:int=0) -> dict:
    return {'message': f"hello {name}","age":age}