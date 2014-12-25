'''
The program should do the following:
Parse the HTTP access log file for the access code 200:
  Get the IP address and print a HTML report of the request URL and IP address/Hostname in a table format

Optional but bonus if you can also use the python-geoip: http://pythonhosted.org/python-geoip/ library to 
find the geolocation of the IP and display that on the report as well.

# ----- ip address  -------  location  ----- hostname -----
'''
import re
from geoip import geolite2

log = open('access_log','r')

FILE = log.readlines()

log.close()
printList = [ ]
for line in FILE:
    if (' 200 ' in line):
         # here you may want to do some splitting/concatenation/formatting to your string
         printList.append(line)

def getAddr( access ):
  if(access is None or not isinstance(access, str) ):
    print "getAddr passed bad input"
    return 1 ## generic failure
  for x in range(0, len(access) ):
    if access[x] == ' ' :
      break;
  return access[:x]

def getLocation( access ):
  if(access is None or not isinstance(access, str) ):
    print "getLocation passed bad input"
    return 1 ## generic failure
  ip = getAddr(access)
  try:
    match = geolite2.lookup(ip)
  except ValueError:
    return "No location found" 
  if match is None:
    return "No location found" 
  else :
    return match.country  

def getHost(access): ##the hostnames come in the form "GET /address here/etc "
  if(access is None or not isinstance(access, str) ):
    print "getHost passed bad input"
    return 1 ## generic failure
  qOnePos = 0 #positions of quotes one and two
  qTwoPos = 0
  for x in range(0, len(access) ): #iterate through to find second quote
    if access[x] == '"' : # the string is contained inside
      if qOnePos == 0:
        qOnePos = x  
      else:
        qTwoPos = x
  return access[ qOnePos + 4 : qTwoPos ]

'''
debugging 
getname(None)
n = 3
getAddr(n)
getHost(None)
getHost(n)

exline = "199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] \"GET /history/apollo/ HTTP/1.0\" 200 6245 "
print getLocation(exline)
'''

print "<table>"
print "<tr> \n" + "<th>Address</th> \n" + "<th>Location</th>\n" + "<th>Hostname</th> \n"

for item in printList:
    print "<tr> \n  <td>" + getAddr(item) + "</td> \n"+ "<td>\n"+ getLocation(item)+"</td>\n" + "<td> \n" + getHost(item) + "</td> \n " + "</tr>"
    

print "</table>"

