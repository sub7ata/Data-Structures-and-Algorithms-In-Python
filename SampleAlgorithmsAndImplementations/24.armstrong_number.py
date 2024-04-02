"""ARMSTRONG NUMBER OR NOT"""

def fun(num):
    s = 0
    while num != 0:
        digit = num % 10
        s = s + digit**3
        num = num // 10
    return s
        
if __name__ ==  "__main__":
    n = int(input("Enter a number: "))
    for i in range(n):
        if i == fun(i):
            print(i)