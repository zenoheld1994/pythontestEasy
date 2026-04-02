'''
operators there are :
1. Arithmetic
2. Comparison
3. Logical
4. Assignment  (+=,-=)
5. identity (is, is not)
6. membership (in, not in)
7. Bitwise (&,|,^,~,<<,>>) (AND,OR,SOR,NOT,zero fill left shift, signed right shift)
'''
#in operator
fruits = ["apple", "banana", "cherry"]
#prints True
print("banana" in fruits)
#prints False
print("banaXXna" in fruits)
#prints False
print("banana" not in fruits)

#identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)