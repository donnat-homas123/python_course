import time
start=time.perf_counter()
map={}
numbers=[1,5,3,4,2,6]
target=7
soln=[]

for i in range(len(numbers)):
    if target-numbers[i] in map:
        soln.append((map[target-numbers[i]],i))
    else:
        map[numbers[i]]=i
print(soln)
end=time.perf_counter()
print(end - start)        