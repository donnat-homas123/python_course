def add(x,y):
    return x+y

def sub(x,y):
    return x-y
k=input('enter + to add or - to substract')
a=int(input('enter first num'))
b=int(input('enter second num'))
if k=='+':
    result=add(a,b)
    print(result)
elif k=='-':
    result=sub(a,b)  
    print(result)  
else:
    print('invalid entry')


        