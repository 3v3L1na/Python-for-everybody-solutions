count = 0                                   # Initialize variables
total = 0

fname = input('Enter the file name: ')      #prompts the user to enter the file name.
try:                                        #initiates the 'try' and 'except' loop. 
    fhand = open(fname)
except FileNotFoundError:                   #sets the exception in case of "FileNotFoundError"
    print('File cannot be opened: ', fname)
    quit()                                  #tells the loop to quit and exit in case if the File cannot be opened. 

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1                      #prompts the loop to count the lines that start with 'X-DSPAM-Condifence.'
        colpos = line.find(':')
        number = line[colpos + 1:].strip()    # Removes all text except number
        SPAM_C = float(number)                # Extract the floating-point number on the line. 
        total = total + SPAM_C

average = total / count
print('Average spam confidence: ', average)