#Exercise  10.1: Revise a previous program as follows: Read and parse the "From"
#lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits by
#creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in the reverse order and print out the person who has the most commits.
#Sample line:
#From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195

dictionary_addresses=dict ()                         # Define variables. 
lst=list ()

fname=input ('Enter file name:')
try:
    fhand=open (fname)                               # Open the file
except FileNotFoundError:
    print ('File cannot be opened:', fname)          # In case the file can't be opened, print:

for line in fhand:
    words=line.split ()                              # Read the file
    if len (words) <3 or words [0] !='From':
        continue
    else:
       if words [1] not in dictionary_addresses:
           dictionary_addresses[words[1]]=1          # First entry
       else:
           dictionary_addresses[words[1]] +=1        # Additional count
for key, val in list (dictionary_addresses.items()):  
    lst. append (val, key)                           # Fill list with value, key or dict
lst.sort (reverse=True)                              # Sort by highest value
for count, email in lst [:1]:                        # Only displays the largest value
    print (email,count)                         
        