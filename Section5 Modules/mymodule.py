#many modules liek math random datetime, os sys json, re time
import math
import os
import sys

#Calculate the squary root of a number
sqrt_value = math.sqrt(16)
fctl_value = math.factorial(5)



# print(f"Square root of 16 is : {sqrt_value}")

#get the current working directory
#be careful os.getcwd() may work differently if not used with the terminal
current_directory = os.getcwd()
# print(current_directory)
#list of files
files = os.listdir(".")
# print(f"Files in the current directory: {files}")
version = sys.version
# print(version)
def printcmdargs(inputdata):
    for data in inputdata:
        print(data)

printcmdargs(sys.argv)



#"C:\Users\Benjamin_Rodriguez\Desktop\PythonCode\repos\anotherrepo\pythontestEasy"
#  ~/Section1/s1.py
# cd /; python C:\Users\Benjamin_Rodriguez\Desktop\PythonCode\repos\anotherrepo\pythontestEasy\'Section5 Modules'\mymodule.py
# cd C:\Users\Benjamin_Rodriguez\Desktop\PythonCode\repos\anotherrepo\pythontestEasy\'Section5 Modules'