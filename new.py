import os
from fastapi import FastAPI
import pymongo
app = FastAPI()
#Connecting to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.college

app.get("/")
def list_students(pcode):
    users = []
    for user in db["students"]  .find():
        users.append(**user)
    return {'users': pcode}