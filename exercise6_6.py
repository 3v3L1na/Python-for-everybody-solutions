#Exercise 6: read the documentation of the string methods.
#Strip and replace are particularly useful. 
#https://docs.python.org/3/library/stdtypes.html#string-methods
#in total, there are 45 methods listed.

#1.capitalize ()

word='strawberry'
new_word = word.capitalize ()
print (new_word)

#2.casefold ()-removes all the case distinctions in a string.

word='StRaWbErRY'
new_word=word.casefold ()
print (new_word)

#3.center ()-prints the word in the center of the string

word='strawberry'
new_word=word.center (30)
print (new_word)

#4.count (0)-returns the number of times the value "strawberry" appears in the string.

sentence='I love strawberry. Strawberry is my fave fruit'
new_word=sentence.count ('strawberry')
print (new_word)

#5.encode () -returns an encoded version of the string 

word='strawberry'
new_word=word.encode ()
print (new_word)

#6.endswith ()-checks if the string ends with a punctuation sign

word='strawberry.'
if word.endswith ('.'):
    print ('Word ends with.')

#7.expandtabs ()-sets the tab size of the string 

word='s\t\r\a\w\b\e\r\r\y'
new_word=word.expandtabs (3)
print (new_word)

#8.find ()-it finds the element of the string.

sentence='I love strawberry. Strawberry is my fave fruit'
new_word=sentence.find ('fruit')
print (new_word)

word='strawberry'
new_word=word.find ('w')
print (new_word)

#9.format ()-format the specified value and insert it inside the string's placeholder.

#https://www.w3schools.com/python/ref_string_format.asp

#10.format_map ()-formats specified values in a string. 

#11. index ()-searches the string for a specified value. 
#Then, it returns the position of where it was found. 
#It is like find (), but it raises ValueError when the substring is not found.

word='strawberry'
new_word=word.index ('y')
print (new_word)

#12. isalnum ()-returns "true" if all characters in the string are alphanumeric

word='strawberry14'
new_word=word.isalnum ()
print (new_word)

#13. isalpha ()-checks if all characters in the string are letters.
#if it's the case, returns "True"
#if it isn't returns "False"

word="1strawberry4"
new_word=word.isalpha ()
print (new_word)

#14. isdecimal ()-checks if all characters in the string are decimals. 
#if it's the case, returns "True"
#if it isn't returns "False"

word='1234'
new_word=word.isdecimal ()
print (new_word)

#15. is digit ()-checks if all characters in the string are digits. 
#if it's the case, returns "True"
#if it isn't returns "False"

word='1234'
new_word=word.isdigit ()
print (new_word)

#16. isidentifier ()-checks if all characters in the string are identifiers. 
#if it's the case, returns "True"
#if it isn't returns "False"
#A string is considered a valid identifier if it only contains a-z, 0-9 or underscores.
#A valid identifier cannot start with a number. 
#A valid identifier cannot contain any spaces.

word='1strawberry'
new_word=word.isidentifier()
print (new_word)

#17. islower ()-checks if all characters in the string are lowercase. 
#if it's the case, returns "True"
#if it isn't returns "False"

word='1Strawberry'
new_word=word.islower()
print (new_word)

#18. isnumeric ()-checks if all characters in the string are numeric. 
#if it's the case, returns "True"
#if it isn't returns "False"

word='1234'
new_word=word.isdigit ()
print (new_word)

#19. isprintable ()-checks if all characters in the string are numeric. 
#if it's the case, returns "True"
#if it isn't returns "False"
#Non printable characters are those defined in the Unicode character database as:
#Other" or "Separator," excepting the ASCII space (0x20), which is considered printable. 

word='strawberry#1'
new_word=word.isprintable ()
print (new_word)

#20. isspace ()-checks if all characters in the string are whitespace. 
#if it's the case, returns "True"
#if it isn't returns "False"

word='strawberry#1'
new_word=word.isspace ()
print (new_word)

#21. istitle ()-checks if all characters in the string are whitespace. 
#if it's the case, returns "True"
#if it isn't returns "False"

sentence='Hello, Darkness, My Old Friend'
new_word=sentence.istitle ()
print (new_word)

#22. isupper ()-checks if all characters in the string are uppercase. 
#if it's the case, returns "True"
#if it isn't returns "False"

word='STRAWBERRY'
new_word=word.isupper()
print (word)

#23. join () - joins the elements of an iterable to the end of the string.
#When it joins them, it uses the hash character as a separator. #

words=('John', 'Peter', 'Vicky')
new_word='#'.join (words)
print (new_word)

#24. ljust () - returns a left justified version of the string

word='strawberry'
new_word=word.ljust (30)
print (new_word, 'is my favorite fruit')

#25. lower () - converts a string into a lower case

word='STRAWBERRY'
new_word=word.lower ()
print (new_word)

#26. lstrip () - returns a left trim version of the string

word='           strawberry       '
new_word=word.lstrip ()
print (new_word)

#27. maketrans () - returns a translation table to be used in translations
#It is a method to replace specified characters. 

word='strawberry'
new_word=word.maketrans ('t', 's')
print (word.translate (new_word))

#28. partition () - returns a tuple where the string is parted into three parts

#everything before the 'match'
#the 'match'
#everything after the 'match' 

words='I could eat strawberries all day'
new_word=words.partition ('strawberries')
print (new_word )


#29. replace () - returns a string where a specified value is replaced with a specified value

words='I hate strawberries'
new_word=words.replace ('strawberries', 'apples')
print (new_word)

#30. rfind () - searches the string for a specified value.
# It returns the last position of where it was found.

words='Mi casa es su casa.'
new_word=words.rfind ('casa')
print (new_word)

#31. rindex () - searches the string for a specified value. 
# It returns the last position of where it was found.

words='Mi casa es su casa.'
new_word=words.rindex ('casa')
print (new_word)

#32. rjust () - returns a right justified version of the string.

word='          strawberry      '
new_word=word.rjust (20)
print (new_word)

#33. rpartition () - returns a tuple where the string is parted into 3. 

words='I could eat strawberries all day, they are my fave'
new_word=words.rpartition ('strawberries')
print (new_word)

#34. rsplit () - Splits the string at the specified separator.
#Then, it returns a list. 

words= 'apples, bananas, cherries'
new_word=words.rsplit (',')
print (new_word)

#35. rstrip () - returns a right trim version of the string. 

word='     strawberry   '
new_word=word.rstrip ()
print ('of all fruits', new_word, 'is my favorite')

#37. split () - Splits the string at the specified separator, and returns a list.

words='welcome to the jungle'
new_word=words.split ()
print (new_word)

#38. splitlines () - Splits the spring at line breaks and returns a list.

words='Thank you for the music\nWelcome to the jungle'
new_word=words.splitlines ()
print (new_word)


#39. startswith () - Check if the string starts with a certain word.
#Returns a true or false.

words ='Hello from the other side'
new_word=words.startswith ('Hello')
print (new_word)

#40. strip () - Returns a trimmed version of the string. 
#removes spaces at the beginning and at the end of the string.

word='         strawberry    '
new_word=word.strip ()
print ('Of all fruits,', new_word, 'is my favorite')

#41. swapcase () - Make the lower case upper case and vice versa.

words=' HELLo fROM the OtHeR SIDE'
new_word=words.swapcase ()
print (new_word)

#42. title () - Converts the first character of each word to uppercase.

words= 'hello from the other side'
new_word=words.title ()
print (new_word)

#43. translate () - replace any 'S' character with a 'P' character

#use a dictionary with ascii codes to replace 83, with 80. 

mydict={83:80}
words='Hello Sam!'
print (words.translate(mydict))

#44. upper () - Uppercase the string.

words='Hello, my friends'
new_word=words.upper ()
print (new_word)

#45. zfill () - fill the string with zeros until it is 10 chars long.

words='50'
new_word=words.zfill (10)
print (new_word)






