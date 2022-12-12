#If the open call fails, we should add recovery code.
fname= input ('Enter the file name:')                       #allows the user to input the file name through defining the file name variable
try:
    fhand =open (fname)
except:                                                    #establishes an exception
   print ('File cannot be opened:', fname)                 #in case that the file can't be opened we should print: 'File cannot be opened', followed by the name of the file. 
count=0
for line in fhand:
    if line.startswith ('Subject:'):
        count=count +1 
print ('There were', count, 'subject lines in', fname)

