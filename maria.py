import re

# some variables
allreq = 0
all94 = 0
all95 = 0
bad = 0
good = 0



# open file again, name it data 
with open('EntireLog.txt') as data:
    L = data.readlines()
    for x in L:
        allreq += 1
        if '403 -' in x or '404 -' in x:
            bad += 1
        if '302 -'in x:
            good += 1
    dec = good / allreq
    perc = "{:.0%}".format(dec)
    decc = (bad / allreq)
    percent = "{:.0%}".format(decc)

print("unsuccessful requests = ",percent)
print("redirected requests = ",perc)

# I feel like my numbers are wrong :( but the code works