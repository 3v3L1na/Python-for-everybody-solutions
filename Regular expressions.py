# Regular expressions is a powerful Python module.
# It helps in reading files, looking for patterns, extracting interesting bits, slicing strings. 
# Regular expressions module 're' must be imported into the program before we can use it

# Search for lines that contain 'From'

import re                              # Import regular expressions
hand=open ('mbox-short.txt')           # Open the text 
for line in hand:                      
    line=line.rstrip ()                # Read through each line
    if re.search ('From', line):       # Use re.search to print the line that contains 'From.'
        print (line)

# Search for lines that start with 'F,' followed by 2 characters, followed by 'm:'

import re                              # Import regular expressions
hand=open ('mbox-short.txt')           # Open the text 
for line in hand:
           line=line.rstrip ()         # Read through each line
if re.search ('^F..m', line):          # Use re.search to print the line that contains 'F,' two characters, followed by 'm.'
        print (line)        

# Search for lines that start with From and have an at sign:

import re                              # Import regular expressions
hand=open ('mbox-short.txt')           # Open the text 
for line in hand:
    line=line.rstrip ()                # Read through each line
    if re.search ('^From':.+@', line): 
       print (line)                    # Use re.search to search for lines that start with from and have an @ sign

# Find all email addresses from each line:

import re
s='A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst=re.findall ('\S+@\S+,s)              
    print (lst)                       # The findall method searches the string in the second argument and returns a list of all the strings.
                                      # That is, all the strings that look like e-mail addresses. 
                                      
# Search for the lines that have an @ sign between characters:

import re
hand=open ('mbox-short.txt')
for line in hand:
    line=line.rstrip ()              # First we read each line 
    x=re.findall ('\S+@\S+,s, line)  # Extract all the substrings that match our regular expression. 
                  if len (x)>0:      # We check if the number of elements is more than zero
                  print (x)          # Print only lines where we found at least one substring that looks like an email address. 
                  
                  
# Search for the lines that have an @ sign between characters
# The characters must be a letter or number

import re
hand=open ('mbox-short.txt')
for line in hand:
line=line.rstrip ()
x=re.findall ('[a-zA-Z09]\S*@\S*[a-z-A-Z]'),
if len (x)>0:
print (x)


# Search for the lines that start with 'X' followed by any non white space characters and ':'
# Followed by a space and any number. 
# The number can include a decimal. 

import re
hand=open ('mbox-short.txt')
for line in hand:
line=line.rstrip ()
if re.search ('^X\S*:[0-9.]+', line):  # The right way to neatly filter only the lines we are looking for. 
print (line)



# Search for the lines that start with 'X' followed by any non white space characters and ':'
# Followed by a space and any number. 
# The number can include a decimal. 
# Then, print the number if it is greater than zero. 

import re
hand=open ('mbox-short.txt')
for line in hand:
line=line.rstrip ()
x=re.findall ('^X\S*:([0-9.]+)',line) # We add parentheses around the part of the re that represents the floating point number. 
if len (x)>0:
print (x)


# Search for lines that start with 'Details: rev=' followed by numbers
# Print the number if one is found

import re
hand=open ('mbox-short.txt')
for line in hand:
    line=line.rstrip ()
    x=re.findall ('^Details:*rev=([0-9]+', line)
    if len (x)>0
    print (x)

                              
 # Search for lines that start with From and a character followed by a two digit number between 00 and 99, followed by ':'
# Print the number if one is found

import re
hand=open ('mbox-short.txt')
for line in hand:
    line=line.rstrip ()
    x=re.findall ('^From.* ([0-9][0-9]:', line)
    if len (x)>0:
    print (x)                             













