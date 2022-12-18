# Use urllib to replicate the previous exercise of (1), retrieving the document from a URL
# (2) displaying up to 3000 characters and (3) counting the overall number of chars. in the doc.
# Don't worry about the headers for this exercise, simply show the first 3000 chars.

# Step by step solution: 

import urlib.request                            # Imports the url library

url=input ('Enter URL:')                        # Prompts the user to read the document
content=urlib.request.urlopen (url).read()      # Reads the text
content=content.decode ()

print (content[3000])                           # Displays up to 3000 characters 
print (len(content))                            # Counts the overall number of characters
