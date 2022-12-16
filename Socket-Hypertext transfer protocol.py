import socket

mysock=socket.socket (socket.AF_INET, socket.SOCK_STREAM)
mysock.connect (('data.pr4e.org',80))                                   # The program makes the connection to port 80 on the server www.py4e.com
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'. encode ()    # The get command is sent followed by a blank line. \r\n means End Of the Line (EOL)
mysock.send (cmd)
while True:
    data=mysock.recv (512)                                              # Once we send a blank line, we write a loop that receives data in 512 chunks
    if len (data) <1:
        break
    print (data.decode (), end='')                                      # The data is printed out until there is no more to read, i.e., the recv () returns an empty string). 
mysock.close ()

# Retrieve an image using HTTP

import socket 
import time 

HOST='data.pr4e.org'
PORT=80
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect ((HOST, PORT))
mysock.sendall (b'GET http://data.pr4e.org/cov-er3.jpg HTTP/1.0\r\n\r\n')# The content-type header indicates that body of the document is an image (image/jpeg)
count=0
picture=b''''''
while True:
    data=mysock.recv (5120)
    if len (data) <1: break
#time.sleep (0.25) 
count=count+len (data)
print (len (data), count)
picture=picture+data
mysock.close ()


# Look for the end of the header (2CRLF)

pos=picture.find (b"\r\n\r\n")
print ('Header length', pos)
print (picture[:pos].decode())


# Skip past the header and save the picture data

picture=picture [pos+4:]
fhand=open ("stuff.jpg", "wb")
fhand.write (picture)
fhand.close ()