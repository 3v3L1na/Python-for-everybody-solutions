#Exercise  9.3: Write a program to read through a mail log, build a histogram
#using a dictionary to count how many messages have come from each email address, and print the dictionary.
#Enter file name: mbox-short.txt
#{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
#'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
#'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
#'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
#'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

dictionary_addresses=dict ()                  # Define the dictionary_addresses variable
fname=input ('Enter file name:')              # Prompt the user to Enter file name. 
try:                                          # Start the try-except loop. 
    fhand =open (fname)
except FileNotFoundError:                     # If the file is not found print 'File cannot be opened' 
    print ('File cannot be opened:', fname)
    (exit )

for line in fhand:
    words=line.split ()                       # This command aids in reading lines
    if len (words) <2 or [words [0]] !='From':# This seeks the 'From' string in all the sent mails.
        continue
    else:
        if words [1] not in dictionary_addresses:
            dictionary_addresses [words[1]]=1
        else:
            dictionary_addresses [words[1]]=+1
print (dictionary_addresses)