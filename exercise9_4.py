#Exercise  9.4: Add code to the above program to figure out who has the most messages in the file.
#After all the data has been read and the dictionary has been created, look
#through the dictionary using a maximum loop (see Section [maximumloop]) to
#find who has the most messages and print how many messages the person has.
#Enter a file name: mbox-short.txt cwen@iupui.ed 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195

dictionary_addresses=dict ()                     # Define the variable 'dictionary addresses'
maximum=0                                        # Define maximum address
maximum_address=''

fname=input ('Enter file name:')                 # Prompt the user to enter the file name
try:
    fhand =open (fname)                          # Try to open the file
except FileNotFoundError:
    print ('File cannot be opened:', fname)      # If it can't be opened print so, and exit the loop. 
    (exit)
    
for line in fhand:
    words=line.split ()                          # Read through the file
    if len (words) <2 or words [0] != 'From':
        continue
    
    if words [1] not in dictionary_addresses:
        dictionary_addresses [words[1]]=1        # First entry
    else:
        dictionary_addresses [words[1]]=+1       # Additional count
 
for address in dictionary_addresses:
    if dictionary_addresses [address]>maximum:   # Checks if new maximum
        maximum=dictionary_addresses [address]   # Update the maximum if needed
        maximum_address=address                  # Stores the address of maximum 

print (maximum_address, maximum)
        
