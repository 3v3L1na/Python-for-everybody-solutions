
#Exercise  10.3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to
#lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than letters a-z. 
# Find textsamples from several different languages and see how letter frequency varies between languages. 
#Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies

import string
counts=0
dictionary_counts=dict ()
relative_lst=list ()                                                # Initialize all the variables

fname=input ('Enter File Name:')
try:
    fhand =open (fname)
except FileNotFoundError:
    print ('File cannot be found', fname)
    exit ()                                                         # Open the program; if the file cannot be found, print so. 

for line in fhand: 
    line=line.translate(str.maketrans ('', '', string.digits))      # Remove numbers
    line=line.translate(str.maketrans ('', '', string.punctuation)) # Remove punctuation
    line=line.lower()                                               # Set letters to lower case

words=line.split ()
for word in words:
    for letter in word:
        counts+=1                                                   # Count each letter for relative frequencies
    if letter not in dictionary_counts:
        dictionary_counts[letter]=1
    else: dictionary_counts [letter]+=1

for key, val in list (dictionary_counts.items()):
    relative_lst.append (val / counts, key))                        # Calculates the relative letter frequency
    
relative_lst.sort (reverse=True)                                    # Sorts from highest relative letter frequency

for key, val in relative_lst:
    print (key,val)
