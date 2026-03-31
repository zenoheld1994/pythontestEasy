#local and global variables
#local defined inside a function and only accesible within the function

#Global variables that are defined outside any function and are accesinble throughout the code. including inside functions
#Global 
num1 = 300
num2 = 100
def myfuncion():
    print("inside the function")

# myfuncion()

#functions take the value of local variables if they are defined inside the function
#you can use the function global to put it as a value in the local one
def addition():
    #num1= num1+50 # this gives an error
    num1 = 50 #This does not
    num2 = 20
    print(num1+num2)

addition()

def substraction():

    print(num1 - num2)

substraction()


