list_e=[]
list_a=[]
for i in range(5):
    k=int(input())
    list_e.append(k)
    if list_e[i]%2==0 :
        list_a.append(list_e[i])
print(list_e)
print(list_a)  