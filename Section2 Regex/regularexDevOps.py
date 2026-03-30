#Used for parsing log files, validating input data, searching and replacing text in config files and extracting
#specific information from text

#When the system is having issues, based on the logs of the system you may know
#find lines that have error or warning use a regex in python
pattern = r"(WARNING|ERROR)"

logfilepath = "path"
#use a for line in file

#use of re.search 
#print(line.strip()) print lines without extra spaces
