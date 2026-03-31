#local and global variables
#local defined inside a function and only accesible within the function

#Global variables that are defined outside any function and are accesinble throughout the code. including inside functions

def myfuncion():
    print("inside the function")

# myfuncion()


def addition():
    num1 = 40
    num2 = 30
    print(num1+num2)

addition()

def substraction():
    num1 = 50
    num2 = 30
    print(num1 - num2)

substraction()