"""NUMBER OF TRAILING ZEROS IN FACTORIAL OF THE GIVEN NUMBER"""

import math
def fun(num):
    if num < 0:
        return False
    f = math.factorial(num)
    fact_num = f
    count = 0
    while f != 0:
        if f % 10 != 0:
            break
        count += 1
        f = f // 10
    return fact_num, count
         
if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(f"Number: {n} \t Factorial: {fun(n)[0]} \t No of trailing zeros: {fun(n)[1]}")