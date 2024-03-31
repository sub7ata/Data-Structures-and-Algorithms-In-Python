"""PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS EVEN OR ODD"""

def fun1(n):
    if n%2 == 0:
        return 'even'
    return 'odd'

def fun2(n):
    return 'even' if n%2 == 0 else 'odd'

def fun3(n):
    if n&1 == 0:
        return 'even'
    return 'odd'

if __name__ == '__main__':
    for i in range(0, 11):
        print(f"{i} is {fun1(i)} - {fun2(i)} -{fun3(i)} number")