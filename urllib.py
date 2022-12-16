# Using urllib, url library, we can treat a web page much like a file. We indicate which web page we would like to retrieve, and urllib handles the protocol and header details.

import urllib.request                                                     # We request the url library to be loaded
fhand=urllib.request.urlopen('http://data.pr4eorg/romeo.txt')             # Urllib opens the webpage
for line in fhand:
    print (line.decode ().strip())                                        # Urllib reads the webpage


# Retrieve the data for romeo.txt and compute the frequency of each word in the file:

import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen ('http://data.pr4eorg/romeo.txt')          # Urllib opens the webpage
counts=dict ()
for line in fhand:
    words=line.decode ().split ()
    for word in words:
        counts [word]=counts.get(word,0)+1
print (counts)

# Make a copy of a binary file (image or a video file) on a hard disk using urllib:

import urllib.request, urllib.parse, urllib.error 

img=urllib.request.urlopen ('http://data.pr4eorg/cover3.jpg'.read())    # Urllib opens the image
fhand=open ('cover3.jpg', 'wb')
fhand.write (img)                                                       # Urllib stores the image in the main memory of our computer, and then opens the file cover.jpg and writes the data out to our disk. 
fhand.close ()

# In order to avoid running out of memory, we retrieve the data in blocks (or buffers) and then write each block to the disk before retrieving the next block.

import urllib.request, urllib.parse, urllib.error 

img=urllib.request.urlopen ('http://data.pr4e.org/cover3.jpg')        # Urllib opens the image
fhand=open ('cover3.jpg', 'wb')
size=0
while True:
    info=img.read (100000)                                            # We read only 100,000 characters at a time
    if len (info)<1: break
    size=size+len (info)
    fhand.write (info)                                                # Then we write those characters to the cover3.jpg file before retrieving the next 100,00 characters from the web. 
print (size, 'characters copied.')
fhand.close ()