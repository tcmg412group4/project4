import re                                                                                       # imports package to use python regular expressions

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")              # Date Pattern ##/MMM/#### in regex form specified for the date format found in the log

data = open('EntireLog.txt', 'r')                                                               # imports the file that contains the data
log = data.readlines()                                                                          # reads the entire log file line by line
matches = []                                                                                    # empty list to hold any matches we get when parsing for the Date pattern

for line in log:                                                                                # for loop for parsing through text file line by line 
    x = re.search(pattern, line)                                                                # searches each line for the Date pattern
    if x == None:                                                                               # if it doesnt find the date pattern on a line, that means its an error log or something else
        matches.append("Error or No Log")                                                       # appends the string "Error or No Log" to the matches list     
    else:
        matches.append(x)                                                                       # If a date pattern is found, the Date is added to the matches list as a string
        
data.close()

print(matches[130].group())
print(matches[130])                                                                             # test to see if it worked

