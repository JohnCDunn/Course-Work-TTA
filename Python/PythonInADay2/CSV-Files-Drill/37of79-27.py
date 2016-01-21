import urllib2
from bs4 import BeautifulSoup

webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

#  Convert to BeautifulSoup

soup = BeautifulSoup((webpage), "html.parser")

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})

divBlock = divContainer.findAll("div", {"class":"block"})

divSep = divBlock[3].findAll("div", {"class":"separator"})

members = divSep[3].findAll("a")

for member in members:
    print ( member.get("href"))

print (members)

# Results
#people/aquaman.html
#people/batman.html
#people/cyborg.html
#people/elementwoman.html
#people/firestorm.html
#people/flash.html
#people/superman.html
#people/wonderwoman.html
#people/zatanna.html
#[<a href="people/aquaman.html" ti
