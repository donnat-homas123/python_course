num=[1,2,5,7,8,9,23,6,1,5]
solutn=[]
target=7
for i in range(len(num)):
    ind1=num[i]
    for j in range(i+1,len(num)):
        ind2=ind1+num[j]
        if ind2==target:
           solutn.append((i,j))
print('tuppled index soln of 7',solutn)           