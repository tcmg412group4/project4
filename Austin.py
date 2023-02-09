import re                                                                                       # imports package to use python regular expressions

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")              # Date Pattern ##/MMM/#### in regex form specified for the date format found in the log

data = open('EntireLog.txt', 'r')                                                               # imports the file that contains the data
log = data.readlines()                                                                          # reads the entire log file line by line
matches = [] 

                                                                                   # empty list to hold any matches we get when parsing for the Date pattern

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

for line in log:                                                                                # for loop for parsing through text file line by line 
    x = re.search(pattern, line)                                                                # searches each line for the Date pattern
    if x != None:                                                                               # if it doesnt find the date pattern on a line, that means its an error log or something else
        matches.append(line)                                                                    # appends the string "Error or No Log" to the matches list     
    else:
        matches.append(line)                                                                    # If a date pattern is found, the Date is added to the matches list as a string
        
data.close()

print(matches[128])                                                                             # prints the line

for i in matches:

    if i.find('Oct/1994') != -1 :
        oct94.append(i)
    elif i.find('Nov/1994') != -1 :
        nov.append(i)
    elif i.find("Dec/1994") != -1 :
        dec.append(i)
    elif i.find("Jan/1995") != -1 :
        jan.append(i)
    elif i.find("Feb/1995") != -1 :
        feb.append(i)
    elif i.find("Mar/1995") != -1 :
        mar.append(i)
    elif i.find("Apr/1995") != -1 :
        apr.append(i)
    elif i.find("May/1995") != -1 :
        may.append(i)
    elif i.find("Jun/1995") != -1 :
        jun.append(i)
    elif i.find("Jul/1995") != -1 :
        jul.append(i)
    elif i.find("Aug/1995") != -1 :
        aug.append(i)
    elif i.find("Sep/1995") != -1 :
        sep.append(i)
    elif i.find("Oct/1995") != -1 :
        oct95.append(i)
    

print(len(oct94))
print(len(nov))
print(len(dec))


