"""SUM OF N NATURAL NUMBERS"""

def fun1(num):
    return 0 if num <= 0 else (num * (num + 1)) // 2

def fun2(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s

def fun3(num):
    return 0 if num <= 0 else num + fun3(num - 1)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(fun1(n))
    print(fun2(n))
    print(fun3(n))
    