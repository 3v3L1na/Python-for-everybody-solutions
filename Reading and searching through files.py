fhand=open ('mbox-short.txt')
count=0                                               #this sets count to zero and later it can get incremented to count +1 
for line in fhand:                                    #for each line in file handle, do this:
    count=count+1
print ('Line Count:', count)                          #this is telling the program to print 'line count' and always increment the count to count +1, add one to count variable

fhand=open ('mbox-short.txt')
inp =fhand.read ()                                    #this is telling the computer to read an entire file. Do it only if the file size is relatively small. 
print= (len(inp))                                     #the entire contents of the file are read:94626 characters 
print (inp [:20])                                     #use of string slicing: we print out the first 20 characters of the string data stored in inp. 

             
fhand=open ('mbox-short.txt')
for line in fhand:                                     #for each line in file handle, do this:     
    if line.startswith ('From'):                       #if the line starts with the word "From", print this line. 
        print (line)                                   #this will help a lot to find all the emails we received. Because the program will list them all. 

fhand=open ('mbox-short.txt')
for line in fhand:  
    line=line.rstrip ()                               #This rstrip method, as we learnt, strips whitespaces from the right side of a string. So the output will look neater. 
    if line.startswith ('From'):          
     print (line)

fhand=open ('mbox-short.txt')
for line in fhand:
    if not line.startswith ('From'):                 #Telling the program to continue searching if the line doesn't start with 'From' will make it work faster.
        continue
    print (line)

fhand=open ('mbox-short.txt')
for line in fhand:
    line=line.rstrip ()
    if line.find ('@uct.ac.za') == -1: continue     #Find looks for an occurence of a string within another string. It returns the position of the string, or a -1 if the string was not found. 
    print (line)