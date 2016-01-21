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

print members

# Results
# [<a href="people/aquaman.html" title="Aquaman">Aquaman (Arthur Curry)</a>...
