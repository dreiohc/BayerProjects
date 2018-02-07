import datetime
import os
import sys

cwid = os.environ["USERNAME"]

temporaryPath = ("//10.50.157.51/Temporary/BCP/BCP_backup_log/" + cwid)

withCWIDpath = os.path.join(temporaryPath, cwid)



dateStamp = datetime.date.today()

cwidLog = open(temporaryPath + str(dateStamp) + ".txt", "w")
   