num=[1,2,5,7,8,9,23,6,1,5]
for i in range(len(num)):
    u=num[i]
    print('num in i th index is',num[i])
    print('num after i th num in list')
    for j in range(i+1,len(num)):
        print(num[j])