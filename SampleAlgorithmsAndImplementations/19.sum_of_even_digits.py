"""SUM OF ODD DIGITS"""

def fun(num):
    s = 0
    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            s += digit
        num = num // 10
    return s

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(f"Sum of even digits: {fun(n)}")