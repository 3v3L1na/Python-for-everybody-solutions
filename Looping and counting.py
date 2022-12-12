word='strawberry'      #we define the variable "word" by sampling one of its possible classes: "strawberry"
count =0               #we set the initial count to '0'
for letter in word:    #commencing of the "for" loop. For each letter in the variable "word"
    if letter =='r':   #if letter equals "r"
        count=count+1  #the count should be "count +1", which is 0+1=1
print (count)          #tell the program to execute the count. The result should be "3"


#Exercise3: Encapsulate this code in a function named count. 
# Generalize it so that it accepts the string and the letter as arguments. 

def count (word, letter): #we define the variable "count" as any word or letter
    counter=0             #counter is set to "0"
    for character in word:#commencing of the "for" loop
        if character==letter: #commencing of the "if" loop-conditioning
            counter=counter +1 
print (count)

input_word = input('Enter the word: ')
input_letter = input('Enter the letter: ')
count(input_word, input_letter)
