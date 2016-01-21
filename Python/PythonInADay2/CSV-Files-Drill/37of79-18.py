import urllib2
from bs4 import BeautifulSoup

webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

#  Convert to BeautifulSoup

soup = BeautifulSoup(webpage)
print soup.body

# Results:
# <body>
# <div id="container">
# <div class="block">
# <div class="title">
# <h1>The Justice League</h1>
# </div>
# </div>
# <div class="block">
# <p><blockquote>"Their founding members included Aquaman, Batman, Cyborg, The Flash, Green Lantern, Superman and Wonder Woman. They first met when Darkseid invaded the planet with his Parademons in search of the Anti-Life Equation. Present day they exist alongside Justice League Dark and Justice League International."</blockquote></p>
# <p class="quote">- Quote from <a href="http://dc.wikia.com/wiki/Justice_League_(Prime_Earth)">DC Wikia</a></p>
# </div>
# <div class="block">
# <div class="image">
# <img alt="The Justice League" height="200px" src="images/justice_league.jpg" title="The Justice League"/>
# <p class="image_quote">- Image from <a href="http://dc.wikia.com/wiki/Justice_League_(Prime_Earth)">DC Wikia</a></p>
# </div>
# </div>
# <div class="block">
# <h2>Information</h2>
# <div class="separator">
# <div class="info_left">Team Name</div>
# <div class="info_right">The Justice League</div>
# </div>
# <div class="separator">
# <div class="info_left">Alignment</div>
# <div class="info_right">Good</div>
# </div>
# <div class="separator">
# <div class="info_left">Status</div>
# <div class="info_right">Active</div>
# </div>
# <div class="separator">
# <div class="info_left">Members</div>
# <div class="info_right">
# <p><a href="people/aquaman.html" title="Aquaman">Aquaman (Arthur Curry)</a></p>
# <p><a href="people/batman.html" title="Batman">Batman (Bruce Wayne)</a></p>
# <p><a href="people/cyborg.html" title="Cyborg">Cyborg (Victor Stone)</a></p>
# <p><a href="people/elementwoman.html" title="Element Woman">Element Woman (Emily Sung)</a></p>
# <p><a href="people/firestorm.html" title="Firestorm">Firestorm (Ronnie Raymond)</a></p>
# <p><a href="people/flash.html" title="Flash">Flash (Barry Allen)</a></p>
# <p><a href="people/superman.html" title="Superman">Superman (Clark Kent)</a></p>
# <p><a href="people/wonderwoman.html" title="Wonder Woman">Wonder Woman (Diana)</a></p>
# <p><a href="people/zatanna.html" title="Zatanna">Zatanna (Zatanna Zatara)</a></p>
# </div>
# </div>
# </div>
# </div>
# </body>
