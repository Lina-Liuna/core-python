import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url = "https://mojim.com/%E9%BB%83%E9%9C%91.html?t4"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(2,len(soup.findAll('a'))+1, 2): #'a' tags are for links
#for i in range(2,6, 2): #'a' tags are for links
    #print("i = " + str(i))
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'https://mojim.com'+ link

    #ßprint("download url = " + str(download_url))
    #newurl = urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    #print(newurl)
    response = requests.get(download_url)
    updatesoup = BeautifulSoup(response.text, "html.parser")
    #print(updatesoup.head.contents[6])
    mystr = str(updatesoup.head.contents[6])
    print("\n")
    print(re.findall('"([^"]*)"', mystr)[0])
    print("\n")
    #print(updatesoup.prettify())
    #time.sleep(1) #pause the code for a sec