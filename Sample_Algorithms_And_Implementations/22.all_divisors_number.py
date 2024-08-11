"""FIND ALL THE DIVISORS OF A NUMBER"""

def fun(num):
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(fun(i))