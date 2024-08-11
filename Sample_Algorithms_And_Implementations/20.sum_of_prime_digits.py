"""SUM OF PRIME DIGITS"""

def fun(num):
    s = 0
    while num != 0:
        digit = num % 10
        if digit in (2,3,5,7):
            s += digit
        num = num // 10
    return s

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(fun(n))