"""IMPLEMENT A PROGRAM TO FIND X TO THE POWER Y"""

def fun1(x, y):
    temp = 1
    for i in range(y):
        temp *= x
    return temp

def fun2(x, y):
    import math
    return int(math.pow(x, y))

def fun3(x, y):
    return x**y

if __name__ == '__main__':
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    print(fun1(a, b))
    print(fun2(a, b))
    print(fun3(a, b))
    
    