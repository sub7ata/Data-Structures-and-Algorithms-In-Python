"""TRIBANACCI SEQUENCE"""

def fun(num):
    lst = []
    a = -1
    b = 0
    c = +1
    for i in range(num):
        d = a + b + c
        lst.append(d)
        a = b
        b = c
        c = d
    return lst

if __name__ == '__main__':
    n = int(input("Enter the number for tribanocci number: "))
    print(fun(n))