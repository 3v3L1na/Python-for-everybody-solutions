data= 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find ('@') #this is a method "at position" that wants us to find data.
print(atpos)
sppos =data. find ('', atpos)
print (sppos)
host= data [atpos+1:sppos]
print (host)

#we use a version of find method that allows us to specify a position.
#once the position is specified, 21, we can start looking.
#This is called "splicing". 
#We extract the characters from "one beyond the at-sign" through up to BUT NOT INCLUDING THE SPACE CHARACTER.

