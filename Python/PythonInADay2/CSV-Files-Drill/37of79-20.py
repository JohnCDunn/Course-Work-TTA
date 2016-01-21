import urllib2
from bs4 import BeautifulSoup

webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

#  Convert to BeautifulSoup

soup = BeautifulSoup(webpage)

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})

divBlock = divContainer.findAll("div", {"class":"block"})
print (divBlock)

# Results:
# [<div class="block">\n<div class="title">\n<h1>The Justice League</h1>\n</div>
# \n</div>, <div class="block">\n<p><blockquote>"Their founding members included Aquaman, Batman, Cyborg,.......
