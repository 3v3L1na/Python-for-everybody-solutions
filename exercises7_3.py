fname=input ('Enter the file name:')                          #prompts the user to enter the name of the file 
try:                                                           
    if fname==('na na boo boo'):                              #if the exact name of the file is na na boo boo, then print:
        print ('NA NA BOO BOO TO YOU - You have been punkd!')
        (exit)
except: FileNotFoundError                                     #except if there is a File Not Found Error 
print ('File cannot be opened', fname)                        #in this case tell the user that the file cannot be opened 
(exit)                                                        #exit the program
        
