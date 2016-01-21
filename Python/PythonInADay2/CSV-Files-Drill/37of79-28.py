import urllib2
from bs4 import BeautifulSoup

webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

#  Convert to BeautifulSoup

soup = BeautifulSoup(webpage)

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})

divBlock = divContainer.findAll("div", {"class":"block"})

divSep = divBlock[3].findAll("div", {"class":"separator"})

members = divSep[3].findAll("a")

for member in members:
    #sTRIP <A> TAGS
    href = member.get("href")
    #Create url to open
    url = "http://inadaybooks.com/justiceleague/" + href
    #print url
    #open url
    mPage = urllib2.urlopen(url)
    print mPage
    
   

# Results