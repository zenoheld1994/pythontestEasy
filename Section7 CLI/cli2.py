import sys


print("Oh boy you passed a lot of arguments!",len(sys.argv))
index =0
for argument in sys.argv:
    print(f"Argument#{index} is {argument}")
    index=index+1
#printthescript name
print("Scriptname: ",sys.argv[0])