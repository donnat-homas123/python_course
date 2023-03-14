file = open("num.txt",'r')
file_to_write=open("write.txt","w")
contents = file.readlines()

print(contents)

for element in contents: 
  
    if int(element.strip())%2==0:  
            file_to_write.write(element.strip()) 
            file_to_write.write("\t") 
            # print(element.strip())

file_to_write.close()
file.close()


with open("num.txt",'r') as doc:
      
      print(doc.readlines())
