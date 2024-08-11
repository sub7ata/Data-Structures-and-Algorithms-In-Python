"""PROGRAM TO FIND MAXIMUM OF FOUR NUMBERS"""

def fun1(a,b,c,d):
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
        return b    
    elif c > d:
        return c 
    else:
        return d

def fun2(a,b,c,d):
    return a if a > b and a > c and a > d else b if b > c and b > d else c if c > d else d 

def fun3(a,b,c,d):
    return max(a, b, c, d)

if __name__ == "__main__":
    a = int(input('Enter the Value of A: '))
    b = int(input('Enter the Value of B: '))    
    c = int(input('Enter the Value of C: '))    
    d = int(input('Enter the Value of D: '))    
    
    print(fun1(a, b, c, d))
    print(fun2(a, b, c, d))
    print(fun3(a, b, c, d))
    