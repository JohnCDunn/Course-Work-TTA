#No Gui for this on
# Create two folders on the desktop Folder A and Folder B
# Create a few files in folder A 

import os
import shutil
import time
from datetime import datetime, timedelta


folderA = "C:\Users\Student\Desktop\Folder A"
folderB = "C:\Users\Student\Desktop\Folder B"

yesterday = datetime.now() + timedelta(hours=-24)
dateTime_24  = format(yesterday, "%Y%m%d")
dateTimeNow = time.strftime("%Y%m%d")

for file in os.listdir(folderA):
    filePathA = os.path.join(folderA,file)
    fileDateTime = time.strftime('%Y%m%d', time.gmtime(os.path.getmtime(filePathA)))

    if (fileDateTime >= dateTime_24 and
        fileDateTime <= dateTimeNow):
        filePathB = os.path.join(folderB,file)
        shutil.move(filePathA, filePathB)
  
