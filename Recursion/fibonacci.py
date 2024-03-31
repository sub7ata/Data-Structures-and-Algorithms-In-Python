def iterative_fibonacci(number):
    first_number = 0
    second_number = 1
    if number < 0:
        return f"{number} is a invalid number for the fibonacci number."
    elif number == 0:
        return 0
    elif number == 1:
        return second_number
    else:
        for i in range(1, number):
            third_number = first_number + second_number
            first_number = second_number
            second_number = third_number
        return third_number
    
def recursive_fibonacci(number):
    if number < 0:
        return f"{number} is a invalid number for the fibonacci number."
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)

if __name__ == "__main__":
    number = int(input("Enter the number for the fibonacci: "))
    print("Fibonacci number using iterative: ", iterative_fibonacci(number))
    print("Fibonacci number using recursive: ", recursive_fibonacci(number))
    