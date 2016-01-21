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
    print member.get("title")

print members

# Results
#
