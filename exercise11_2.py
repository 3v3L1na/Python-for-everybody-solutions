#Exercise  11.2: Write a program to look for lines of the form
#'New Revision: 39771'
#and extract the number from each of the lines using a regular expression and
#the findall() method. Compute the average of the numbers and print out the average.
#Enter file:mbox.txt
#38549.7949721
#Enter file:mbox-short.txt
#39756.9259259

import re
rev =[]
rev_ave=0                                            # Define variables

fname=input ('Enter file name:')
try:
    fhand=open (fname)
except FileNotFoundError:
       print ('File cannot be opened:', fname)      # Open file unless it cannot be opened/found
       exit ()
for line in fhand:
    line =line.rstrip ()
rev_temp=re.findall ('^New Revision: [0-9.]+',line)

for val in rev_temp:
    val=float (val)                                 # Convert the strings to floats
    rev=rev+[val]                                   # Combine all values

rev_sum=sum (rev)
count=float (len(rev))
if count:
    rev_ave=rev_sum/count                           # Compute the average of numbers
print (rev_ave)                                     # Print out the average


       