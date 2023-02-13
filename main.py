## this will be our main python file, which will house the final code for this project

import re                                                                                       # imports package to use python regular expressions

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?")              # Date Pattern ##/MMM/#### in regex form specified for the date format found in the log

data = open('EntireLog.txt', 'r')                                                               # imports the file that contains the data
log = data.readlines()                                                                          # reads the entire log file line by line
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
                                                                                                # create text files for individual months
october94 = open("October94.txt", "w+")
november = open("November.txt", "w+")
december = open("December.txt", "w+")
january = open("January.txt", "w+")
february = open("February.txt", "w+")
march = open("March.txt", "w+")
april = open("April.txt", "w+")
May = open("May.txt", "w+")
june = open("June.txt", "w+")
july = open("July.txt", "w+")
august = open("August.txt", "w+")
september = open("September.txt", "w+")
october95 = open("October95", "w+")
errorLog = open("ErrorLog.txt", "w+")


for line in log:                                                                                # for loop for parsing through text file line by line 
    x = re.search(pattern, line)                                                                # searches each line for the Date pattern
    if x != None:                                                                               # if it doesnt find the date pattern on a line, that means its an error log or something else
        matches.append(line)                                                                    # appends the line to the matches list     
    else:
        matches.append(line)                                                                    # If a date pattern is found, the Date is added to the matches list as a string
        

print(matches[128])                                                                             # test to print the line

for i in matches:

    if i.find('Oct/1994') != -1 :
        oct94.append(i)
        october94.write(i + '\n')
    elif i.find('Nov/1994') != -1 :
        nov.append(i)
        november.write(i + '\n')
    elif i.find("Dec/1994") != -1 :
        dec.append(i)
        december.write(i + '\n')
    elif i.find("Jan/1995") != -1 :
        jan.append(i)
        january.write(i + '\n')
    elif i.find("Feb/1995") != -1 :
        feb.append(i)
        february.write(i + '\n')
    elif i.find("Mar/1995") != -1 :
        mar.append(i)
        march.write(i + '\n')
    elif i.find("Apr/1995") != -1 :
        apr.append(i)
        april.write(i + '\n')
    elif i.find("May/1995") != -1 :
        may.append(i)
        May.write(i + '\n')
    elif i.find("Jun/1995") != -1 :
        jun.append(i)
        june.write(i + '\n')
    elif i.find("Jul/1995") != -1 :
        jul.append(i)
        july.write(i + '\n')
    elif i.find("Aug/1995") != -1 :
        aug.append(i)
        august.write(i + '\n')
    elif i.find("Sep/1995") != -1 :
        sep.append(i)
        september.write(i + '\n')
    elif i.find("Oct/1995") != -1 :
        oct95.append(i)
        october95.write(i + '\n')
    elif i.find("local 780") != -1 :                    #not sure how to append error log to proper month lists
        errorlog.append(i)
        errorLog.write(i + '\n')
    elif i.find("local      index.html") != -1 :
        errorlog.append(i)
        errorLog.write(i + '\n')
                                                        # program works, splits logs into monthly files after being run, all except the error logs. Not sure
                                                        # about how to add the error logs to the proper month when the program is parsing through the entire log file. 

