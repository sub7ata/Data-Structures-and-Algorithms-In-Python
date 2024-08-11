"""PROGRAM TO SWAP GIVEN TWO INTEGER VALUES"""

def fun1(a,b):
    """by using temp variable"""
    print(f"Before swapping: a= {a}, b= {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a= {a}, b= {b}")
    
def fun2(a,b):
    """by using add and sub operations"""
    print(f"Before swapping: a= {a}, b= {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swapping: a= {a}, b= {b}")

def fun3(a,b):
    """by using mul and div operations"""
    print(f"Before swapping: a= {a}, b= {b}")
    a = a * b
    b = a // b
    a = a // b
    print(f"After swapping: a= {a}, b= {b}")

def fun4(a, b):
    """by using bitwise operators"""
    print(f"Before swapping: a= {a}, b= {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swapping: a= {a}, b= {b}")
    
def fun5(a, b):
    """by using single line"""
    print(f"Before swapping: a= {a}, b= {b}")
    a, b = b, a
    print(f"After swapping: a= {a}, b= {b}")
    
    
    
if __name__ == "__main__":
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    
    print(f"\n{fun1.__doc__}")
    fun1(a, b)
    
    print(f"\n{fun2.__doc__}")
    fun2(a, b)
    
    print(f"\n{fun3.__doc__}")
    fun3(a, b)
    
    print(f"\n{fun4.__doc__}")
    fun4(a, b)
    
    print(f"\n{fun5.__doc__}")
    fun5(a, b)
    
    
    
    