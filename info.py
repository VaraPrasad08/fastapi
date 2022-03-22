from fastapi import  FastAPI
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
    
    
app=FastAPI()

conn =mysql.connector.connect(host='localhost',user='root',password="",database='student')
cursor=conn.cursor()
print("database connection is successfull")

@app.post("/registration")
def create_info(info:info):
    sql=" INSERT INTO info (Roll_number,Name, Email_address, Mobile_number, Address, Country, State, Zip) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(info.Roll_number,info.Name,info.Email_addess,info.Mobile_number,info.Address,info.Country,info.State,info.Zip)

    cursor.execute(sql,val)
    new_data=cursor.fetchone()
    conn.commit()
    return{"data":new_data}