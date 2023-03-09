users={}
print('enter username of 3 people')
for i in range(3):
    username=input('enter the username')
    if username in users:
        print('already exist')
    else:
        password=input('enter the password')    
        users[username]=password
    
print(users)


user_name=input('enter username')
if user_name in users:
    pass_word=input('enter the password')
    correctpassword=users[user_name] #pass

    if correctpassword == pass_word:
        print('Login success')
    else:
        print('invalid password')
else:
    print('invalid login')            