us_ername={}
print('enter username of 3 people')
for i in range(3):
    username=input('enter the username')
    pass_word=input('enter the password')
    us_ername[username]=pass_word
    #print (us_ername)

print(us_ername)

#do not allow the user to use an already existing username
#ask for username and passwrd and print them if present