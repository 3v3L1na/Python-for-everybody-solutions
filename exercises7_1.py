#Exercise 1: Write a program to read through a file.
#Print the contents f a file (line by line), all in upper case. 
#Executing the program will look as follows: python shout.py 

fhand=open ('mbox-short.txt')                         #indicates file handle to open a certain file. 
for line in fhand: 
    shout=line.rstrip (). upper                       #we use variable 'shout' because this is what the executing of the program will look like as per task. We use the functions of rstrip and uppercase together. 
    print (shout)                                     #rstrip gets us rid of the new line and upper capitalizes the text. 
    
