import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")

print("Connected")
print(client.list_database_names())
db=client["class"]   #class database

coln=db["details"]  #table details created a collection

user={
    'name':'Donna',
    'age':12,
    'adm':123

}
coln.insert_one(user)

#single user data
