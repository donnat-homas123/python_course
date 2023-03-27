a=[23,45,12,92]
k=a[0]
for i in range(4):
    if a[i]>=k:
        k=a[i]
print('largest num is',k)