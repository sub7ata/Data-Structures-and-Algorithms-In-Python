"""PERFECT NUMBER OR NOT"""

def fun(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s==num

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        if fun(i):
            print(i)