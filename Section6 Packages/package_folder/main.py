#import the package (my_package)
import my_package

#use functions from package
result_add = my_package.add(5,5)
result_minus = my_package.substract(20,2)
bigstring = my_package.to_lower("pendejo")
smallstring = my_package.to_upper("hola")
print(result_add)
print(result_minus)
print(smallstring)
print(bigstring)
