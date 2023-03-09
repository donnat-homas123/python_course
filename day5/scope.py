x=10
def change_value(x):   #x=20 not returned 
    x=20

x=change_value(x)
print(x)    #here output is 10 not 20 

x=10
def change_value(x):   #x=20 returned 
    x=20
    return x
    print('hello')   #hello not printed anything after return command not executed

x=change_value(x)
print(x)    #here output is 20  

def fn2():
    print('this is fn2 ')
    def a():
        print('hi all')
    a()
fn2()    