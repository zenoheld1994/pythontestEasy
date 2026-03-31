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


global_var= 32 #myage

def print_global_variables():
   print(global_var)

def modify_global_variable():
    global global_var
    global_var = 33
    print(global_var)

modify_global_variable()
print_global_variables()

student = {
    "name":"Benek",
    "last_name":"Don",
    "age":90,
    "height":171.5,
    "pro":True
}
student["GPA"]=80
student["age"]=9
# print("GPA is",student["GPA"],"age is:",student["age"])
for key in student:
    print(key+":",student[key])
#different way
for key,value in student.items(): #items
    print(f"{key}:{value}")
#also possibe
for key, value in student.items():
    print(key, ":", value)