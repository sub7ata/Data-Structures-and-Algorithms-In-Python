"""EXTRACTING DIGITS FROM THE GIVEN NUMBER"""

def fun(num):
    if num < 0:
        print(f"{num} is negative number. Please try with positive numbers!")
    while num > 0:
        digit = num % 10
        print(digit)
        num = num // 10
        
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    fun(n)