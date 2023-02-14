import re 

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")              # Date Pattern ##/MMM/#### in regex form specified for the date format found in the log

data = open('EntireLog.txt', 'r')                                                               # imports the file that contains the data
log = data.readlines()                                                                          # reads the entire log file line by line
matches = [] 

for line in log:                                                                                # for loop for parsing through text file line by line 
    x = re.search(pattern, line)                                                                # searches each line for the Date pattern
    if x != None:                                                                               # if it doesnt find the date pattern on a line, that means its an error log or something else
        matches.append(line)                                                                    # appends the line to the matches list     
    else:
        matches.append(line)  

print("Enter the date in DD/MMM/YYYY for which you'd like to view number of requests. \n ")
ui = input("Date:  ")

x = 0
for i in matches:
    if i.find(ui) != -1:
        x = x + 1

print("There were ", x, " requests made on ", ui)

print( "Please enter the first 3 letters of the month you'd like to view data for. For example, January = Jan, February = Feb, etc.")
print( "If you are attempting to view data for October, please specify the year as follows: Oct/1994 or Oct/1995")
month_ui = input(" Month: ")

z = 0
for y in matches:
    if y.find(month_ui) != -1:
        z = z + 1
    
print ("There were ", z, "requests made in the month:", month_ui)

