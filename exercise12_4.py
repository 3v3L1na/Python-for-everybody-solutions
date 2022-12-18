# Change the urllinks.py program to extract and count paragraphs (p) tags from HTLM doc.
# Also, to display the count of the paragraphs as the output of your program. 
# Do not display the paragraph text, only count the paragraphs.
# Test your program on several small web pages as well as on some larger web pages. 

import urllib.request, urllib.parse, urllib.error

import ssl

from bs4 import BeautifulSoup

count=0                                                  # Initialize variables
ctx=ssl.create_default_context ()
ctx.check_hostname=False 
ctx.verify_mode=ssl.CERT_NONE

url=input ('Enter URL:')
html=urllib.request.urlopen (url, context=ctx).read()
soup=BeautifulSoup ('html.parser')

# Retrieve all of the anchor tags

tags=soup ('p')
for tag in tags:
    count +=1                                           # Increment counter
print (count)