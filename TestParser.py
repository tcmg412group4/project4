import re                                                                                       # imports package to use python regular expressions

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")              # Date Pattern in regex form specified for the date format found in the log

data = open('EntireLog.txt', 'r')                                                               # imports the file that contains the data
log = data.readlines()                                                                          # reads the entire log file line by line
matches = []                                                                                    # empty list to hold any matches we get when parsing for the Date pattern
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

for line in log:                                                                                
    x = re.search(pattern, line)                                                               
    if x == None:                                                                            
        errorlog.append(line)
        
    date = x.group()

    if date.find("Oct/1994") != 1:
        oct94.append(line)
    elif date.find("Nov/1994") != 1:
        nov.append(line)              
        
data.close()
print(len(oct94))

