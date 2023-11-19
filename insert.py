import json
from pymongo import MongoClient

# Read data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Connect to the MongoDB server
client = MongoClient('192.168.0.102', 30000)

# Create or get the database
db = client['lab16']

# Create or get the collection
collection = db['weather']

# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
client.close()