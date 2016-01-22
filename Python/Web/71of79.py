
import webbrowser

f = open('stayTuned.html','w')

bodyText = "Try this one"

message = """
<html>
<body>
bodyText
</body>
</html>
"""

f.write(message)
f.close()

webbrowser.open_new_tab('stayTuned.html')