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

def extractMData(webpage):
    soup = BeautifulSoup(webpage)
    info = divBlock[3]
   # divBlock = divContainer.findAll("div", {"class":"block"})
    getLeft = info.findAll("div", {"class":"info_left"})
    getRight = info.findAll("div", {"class":"info_right"})
    for i in range(0, len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        print textLeft + ": " + textRight
        
   # getLeft = info.findAll("div", {"class":"info_left"})
   # getRight = info.findAll("div", {"class":"info_right"})                               
    
   # print getLeft
   # print getRight                                

for member in members:
    #sTRIP <A> TAGS
    href = member.get("href")
    #Create url to open
    url = "http://inadaybooks.com/justiceleague/" + href
    #print url
    #open url
    mPage = urllib2.urlopen(url)
    extractMData(mPage)
    print mPage
    


# Results
# Team Name: The Justice League
# Alignment: Good
# Status: Active
# Members: 
# Aquaman (Arthur Curry)
#Batman (Bruce Wayne)
#Cyborg (Victor Stone)
#Element Woman (Emily Sung)
#Firestorm (Ronnie Raymond)
#Flash (Barry Allen)
#Superman (Clark Kent)
#Wonder Woman (Diana)
#Zatanna (Zatanna Zatara)
