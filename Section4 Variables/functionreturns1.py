#Return exit a function and send back a value to the claler.
#When return is found inside a function the function stops and returns the value to the caller
#if no value is specified the function returns None
#We always use a return inside a function
def add(a,b):
    return a+b
    print("THis won't be printed")
#you need to put the function in a variable
def first():
    result = add(5,3)
    print(result)
# first()
#return multiple values with a function
def get_details():
    name = "Jai"
    age = 30
    return name,age
#returns a tuple
def second():
    details = get_details()
    #returns a tuple, you may use type keyword to print the type of the variable
    print(details)

# second()
