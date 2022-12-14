my_list = []                               #at first, the list should be defined as empty.
while True:
    number=0.0
    input_number=input ('Enter a number:') #prompt the user to Enter a number with 'input' command
    if input_number=='done':               #when the user enters 'done'
       break 
    try: 
        number=float (input_number)
    except ValueError:
        print ('Invalid input')
        quit ()                           #if the value is erroneous, print 'Invalid Input' and exit the loop with quit ()

if my_list:
    print ('Maximum:', max (my_list) or None)
    print ('Minimum'), min (my_list)     #compute the maximum and minimum numbers AFTER the loop completes (afte the quit moment)
       
