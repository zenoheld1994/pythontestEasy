import re
text = "Hello how are you \
    My name is Benjamin Rodriguez \
        I love python \
            I hope you enjoy learning python and everything else with me !!!!"
#pattern = r"python"
#re.findall finds all the occurences within the string and returns those words
#result = re.findall(pattern,text)
#print(result)
#re.sub replaces the matches with a given string useful for scripts that need to be changed
text0= "Python    is    amazing and thats it ttttttt"
pattern = r"t+t"
result = re.sub(pattern,"puto" ,text0)
print(result)
