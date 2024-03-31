"""CHECK WHETHER THE GIVEN DIGIT IS PRESENT IN A NUMBER OR NOT"""

def fun1(num, key):
    while num != 0:
        digit = num % 10
        if digit == key:
            return True
        num = num // 10
    return False

def fun2(num, key):
    return True if str(key) in str(num) else False

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    if n < 0:
        print("Please enter a positive number")
    else:
        k = int(input("Enter number to search: "))
        print(fun1(n, k))
        print(fun2(n, k))
    