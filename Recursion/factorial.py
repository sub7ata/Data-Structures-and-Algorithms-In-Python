def iterative_factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact += number
    return fact

def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number - 1)

if __name__ == '__main__':
    element = int(input("Enter the number for the factorial: "))
    print(f"Factorial number using iterative: {recursive_factorial(element)}")
    print(f"Factorial number using recursive: {recursive_factorial(element)}")