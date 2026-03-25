# Tuples
# Ordered collections of items
# THey can't be modified/they are immutable
# Script a tuple and there you have a few items
# TUples use ()
#  useful for configurations like:
db_config = ("localhost",5432,"admin","password")
# my_tuple=(1,2,3,4,5,6,7)
#print("my tuple:",my_tuple)
#Error
# my_tuple[0]=3
# print("my tuple:",my_tuple)
#Error
# my_tuple(1)=3
# print("my tuple:",my_tuple)

#if you need to modify only when you creat eit

#Sets
#Unordered collection of UNIQUE items
#remvoes duplicates 
#mutable but only ADD or REMOVE 
#uses curly braces
set_example={1,2,3,4,5,6,1}
print("my set:",set_example)
set_example.add(10)
set_example2={7}
#update accepts lists, tuples, or other sets
set_example.update(set_example2)
print("my set:",set_example)
#unique entries like IPs or user groups
# users={'192.168.161.5','192.168.161.5','usuario1','usuario1','verga'}
# print('seguridad:',users)
