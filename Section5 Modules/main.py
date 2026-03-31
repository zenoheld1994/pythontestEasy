#import it
import custom_module

#Use the functions and variable from my own module
name = "Ben"
greeting = custom_module.greet(name)
print(greeting)
num1=5
result = custom_module.add(num1,custom_module.my_variable)
print(f"Addition: {num1} + {custom_module.my_variable} = {result}")

# print(cus)
