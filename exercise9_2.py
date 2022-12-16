#Exercise  9.2: Write a program that categorizes each mail message by which day of the week the commit was done. 
#To do this, look for lines that start with"From", then look for the third word and keep a running count of each of the
#days of the week. At the end of the program, print out the contents of your
#dictionary (order does not matter).
#Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Sample Execution:
#python dow.py
#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}

dictionary_days=dict ()                       # Define the variable of dictionary days 
fname=input ('Enter a file name:')            # Prompt for the file name
try: 
    fhand=open (fname)                        # Open file unless:
except FileNotFoundError:                     # The file can't be found. 
    print ('File cannot be opened', fname)    # In that case, print 'File cannot be opened.'
    exit ()

for line in fhand:                            
    words=line.split ()                       # Read through the file
    if len (words) <3 or words [0] != 'From': # If there are more than three words in line and if line starts wth 'From'
        continue                              # Continue
    else:
        if words [2] not in dictionary_days:  # If not:
            dictionary_days [words[2]]=1
        else:
            dictionary_days [words[2]]+=1

print (dictionary_days)