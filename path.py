'''
from fastapi import FastAPI
app=FastAPI()
@app.get("/items/{item_id}")
def read_item(item_id:int,item:str):
    return{"item_id":item_id,"item_name":item}
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: int):
    return {"file_path": file_path}