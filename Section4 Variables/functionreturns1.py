#Starting here i am using functions to stop the functionality of the code, to check something just uncomment the functions with 
#names like first, second, etc...
#Return exit a function and send back a value to the caller.
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
def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
def third():
    result = check_even(8)
    print(result)
# third()

def maximum_value(numbl):
    return max(numbl)

list_num=[1,2,5,9,0,10]
result = maximum_value(list_num)
print(result)
result = result**2
print(result)
