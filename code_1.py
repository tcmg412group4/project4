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
    

for i in matches:                                                                               # for loop for finding dates in logs and then appends them to corresponding list
                                                                                                # and writes the log into a corresponding .txt file
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

# above portion will write logs into monthly text files, which will then be used to gather more data


with open('October94.txt', 'r') as oct_94:
    x = len(oct_94.readlines())
    print('October 1994 Total:', x)

with open('November.txt', 'r') as nov:
    x = len(nov.readlines())
    print('November 1994 Total:', x)

with open('December.txt', 'r') as dec:
    x = len(dec.readlines())
    print('December 1994 Total:', x)

with open('January.txt', 'r') as jan:
    x = len(jan.readlines())
    print('January 1995 Total:', x)

with open('February.txt', 'r') as feb:
    x = len(feb.readlines())
    print('February 1995 Total:', x)

with open('March.txt', 'r') as mar:
    x = len(mar.readlines())
    print('March 1995 Total:', x)

with open('April.txt', 'r') as apr:
    x = len(apr.readlines())
    print('April 1995 Total:', x)

with open('May.txt', 'r') as may:
    x = len(may.readlines())
    print('May 1995 Total:', x)

with open('June.txt', 'r') as jun:
    x = len(jun.readlines())
    print('June 1995 Total:', x)

with open('July.txt', 'r') as jul:
    x = len(jul.readlines())
    print('July 1995 Total:', x)

with open('August.txt', 'r') as aug:
    x = len(aug.readlines())
    print('August 1995 Total:', x)

with open('September.txt', 'r') as sep:
    x = len(sep.readlines())
    print('September 1995 Total:', x)

with open('October95', 'r') as oct95:
    x = len(oct95.readlines())
    print('October 1995 Total:', x)

# some variables
allreq = 0
bad = 0
good = 0
records = {}


# open file again, name it data 
with open('EntireLog.txt') as data:
    L = data.readlines()                
    for x in L:
        allreq += 1
        if '403 -' in x or '404 -' in x:                #search for errors
            bad += 1
        if '302 -'in x:                                 #search for redirects
            good += 1
        seq = re.split("[A-Z]{3,5} (.+) HTTP/1.0", x)           #pattern to filter the 'GET..." only
        if len(seq) == 3:
            file = seq[1]                               #index the names of the files
            if file in records:                         #count and store it in a dictionary
                records[file] += 1
            else:
                records[file] = 1

    dec = good / allreq
    perc = "{:.0%}".format(dec)                         #convert to percent
    decc = (bad / allreq)
    perc2 = "{:.0%}".format(decc)                       #convert to percent
        

# for questions 3 and 4
print("unsuccessful requests = ",perc)                  # I feel like my numbers are wrong. Please double check for both
print("redirected requests = ",perc2)


# for questions 5 & 6
sorted_d = dict( sorted(records.items(), key=operator.itemgetter(1),reverse=True))        # descending order
print(("Most requested: " + list(sorted_d.keys())[0]))                                           #turn to list, index the 1st key
print("Least requested: " + list(sorted_d.keys())[-1])                                  #turn to list, index the last key
