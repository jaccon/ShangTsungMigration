import os
import sys
from subprocess import Popen
import platform

devnull = open(os.devnull, 'wb')
configurationFile = 'config.json'

print "Shang Tsung IMAP Migration ..."
print "Set your configuration in config.json file and type Enter ..."
raw_input()

# Check ImapSync
cmd = "where" if platform.system() == "Windows" else "which"
try: 
    subprocess.call([cmd, imapsync])
except: 
    print "ImapSync not installed. Please run brew install imapsync to continue"
    exit

# question=raw_input("Start configuration...")
import json
with open(configurationFile) as f:
  data = json.load(f)

  disableSSLCheck = data["disableSSLCheck"]
  sourceServer = data["sourceServer"]
  sourceUser = data["sourceUser"]
  sourcePassword = data["sourcePassword"]
  destinationHost = data["destinationHost"]
  destinationUser = data["destinationUser"]
  destinationPassword = data["destinationPassword"]

  print ""
  print ""
  print("Disable SSL Check :" +  disableSSLCheck)
  print ""
  print "Host Server Settings"
  print("Source Host Server :" + sourceServer)
  print("Source User:" + sourceUser)
  print("Source Password:" + sourcePassword)
  print ""
  print "Destination Server Settings"
  print("Destination Host Server:" + destinationHost)
  print("Destination User:" + destinationUser)
  print("Destination Password:" + destinationPassword)
  print ""
  print ""
  print "***** Enjoy my magic ******** "

  if disableSSLCheck == "Y":
      nosslcheck = "nosslcheck"

  os.system('imapsync --host1 '+ sourceServer +' --user1  '+ sourceUser +' --password1 '+ sourcePassword +' --host2 '+ destinationHost +' --user2 '+ destinationUser +' --password2 '+ destinationPassword +' --'+ nosslcheck  )
  




# os.system('imapsync --host1 '+ host1 +' --user1  '+ user1 +' --password1 '+ password1 +' --host2 '+ host2 +' --user2 '+ user2 +' --password2 '+ password2 +' --'+ nosslcheck  )

# imapsync --host1 imap.uhserver.com --user1  francisco@tostoedonda.adv.br --password1 230902es --host2 gator3009.hostgator.com --user2 francisco@tostoedonda.adv.br --password2 @12345678 --nosslcheck
