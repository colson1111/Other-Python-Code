
from pymongo import MongoClient

client = MongoClient()

# access database named test
db = client.test
db = client['test'] # dictionary style access

# access restaurants collection in test database
db.restaurants
coll = db['restaurants']

# insert a document
from datetime import datetime
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

# create an 'InsertOneResult' object, which contains an attribute called
# inserted_id that holds the _id of the inserted document.

result.inserted_id # '57b9cc44ad7c6527dbf3091e'


# Find or query data from Mongodb

# query for all documents in a collection
cursor = db.restaurants.find()


for document in cursor:
    print(document)
    
    
# SPECIFY EQUALITY CONDITIONS

# query by a top level field
cursor = db.restaurants.find({"borough": "Queens"})

for document in cursor:
    print(document)


# query by name
cursor = db.restaurants.find({"name": "Monster Sushi"})

for document in cursor:
    print(document)

    
# query by a field in an embedded document
cursor = db.restaurants.find({"address.zipcode": "10075"})

for document in cursor:
    print(document)

    
# query by a field in an array
# the grades array contains embedded documents as its elements.
cursor = db.restaurants.find({"grades.grade": "B"}) # select all entries with at least one grade = 'B'

for document in cursor:
    print(document)


# SPECIFY CONDITIONS WITH OPERATORS
# {<field1>: {<operator1>: <value1> }}

# greater than
cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
for document in cursor:
    print(document)
    
# less than
cursor = db.restaurants.find({"grades.score": {"$lt": 10}})
for document in cursor:
    print(document)

# combining conditions
cursor = db.restaurants.find({"cuisine": "Italian", 
                              "address.zipcode" : "10075", 
                              "grades.score": {"$lt": 10}})
for document in cursor:
    print(document)

# using the or operator
cursor = db.restaurants.find({"$or": [{"cuisine": "Italian"},
                                      {"address.zipcode": "10075"}]})

for document in cursor:
    print(document)
    

# sorting results
import pymongo
cursor = db.restaurants.find({"grades.score": {"$gt": 30}}).sort([
    ("grades.score", pymongo.ASCENDING)])

for document in cursor:
    print(document)
    
    
    
# UPDATING DATA

# update top level fields
result = db.restaurants.update_one(
    {"name": "Juni"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)

result.matched_count

result.modified_count

# update embedded field
rest1 = db.restaurants.find({"restaurant_id": "41156888"})
for doc in rest1:
    print(doc)

result = db.restaurants.update_one(
    {"restaurant_id": "41156888"},
    {"$set": {"address.street": "East 31st Street"}}
)
result.matched_count

result.modified_count


# update multiple documents
result = db.restaurants.update_many(
    {"address.zipcode": "10016", "cuisine":"Other"},
    {
        "$set": {"cuisine": "Category To Be Determined"},
        "$currentDate": {"lastModified":True}
     }
)

result.matched_count

result.modified_count


# REPLACE AN ENTIRE DOCUMENT
result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
)

result.matched_count

result.modified_count


# REMOVE ALL DOCUMENTS THAT MATCH A CONDITION

# result = db.restaurants.delete_many({"borough": "Manhattan"})
# result.deleted_count

# REMOVE ALL DOCUMENTS

# result = db.restaurants.delete_many({})
# result.deleted_count

# DROP A COLLECTION

# db.restaurants.drop()


# GROUP DOCUMENTS BY A FIELD AND CALCULATE COUNT
cursor = db.restaurants.aggregate(
    [
        {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
    ]
)

for document in cursor:
    print(document)

# FILTER AND GROUP DOCUMENTS
cursor = db.restaurants.aggregate(
    [
        {"$match": {"borough": "Queens", "cuisine": "Brazilian"}},
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
    ]
)

for document in cursor:
    print(document)
    
    
# CREATE A SINGLE FIELD INDEX
db.restaurants.create_index([("cuisine", pymongo.ASCENDING)])

# CREATE A COMPOUND INDEX
db.restaurants.create_index([
    ("cuisine", pymongo.ASCENDING),
    ("address.zipcode", pymongo.DESCENDING)
])


# read from mongodb to pandas dataframe
import pandas as pd
df = pd.DataFrame(list(db.restaurants.find({})))


