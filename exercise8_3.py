fhand=open ('mxbox-short.txt')
for line in fhand: 
    words=line.split ()
    if len (words) <3 or words[0]!='From':
     continue 
    print(words[2])   
    
    #The code from exercise 8_2 has been rewritten. 
    #The code is now compound 'if', 'or' instead of having two 'if' statements. 