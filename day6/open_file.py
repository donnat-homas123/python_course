file = open("num.txt",'r')
contents = file.readlines()

# print(contents)
for element in contents: 
  
    if int(element.strip())%2==0:   
            print(element.strip())

# contents =contents.split(',')
# "pTTHON COADING".split()
           