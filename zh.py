import re, sys, requests


print """
########################
# Coded By Afrizal F.A #
# Auto Mirror Zone-H   #
########################
"""

listweb=open(sys.argv[1], "r").read()
pisah=listweb.split("\n")
nick=sys.argv[2]
user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

for x in pisah :
   if not x :
      continue
   mirror=requests.post(url="http://www.zone-h.org/notify/single?hz=1", data={ "defacer" : nick, "domain1" : x, "hackmode" : 1, "reason" : 1}, headers={"User-Agent" : user_agent})
   if re.search("ERROR", mirror.content) :
      print "[-] " + x + " => Error"
   else :
      print "[+] " + x + " => Ok"
