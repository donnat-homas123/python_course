import time
start=time.perf_counter()

num=[1,2,5,7,8,9,23,6,1,5]
solutn=[]
indexpotn=[]
target=7
for i in range(len(num)):
    ind1=num[i]
    for j in range(i+1,len(num)):
        ind2=num[j]
        for k in range(i+2,len(num)):
            ind3=num[k]
            sumof3=ind1+ind2+ind3
        if sumof3==target:
           indexpotn.append((i,j,k))
           solutn.append((ind1,ind2,ind3))
print('tuppled index soln of 7',indexpotn)  
print('tuppled values for soln of 7',solutn)
end=time.perf_counter()

print(end - start)