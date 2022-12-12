#Format operator-it allows us to construct strings, replacing parts of the strings with the data stored in variables.
#When applied to integers it is called MODULUS OPERATOR.
#When applied to strings it is called FORMAT OPERATOR. 

camels=42
'%d' % camels 

#the format sequence %d means:
#the second operand should be formatted as an integer.
#the result is a string '42'

camels=42
'I have spotted %2 camels.' %camels
#result: 'I have spotted 42 camels.'

'In %d years I have spotted %d camels.' (3, 0.1, 'camels')

#result: In 3 years I have spotted 0.1 camels. 