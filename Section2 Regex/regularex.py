#Finding particular key items in logs with Regex
#Already provided functions with regular expressions
#Different ones like
# re.match() Determines if the regex matches at the beginning of the stirng
# re.search() Searches the string for a match and returns the first occurence
# re.findall() Returns a list of all matches in the sting
# re.sub() Replaces matches with a new string
#common special characters
# . Any character except newline
# ^ Start of string
# $ end of string
# * 0 or more occurences
# + 1 or more occurences
# [] character Set 
# | OR  
# \ Escape special characters
# \d Digit
# \w Word character
# \s whitespace
import re 
text = "hello world"
pattern = r"world"
#Only will find it, if it is at the beginning of the string try with world
result = re.search(pattern,text)
print(result.group())
# re.search will find the pattern across the whole string
#group returns the pattern found
# result = re.search(pattern,text)
# if result:
#     print(result.group())
# re.findall() will find all matches in the string, so it is useful for log files like for a particular message

