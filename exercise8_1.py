def chop (lst):  #Write a function called chop. 
    del lst [0]  #Removes the first element.
    del lst [-1] #Removes the last element. 
    
    def middle (lst) #Write a function called middle.
    new=lst [1:] #Stores all but the first element.
    del new [-1] #Deletes the last element. 
    return new 
    
my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)                          # Should be [2,3]
print(chop_list)                        # Should be None

middle_list = middle (my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]