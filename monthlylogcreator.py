import re

entirelog = open('EntireLog.txt', 'r')

log = entirelog.read()
logAslist = entirelog.readlines()
#print(logAslist[1]) #this is a test to see if the log becomes a list properly

pattern1 = "([\d]{2}\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s[\d]{4})" #search pattern specified to date format on the log

for i in logAslist:
    if(re.search(pattern1, i) != None):
        print("Date found")
    else:
        print("No date found")