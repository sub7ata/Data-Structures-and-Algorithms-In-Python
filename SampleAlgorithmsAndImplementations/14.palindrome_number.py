"""PALINDROME NUMBER OR NOT"""

def fun1(num):
    r = 0
    while num != 0:
        digit = num % 10
        r = r * 10 + digit
        num = num // 10
    return r

def fun2(num):
    return int(str(num)[::-1])

if __name__ == '__main__':
    n = int(input("Enter a number for checking polidrome: "))
    print(n == fun1(n))
    print(n == fun2(n))

    if n == fun1(n) and n == fun2(n):
        print(f"{n} is a Palindrome Number. ")
    else:
        print(f"{n} is not a Palindrome Number. ")
    