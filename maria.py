import re
import operator

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
        seq = re.split("[A-Z]{3,5} (.+) HTTP/1.0", x)           #pattern to filter out the name of the file only
        if len(seq) == 3:
            file = seq[1]                               #index
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

print("Most requested: " + str(list(records.keys())[0]))
print("Least requested: " + str(list(records.keys())[-1]))
