"""PRIME NUMBER APPLICATION"""

def fun1(num):
    faactors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            faactors += 1
    return faactors == 2

def fun2(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("Enter any number: "))
    print(fun1(n))
    print(fun2(n))