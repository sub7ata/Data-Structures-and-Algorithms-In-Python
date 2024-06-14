"""Example: 1"""
def fun(a, b):
    '''this function is used for calculating addition of two numbers'''
    print(a + b)

if __name__ == '__main__':
    fun(10, 20)
    print(fun.__doc__)
    

"""Example: 2"""
import math
print(math.factorial(5))
print(math.factorial.__doc__)
