fname=input ('Enter the file name:')                      #define the file name variable. Ask from the user to input the file name. 
fhand=open (fname)                                        #allow the variable fhand to open the file name. 
count=0                                                   #set the count to zero.
for line in fhand: 
    if line.startswith ('Subject:'):                      #tell the computer that if the line starts with the word 'Subject' the count should be incremented to count+1
        count=count+1
print ('There were', count, 'subject lines in', fname)    #prompt the action to print the final count in the end in the file name. 