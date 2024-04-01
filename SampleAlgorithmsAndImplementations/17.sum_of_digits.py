"""SUM OF DIGITS"""

def fun1(num):
    s = 0
    while num != 0:
        digit = num % 10
        s += digit
        num = num // 10
    return s

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(f"Sum of digits: {fun1(n)}")