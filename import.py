import urllib.request

try:
    textfile = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
except urllib.error.URLError as e:
    print("Failed to connect to the URL: ", e)
    exit()

with open('EntireLog.txt', 'w+', encoding='utf-8') as data:
    for line in textfile:
        strline = str(line, encoding='utf-8')
        data.write(strline + '\n')


