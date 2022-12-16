# Nested loops: when we have two 'for' loops.
# One loop is reading the file lines.
# Second loop is iterating through each of the word on the particular line. 

fname=input ('Enter the file name:')              # Prompt the user to enter the file name
try: 
    fhand=open (fname)
except:
    print ('File cannot be opened', fname)       # Open the file except if the file cannot be opened
exit ()

counts=dict ()
for line in fhand: 
    words=line.split ()
    for word in words:
        if word not in counts:
            counts [word]=1
        else: 
            counts [word] +=1                    # This is a compact alternative to: counts [word]=counts [word +1]. Similar alternative exists for -=1, *=1 and /=1
print (counts)