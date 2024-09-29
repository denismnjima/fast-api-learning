from fastapi import FastAPI

app = FastAPI()

@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id":item_id}

# With types
@app.get("/videos/{id}")
async def read_item(id:int):
    return {"video_id":id}