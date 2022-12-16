#Exercise 1: Write a program that reads the words in words.txt and stores them as keys in a dictionary.
#Use the 'in' operator to check whether a string is in a dictionary. 

count=0                               #the word count is established at first
dictionary_words=dict ()              #we define the dictionary_words variable as dict ()
fhand=open ('words.txt')              #ONLY THEN can we open the document
for line in fhand: 
    words=line.split ()               #split the line
    for word in words: 
        count+=1                      #count the words-means read them at the same time
        if word in dictionary_words:
            continue                  #discard the duplicates
        dictionary_words[word]=count  #Value is first time word appears
if 'Python' in dictionary_words:      #Checking whether a string is in the dictionary. 
    print ('True')
else:
    print ('False')
    