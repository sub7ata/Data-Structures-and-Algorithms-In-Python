"""PROGRAM TO PRINT FACTORIAL OF THE GIVEN NUMBER"""

import math
def fun1(n):
    if n < 0:
        return "Please enter a valid number."
    return math.factorial(n)

def fun2(n):
    if n < 0:
        return "Please enter a valid number."
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

def fun3(n):
    if n < 0:
        return "Please enter a valid number."
    elif n == 0:
        return 1
    return n *  fun3(n - 1)


if __name__ == '__main__':
    n = int(input("Enter the number for generating factorial number:"))
    print(fun1(n))
    print(fun2(n))
    print(fun3(n))
    
