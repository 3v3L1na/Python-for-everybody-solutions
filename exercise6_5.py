#Exercise 5: Take the following Python code that stores a string: str ='X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after :
#Then, use the "float" function to convert the extracted string into a floating point number.

string= 'X-DSPAM-Confidence:0.8475' #define the string
col_pos =string.find (':')          #find the colon character
number=string [col_pos +1:]         #extract portion after ":"
confidence=float (number)           #convert confidence to floating point number
print (confidence)
