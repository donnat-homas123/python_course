import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")

print("Connected")
print(client.list_database_names())
db=client["class"]   

coln=db["details"]  

user=[{
    'name':'Donna',
    'age':12,
    'adm':123

},{
   'name':'Ann',
    'age':22,
    'adm':14523 
},{
   'name':'Dionna',
    'age':121,
    'adm':123675 
},{
   'name':'Donhfuj',
    'age':23,
    'adm':1263 
}]

for doc in coln.find({"name":{"$regex":"^D"},"age":{"$gt":22,"$lt":40}}):
    print(doc)

#find name starting with D and age bw 22 and 40    