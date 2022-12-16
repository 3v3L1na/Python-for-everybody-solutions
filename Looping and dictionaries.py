# If you use a dictionary as a sequence in a for statement, it traverses the keys of the dictionary. 

counts= {'chuck':1, 'annie':42, 'jan':100}
for key in counts:
    print (key, counts [key])                 # The keys and the corresponding values are printed but in no particular order.
    
# Find all the entries in a dictionary with a value above ten. 

counts={'chuck':1, 'annie':42, 'jan':100}
for key in counts:
    if counts [key]>10:
        print (key, counts[key])
        
# Print the keys in alphabetical order:

counts={'chuck':1, 'annie':42, 'jan':100}
lst=list(counts.keys())                     # First we see the keys in the unsorted order 
print (lst)
lst.sort ()                                 # Sorted order
print (key, counts [key])