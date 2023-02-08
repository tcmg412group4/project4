import urllib.request

textfile = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")

data = open('EntireLog.txt','w+')

for line in textfile:
    strline = str(line)
    data.write(strline + '\n')
    

data.close()

