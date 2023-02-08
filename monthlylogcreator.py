import re

entirelog = open('EntireLog.txt', 'r')

log = entirelog.read()
logAslist = log.splitlines()
print(logAslist[1]) #this is a test to see if the log becomes a list properly

pattern1 = "?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"

for i in logAslist:
    if(re.search(pattern1, i)):
        print("Date found")
    else:
        print("No date found")