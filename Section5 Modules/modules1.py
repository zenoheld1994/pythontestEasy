#modules are files that contain python code, with functions, classes, variables and can include runnable code
#Help organizing and reusing code across different programs
#why use
#Code reusability
#Organization it is easier to manage

#Types of Modules
#Built-in Modules: come with python like math, os, sys
#User-defined MOdules: you create for you
#example
import math
result = math.sqrt(16)
print(result)
#the module is imported to use its sqrt() function

# User-defined example
# mymodule.py
def add(a,b):
    return a+b
def greet(name):
    print(f"Hello, {name}")

# main.py
#import custom module
# import mymodule
# Use functions from the module
#greeting = mymodule.greet("ben")
greeting = greet("ben") 
#sum_result=mymodule.add(5,5)
sum_result=add(5,5)
print(greeting)
print(print(greeting))