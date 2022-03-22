from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import mysql.connector
import mysql

class info(BaseModel):
    Roll_number: int
    Name: str
    Email_addess: str
    Mobile_number: int
    Address: str
    State: str
    Country: str
    Zip: int

while True:
    try:
        conn =mysql.connector.connect(host='localhost',user='root',password="",database='student')
        cursor=conn.cursor()
        print("database connection is successfull")
        break
    except Exception as error:
        print("connection to database failed")
        print("error:",error)    


app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/registration")
async def get_info():                   
    cursor.execute("""SELECT * FROM info""")
    data=cursor.fetchall()
    get_info()
    print(data)
    return {"data":data}
    