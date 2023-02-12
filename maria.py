import re

# some variables
allreq = 0
all94 = 0
all95 = 0
bad = 0
good = 0
seq = []

pattern = re.compile("[0-9]{2}[^a-zA-Z0-9]{1}[a-zA-Z]{3}[^a-zA-Z0-9]{1}[0-9]{4}?") 


# open file again, name it data 
with open('EntireLog.txt') as data:
    L = data.readlines()
    for x in L:
        allreq += 1
        if '403 -' in x or '404 -' in x:
            bad += 1
        if '302 -'in x:
            good += 1
        #seq = re.split(".+\[(.+)\]*\"(.+)\"*(\d{3})", x)
    dec = good / allreq
    perc = "{:.0%}".format(dec)
    decc = (bad / allreq)
    percent = "{:.0%}".format(decc)

print("unsuccessful requests = ",bad)
print("redirected requests = ",good)
print(pattern)



# I feel like my numbers are wrong :( but the code works