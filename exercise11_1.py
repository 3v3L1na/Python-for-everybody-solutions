#Exercise  11.1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author
#$ python grep.py
#Enter a regular expression: ^X-
#mbox.txt had 14368 lines that matched ^X-
#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4218 lines that matched java$

import re                                               # Import regular expressions

count=0                                                 # Counter starts at 0

input_exp =input ('Enter a regular expression:')        # Define variables
reg_exp= str (input_exp)                                # Regular expressions are strings
fname='mbox.txt'
fhand=open (fname)

for line in fhand:
    line=line.rstrip()
    if re.findall (reg_exp,line) !=[]:
        count +=1                                       # Read through the file and only count if something was found; then print

print (fname + 'had' + str (count) + 'lines that matched' + reg_exp)   