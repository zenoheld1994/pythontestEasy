#CLI arguments in python enables you to pass arguments to a program 
#we execute the followign command python script.py arg1 arg2 arg4
#after script.py those are command line arguments
#with sys module you can access those arguments import sys
#sys.argv[0] sys.argv[1] and so on
#Simple Script to add two numbers
def add(a, b):
    return a + b

# Calling the Function
output = add(10, 15)
print(output)