#Functions are reusable
#help organize and manage code by encapsulating tasks into manageable secitons
#THey can take inputs, perform operations and return outputs
#THey have function definition with def 
#Name of the function after def
#close with ()
#inside () optional inputs and then :
#function body
#return statement

#advantages 
#Reusable
#Readability 
#Abstraction track  a large python program when is big
#Maintanability
#Testing
def simple():
    print("Hello World")

# simple()
def greet(name, age):
    #you have to put f with {} variables to get the variables value
    print(f"hello, {name} ! you are {age}")

# greet("Benjamin",32)
def add(a,b):
    return a+b
num1=5
num2=5
result =add(num1,num2)
print(f"The sum is:{result}")
#this works too
# print(add(num1,num2))