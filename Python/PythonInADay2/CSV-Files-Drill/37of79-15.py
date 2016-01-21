import urllib2
from bs4 import BeautifulSoup

webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

print BeautifulSoup(webpage)

# Results:
#    <!DOCTYPE html>

#  <html>
#  <head>
#  <link href="style.css" rel="stylesheet" type="text/css"/>
#  <title>In A Day Books: Web Scraping</title>
#  </head>
#  <body>
#  <div id="container">
#  ...
#  ...
#  ...

#  <div class="info_left">Members</div>
#  <div class="info_right">
#  <p><a href="people/aquaman.html" title="Aquaman">Aquaman (Arthur Curry)</a></p>
#  <p><a href="people/batman.html" title="Batman">Batman (Bruce Wayne)</a></p>
#  <p><a href="people/cyborg.html" title="Cyborg">Cyborg (Victor Stone)</a></p>
#  <p><a href="people/elementwoman.html" title="Element Woman">Element Woman (Emily Sung)</a></p>
#  <p><a href="people/firestorm.html" title="Firestorm">Firestorm (Ronnie Raymond)</a></p>
#  <p><a href="people/flash.html" title="Flash">Flash (Barry Allen)</a></p>
#  <p><a href="people/superman.html" title="Superman">Superman (Clark Kent)</a></p>
#  <p><a href="people/wonderwoman.html" title="Wonder Woman">Wonder Woman (Diana)</a></p>
#  <p><a href="people/zatanna.html" title="Zatanna">Zatanna (Zatanna Zatara)</a></p>
#  </div>
#  </div>
#  </div>
#  </div>
#  </body>
#  </html>
