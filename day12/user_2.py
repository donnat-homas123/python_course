#multi user data
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")

print("Connected")
print(client.list_database_names())
db=client["class"]   #class database

coln=db["details"]  #table details created a collection

#inside list store as dictionary
user=[{
    'name':'Donna',
    'age':12,
    'adm':123

},{
   'name':'Ann',
    'age':22,
    'adm':14523 
},{
   'name':'Sonna',
    'age':121,
    'adm':123675 
},{
   'name':'Donhfuj',
    'age':23,
    'adm':1263 
}]
coln.insert_many(user)