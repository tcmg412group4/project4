import re

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")

#pattern is adjusted to format used in the log file

data = open('EntireLog.txt', 'r')
log = data.readlines()
matches = {}

for line in log:
    print(pattern.search(line))
data.close()

# above portion searches the entirelog.txt file and searches for the Date pattern in each line 