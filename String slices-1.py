s='Monty Python' #'s' stands for slice variable. The variable is defined as "Monty Python"
print (s[0:5]) #the segment 0:5 means that the program is supposed to print the positions 0,1,2,3,4 of the word 'Monty.'

s='Evelina Saponjic'
print (s[8:16])

vegetable='carrot' #variable "vegetable" is being defined as a one of its individual representatives 
print (vegetable [:3]) #the slice starts at the beginning of the string and prints the first three letters

vegetable='eggplant'
print =(vegetable [5:])

#Exercise 2: Given that fruit is a string, what does fruit [:] mean?

# Answer: fruit[:] is the whole string stored in the variable fruit
# .... this is because omission of the first index starts the slice 
# at the beginning and omission of the second index goes to the end
# of the string.

greeting= 'Hello, world!'
new_greeting= 'J' + greeting [1:]
print (new_greeting)

#This example concatenates a new first letter onto a slice of greeting.
# Strings are immutable so we can't change an existing string. 
# But, what we can do, is create a new string. 
# In this case if the words belonged to a variable "greeting", we will create a variable new_greeting and define it as J + ello world. "Ello world" is a greeting [1:]"