fhand=open ('mbox-short.txt')
count=0
for line in fhand: 
    words=line.split ()
    if len (words) <3 or words [0] !='From': #! (couldn't crack this one so best to review again. )
        continue
print (words [1])
for line in fhand:
    if line.startswith ('From'):
      count=count+1 
print ('There were %d lines in the file with From as the first word' %count) #!
    
    