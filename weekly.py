import re
import operator

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")              # Date Pattern ##/MMM/#### in regex form specified for the date format found in the log

with open('EntireLog.txt', 'r') as data:                                                        # imports the file that contains the data
    log = data.readlines()                                                                      # reads the entire log file line by line
matches = [] 

                                                                                                # create empty lists to hold daily logs
oct94 = []
nov = []
dec = []
jan = []
feb = []
mar = []
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
oct95 = []
errorlog = []

for line in log:                                                                                # for loop for parsing through text file line by line 
    x = re.search(pattern, line)                                                                # searches each line for the Date pattern
    if x != None:                                                                               # if it doesnt find the date pattern on a line, that means its an error log or something else
        matches.append(line)                                                                    # appends the line to the matches list     
    else:
        matches.append(line)                                                                    # If a date pattern is found, the Date is added to the matches list as a string
    
dailydictionary = {}
for line in open("EntireLog.txt"):
    date = re.search(pattern, line)
    
    if date:
        day = date.group()
        if day in dailydictionary:
            dailydictionary[day] += 1
        else:
            dailydictionary[day] = 1

s = 0
for value in dailydictionary.values():
    s += value

s = s / len(dailydictionary)

print("There was an average of", s, "requests made each day")

