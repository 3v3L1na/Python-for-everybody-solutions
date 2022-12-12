#Python has a function called dir which lists the methods available for an object.
#The "Type" function shows the type of an object, and the "dir" shows all its methods.

stuff = ('Hello, world!')
type (stuff) #class 'str' - this means that 'type' is a function that tells us that 'Hello world' is a string.
dir (stuff)  #capitalize, casefold, center, count, find, format, index, rpartition...
#"dir" lists all the methods that you can do with the strings. There is a library that lists absolutely all string methods.

#instead of the function syntax upper (word), the method uses the method syntax word.upper()
#this is called a dot notation. "Upper" is the name of the method. The parenthesis indicate that this method takes no argument. 

word= 'banana'          #we define a variable "word" with "banana", one of the possible words.
new_word =word.upper () #we define a variable "new_word" as a method: word.upper ()
print (new_word)        #the program prints the word "banana" in uppercaseletters: BANANA

word= 'banana'
index= word.find ('a') #method "find" searches for the position of one string within another.
print=index 

line='Here we go'
line.strip () #remove white spaces, tabs or newsline

line='Have a nice day'
line.startswith ('Have') #This method returns boolean values, "True" or "False"
line.startswith ('h') #False. It requires a case to match. 
