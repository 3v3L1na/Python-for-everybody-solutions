x=14
if x>0:
    print ('x is positive') #if statements always end with a colon character: The lines after the if statement are indented, however there are programs for auto indentation)
    
y=3
if y <10:
    print ('Small')
    
    
z=14
if z%2 == 0:
    print ('z is even')
else:
    print ('z is odd') #alternative execution - only one of the options gets executed. There is one branch. 
    
a=13
b=14

if a<b:
    print ('a is less than b')
elif a>b:
    print ('a is greater than b')
else:
    print ('a and b are equal') #chained conditional - only one of the options gets executed. There are two or more branches.
    

x==1
y==1
if x==y:
    print ('x and y are equal')
else:
    if x<y:
        print ('x is less than y')
    else:
        print ('x is greater than y') #nested conditional. The first branch contains a simple sentence, and the second branch contains two branches of its own. They are best avoided.

if 0 <x:
    if x <10:
        print ('x is a positive single-digit number.') #this conditional can be simplified.add()
        
if 0<x and x<10:
    print ('x is a positive single-digit number.')