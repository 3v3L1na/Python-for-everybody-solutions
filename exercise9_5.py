#Exercise  9.5: This program records the domain name (instead of the address)
#where the message was sent from instead of who the mail came from (i.e., the whole email address). 
#At the end of the program, print out the contents of your dictionary.
#python schoolcount.py
#Enter a file name: mbox-short.txt
#['media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
#'caret.cam.ac.uk': 1, 'iupui.edu': 8}

# There are six important segments:

#1. Define variable

dictionary_domains=dict ()                    # Define the variable dictionary_domains

#2. Open the file

fname=input ('Enter file name:')              # Prompt the user to enter the file name
try:
    fhand=open(fname)                         # Try to open the file name
except FileNotFoundError:                     # If the FileNotFoundError appears print: File cannot be opened
    print ('File cannot be opened:', fname)
    quit ()

#3. Read the file

for line in fhand:
    words=line.split ()
    if len (words) <2 or words [0] !='From':
        continue
    
#4. In this segment, we determine the position of the 'at sign

    else:
        atpos=words [1].find ('@')           # Position of the 'at' sign
        domain=words[1][atpos+1:]            # Storing characters after 'at' sign

#5. First entry and additional count

        if domain not in dictionary_domains:
            dictionary_domains[domain]=1     # First entry
        else:
            dictionary_domains [domain] +=1  # Additional counts

#6. Print the final result
 
    print (dictionary_domains)