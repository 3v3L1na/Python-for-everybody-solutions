# One way to parse HTML is to use regular expressions to repeatedly search for and extract substrings that match a particular pattern

# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <1 href="http://dr-chuck.com/page2.htm">
# Second Page </a>
# </p>

# We can consult a well-formed regular expression to match and extract the link values. 

import urllib.request, urllib.parse, urllib.error
import re
import ssl                                               # The ssl library allows the program to access web sites that strictly enforce HTTPS

# Ignore SSL certificate errors

ctx=ssl.create_default_context ()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input ('Enter -')
html=urllib.request.urlopen (url, context=ctx).read () # The read method returns HTML source code as a bytes object, instead of returning an HTTP Response object
links=re.findall (b'href="(http[s]?://.*?)"', html)    # The findall regular expression method will give us a list of all the strings that match our regular expression, returning only the link text between the ""
for link in links:
    print (link.decode ())
    
# Parsing HTML using Beautiful Soup - if we only use regular expressions we might either miss some valid links or end up with bad data

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

# Ignore SSL certificate errors

ctx=ssl.create_default_context ()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input ('Enter-')                                 # The program prompts for the web address. 
html=urllib.request.urlopen (url, context=ctx).read()# The program reads the data. 
soup=BeautifulSoup (html, 'html.parser')             # The program passes the data to the BeautifulSoup parser

# Retrieve all of the anchor tags

tags=soup ('a')
for tag in tags:
    print (tag.get ('href', None))                  # All the anchor tags are retrieved and the href attribute is printed for each tag. 
    
# Pull out various parts of each tag:

from urllib.request import urlopen
from bs4 import BeautifulSoup 
import ssl

# Ignore SSL certificate errors 

ctx=ssl.create_default_context ()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input ('Enter-')
html=urlopen (url, context=ctx).read ()
soup=BeautifulSoup (html, "html.parser")

# Retrieve all of the anchor tags

tags=soup ('a')
for tag in tags:
    # Look at the parts of a tag and pull out parts of each tag such as URL, Contents, or Attributes
    print ('TAG:', tag)
    print ('URL:', tag.get ('href', None))
    print ('Contents:', tag.contents[0])
    print ('Attrs:', tag.attrs)













