users={'user1':'pass'}

username=input('enter username')
if username in users:
    password=input('enter the password')
    correctpassword=users[username] #pass

    if correctpassword == password:
        print('entered the correct details')
    else:
        print('invalid password')
else:
    print('invalid username')            