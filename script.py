import pymongo
from pymongo import MongoClient

# Connect 
client = MongoClient("mongodb+srv://cluster0.pnxzwgz.mongodb.net/")
db = client["mnk3kd"]  

# Create collection
collection = db["my_collection"]

# Insert many documents
documents = [ 
    {"name": "document1", "value": 84},
    {"name": "document2", "value": 20},
    {"name": "document3", "value": 15},
    {"name": "document4", "value": 42},
    {"name": "document5", "value": 78}
]
collection.insert_many(documents)

# Query 
result = collection.find().limit(3)
for document in result:
    print(document)
