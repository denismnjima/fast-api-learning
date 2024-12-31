from fastapi import FastAPI

app = FastAPI()

# If you don't provide path parameters, 
# function parameters will be assumed to be query strings.
@app.get('/greet/{name}')
async def greet_name(name:str,age:int) -> dict:
    return {'message': f"hello {name}","age":age}