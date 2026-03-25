#Dictionary
#Unordered collection of key-value pairs each key is associated with a value
#Mutable you can add,update or delete key-value pairs
#Key features
#Keys must be unique and IMMUTABLE and can only be of type: strings, numbers or tuples
#Values any data Stirngs, lists or other dictionaries
my_dict = {
    "name":"Don",
    "last_name":"vergas",
    "age":1000,
    "Posotion":"todo we una verga para todo",
    "Salario":"infinito we"
}

# print("el wey:",my_dict)
# print("su nombre completo:",my_dict["name"],my_dict["last_name"])
my_dict["Salario"]="Infinito de orden superior"
my_dict["Que hace"]="Pues todo we"
# print("su salario alv...:",my_dict["Salario"])
print("todo:",my_dict)
#delete use the second value to be None so it returns None if it does nto find it
# my_dict.pop('age')
my_dict.pop('ae',None)
# del my_dict['age']
print("todo:",my_dict)