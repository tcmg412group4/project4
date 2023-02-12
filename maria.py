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
#seq = re.split(".+\[(.+)\.+\]*\"(.+)\"*(\d{3})", x)
    for x in L:
        allreq += 1
        if '403 -' in x or '404 -' in x:
            bad += 1
        if '302 -'in x:
            good += 1
    dec = good / allreq
    perc = "{:.0%}".format(dec)
    decc = (bad / allreq)
    perc2 = "{:.0%}".format(decc)
    
    seq = re.split(".+\[(.+).+]*\"(A-Z)*(.+) (.+)\" ([0-9]{3})", x)
    file = seq[2]
    fname = {}
    if file in fname:
        fname[file] += 1
    else:
        fname[file] = 1
    

print("unsuccessful requests = ",perc)
print("redirected requests = ",perc2)
# print("Least requested: " + str(list(fname.keys())[-1]))



# I feel like my numbers are wrong :( but the code works