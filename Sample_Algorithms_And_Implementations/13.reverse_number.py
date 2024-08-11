"""REVERSE THE GIVEN NUMBER"""

def fun1(num):
    temp = 0
    while num != 0:
        digit  = num % 10
        temp = (temp * 10) + digit
        num = num // 10
    return temp

def fun2(num):
    return str(num)[::-1]

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print(fun1(n))
    print(fun2(n))