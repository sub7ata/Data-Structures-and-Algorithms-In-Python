"""STRONG NUMBER OR NOT"""

import math
def fun(num):
    s = 0
    while num!=0 :
        digit = num % 10
        s = s+math.factorial(digit)
        num = num // 10
    return s

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        if i == fun(i):
            print(i)