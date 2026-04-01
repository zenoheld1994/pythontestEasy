import sys

#Writing functions for add, sub & multiplication

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
operator = sys.argv[2]
result=0
if operator=='add':
    result = add(num1,num2)
    print(result)
elif operator=='sub':
    result = sub(num1,num2)
    print(result)
elif operator=='mult':
    result = mult(num1,num2)
    print(result)
else:
    print("type a correct operator add, sub or mult")