"""PROGRAM TO FIND MAXIMUM OF TWO NUMBERS"""

def fun1(a,b):
    if a > b:
        return a
    else:
        return b
    
def fun2(a,b):
    return a if a < b else b

def fun3(a,b):
    return max(a,b)

if __name__ == '__main__':
    a = int(input('Enter a value:'))
    b = int(input('Enter a value:'))
    print(fun1(a,b))
    print(fun2(a,b))
    print(fun3(a,b))
    
    