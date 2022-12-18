# Change your socket program so that it counts the number of characters it has received and stops displaying
# any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and 
# display the count of number of characters at the end of the document. 

import socket                                 # Socket is imported

try:
    url=input ('Enter URL:')                 # User is prompted to enter URL
    host= (url.split ('/')[2])               # 'Split' is used to break the URL into its component parts. 
    mysock=socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect ((host,80))
    cmd='GET' + url + 'HTTP/1.0\r\n\r\n.encode()'
    cmd=cmd.encode ()
    mysock.send (cmd)
    
    received="b"                             # The variable that onsets the count of number of characters
    while True:
        data=mysock.recv (512)
        if len (data) < 1:
           break
        received +=data 
        
    received=received.decode ()
    print (received [3000])
    print (len (received))                   # Telling the program the exact number of characters, 300
    mysock.close ()
    
except: 
    print ('The URL is improperly formatted or non-existent!')
