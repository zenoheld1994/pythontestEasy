import random
import datetime
import re

# randomfloat = random.random()
# randominteger = random.randint(20,100)
# print(randomfloat,randominteger)

# print(datetime.now().strftime("%d/%m/%Y, %H:%S"))

text = "whatever this is"
pattern = r"this"
uppertext = text.upper()
haspattern = False
subtext = "this" in text
if(subtext != None):
    haspattern = True
print(f"Basic string:{text}, converted to uppercase: {uppertext} and Does it contain the following substring(this)? : {haspattern}")
