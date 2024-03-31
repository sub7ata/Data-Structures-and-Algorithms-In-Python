"""EXTRACTING DIGITS FROM THE GIVEN NUMBER"""

def fun(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count
        
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Number: {n} and number of digits: {fun(n)}")