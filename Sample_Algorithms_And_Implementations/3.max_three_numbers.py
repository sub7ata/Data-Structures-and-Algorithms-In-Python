"""PROGRAM TO FIND MAXIMUM OF THREE NUMBERS"""

def fun1(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    
def fun2(a, b, c):
    return a if a > b and a > c else b if b > c else c

def fun3(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))
    c = int(input("Enter the value of c :"))
    print(fun1(a, b, c))
    print(fun2(a, b, c))
    print(fun3(a, b, c))
    
    