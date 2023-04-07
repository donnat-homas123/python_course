import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")

print("Connected")
print(client.list_database_names())
db=client["class"]  
coln=db["details"] 

def register():
    regirt_trn = {}
    print('Registration')
    for i in range(1):
        user_name=input('enter username ')
        pss_wrd=input('enter pss_wrd')
        regirt_trn['user_name'] = user_name
        regirt_trn['pss_wrd'] = pss_wrd
    l=[]
    l.append(regirt_trn)
    print(l)      
    coln.insert_many(l)
register()

def login():
    print('Login')
    user_name=input('enter username')
    pss_wrd=input('enter pss_wrd')
    a=coln.find_one({"user_name":user_name, "pss_wrd": pss_wrd}) 
    if a:
        print("Login succes")
    else:
        print("Wrong pass")

login()

