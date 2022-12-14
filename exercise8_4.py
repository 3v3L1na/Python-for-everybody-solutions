my_list=['Arise,', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
fhand=open ('romeo.txt') #Step 1 and Step 2 were correct: define the list and open the romeo.txt. 
for line in fhand:
    words=line.split ()  #splits line into array of words
for word in words:       #this line was missing
    if word in my_list:
        continue         #discard duplicates
my_list.append (word)    #update the list by appending
print (sorted(my_list))  #an elegant way to print out the whole list already sorted in alphabetical order.
                         #Instead of using the command sort ()
        