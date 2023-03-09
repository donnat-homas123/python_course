name=input('enter ur name')

alpha={}
for i in name:
    alpha[i] = 0
for i in name:
    j = alpha[i]
    if i in alpha:
        j=j+1       
    else:
        j=1       
    alpha[i]=j
print(alpha)