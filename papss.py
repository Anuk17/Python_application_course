#install

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db=client["test_db"]
col=db["test_col"]
data = {_id1,"name":"anu" , "place": "Bangalore"}
col.insert_one(data)
resp = col.find_one(query)
query = {"_id":1}
resp = col.find_one(query)
data["country"] = "India"
col.update_one(query, {"$set":data})
resp = col.find_one(query)
