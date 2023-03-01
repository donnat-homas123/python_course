a=int(input('enter first num'))
b=int(input('enter second num'))
c=input('enter + fpr add,- for sub,* for pdt and % for div')
if c=='+':
    print('sum is',a+b)
elif c=='-':
    print('diff is',a-b)
elif c=='*':
    print('pdt is',a*b)
elif c=='%':
    print('div is',a%b)
else:
    print('invalid input')                