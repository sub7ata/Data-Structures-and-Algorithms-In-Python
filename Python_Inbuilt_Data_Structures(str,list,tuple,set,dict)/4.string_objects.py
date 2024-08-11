# """Creation of string objects  in python"""
# '''
# 1. single quotes
# 2. double quotes
# 3. triple single quotes
# 4. triple double quotes
# 5. input() function
# 6. str() type casting function
# 7. eval() function
# '''

# """Example: 1"""
# obj = input("Enter any object: ")
# print(obj)
# print(type(obj))

# """Example: 2"""
# obj1= 222
# obj2= str(obj1)
# print(obj1, type(obj1))
# print(obj2, type(obj2))

# """Example: 3"""
# obj = eval(input("Enter any object: "))
# print(obj, type(obj))


# """Accessing string objects"""
# '''
# 1. directly
# 2. index concept
# 3. slice operator
# 4. while loop
# 5. for each loop
# '''

# """Example: 1"""
# s = "ijklmnop"
# print(s, type(s))
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[6])
# print(s[7])


# """Example: 2"""
# s = "wxyz"

# index = 0
# while index < len(s):
#     print(f'index: {index} character: {s[index]}')
#     index += 1
    

# """Example: 3"""
# s = "wxyz"

# index = -1
# while index >= - len(s):
#     print(f'index: {index} character: {s[index]}')
#     index -= 1
    
# """for each loop"""
# """Example: """
# s = "incident"

# print(s)
# for i in s:
#     print(i)

"""Slice Operator"""
'''
version1: s[startIndex: endIndex] ---------------> startIndex to endIndex -1
version2: s[startIndex: endIndex: stepValue] ----> startIndex to stepValue -1 with step
'''

"""Example: 1"""
s = "abcdefghijklmnopqrstuvwxyz"
print(s)
print(s[0:26])
print(s[0:len(s)])
print(s[5:8])

"""Example: 2"""
s = "abcdefg"
print(s)
print(s[-7:-4])
print(s[-1:-4])

"""Example: 3"""
s = "abcdefg"
print(s)
print(s[0:7:1])
print(s[0:7:2])
print(s[0:7:3])
print(s[0:7:4])


"""The default values in forward direction"""
'''
1. default value for start: 0
2. default value for end: len(s)
3. default value for step: 1
'''

"""Example: 1"""
s = "abcdefg"
print(s)
print(s[0:7:1])
print(s[:7:1])
print(s[0::1])
print(s[0:7:])
print(s[::])


"""Example: 2"""
s = "abcdefg"
print(s)
print(s[-1:-8:-1])
print(s[-1:-8:-2])
print(s[-1:-8:-3])
print(s[-3:-8:-1])

print(s[-1:-8:-1])
print(s[-1:-8:+1])
print(s[-4:-2:+1])


"""The default values backward direction"""
'''
1. default value for start: -1
2. default value for end: -(len(s)+1)
3. default value for step: No default for step
'''

"""Example: 1"""
s = "abcdefg"
print(s)
print(s[-1:-8:-1])
print(s[:-8:-1])
print(s[-1::-1])
print(s[-1:-8:])

"""Example: 2"""
s = "abcdefg"
print(s[::])
print(s[::-1])




