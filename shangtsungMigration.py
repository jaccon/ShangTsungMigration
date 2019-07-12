import os
import sys
from subprocess import Popen
devnull = open(os.devnull, 'wb')

print "Shang Tsung IMAP Migration ..."
print "Type Enter to continue ..."

raw_input()
str1=raw_input("1) Disable SSL Check (Y/N) ")

str2=raw_input("2) Source Host Server ")
str3=raw_input("3) Source User  ")
str4=raw_input("4) Source Password  ")

str5=raw_input("4) Destination Host Server  ")
str6=raw_input("4) Destination User  ")
str7=raw_input("4) Destination Password  ")

if str1 == "Y":
    nosslcheck = 'nosslcheck'

os.system('imapsync --host1 '+ host1 +' --user1  '+ user1 +' --password1 '+ password1 +' --host2 '+ host2 +' --user2 '+ user2 +' --password2 '+ password2 +' --'+ nosslcheck  )

# imapsync --host1 imap.uhserver.com --user1  francisco@tostoedonda.adv.br --password1 230902es --host2 gator3009.hostgator.com --user2 francisco@tostoedonda.adv.br --password2 @12345678 --nosslcheck
