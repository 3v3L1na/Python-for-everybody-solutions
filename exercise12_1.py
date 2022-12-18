# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any page.
# You can use split ('/') to break the URL into its component parts so you can extract the host name 
# for the socket connect call. Add error checking using 'try' and 'except' to handle the condition 
# Where the user enters  an improperly formatted or non-existent URL.

import socket                            # Socket is imported

try:
    url=input ('Enter URL:')                 # User is prompted to enter URL
    host= (url.split ('/')[2])               # 'Split' is used to break the URL into its component parts. 
    mysock=socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect ((host,80))
    cmd='GET' + url + 'HTTP/1.0\r\n\r\n.encode()'
    cmd=cmd.encode ()
    mysock.send (cmd)

    while True:
        data=mysock.recv (512)
        if len (data) < 1:
           break
    print (data.decode (), end='')
    
    mysock.close ()
    
except: 
    print ('The URL is improperly formatted or non-existent!')
