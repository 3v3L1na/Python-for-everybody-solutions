def computepay (tmp_hours, tmp_rate): #calculates the amount to pay taking into the account overtime 
    if tmp_hours <= 40:
        print (tmp_hours * tmp_rate) #no overtime calculation

overtime = tmp_hours - 40.0                # How much overtime is left
return (tmp_rate * 40.0) + (1.5 * tmp_rate * overtime)


def check_for_float(input1):
    """
    Checks if the type of "input1" is a float and returns the value if so.
    Input:    input1 -- variable to check
    Output: val -- value of float
    """
    try:
        val = float(input1)                # Only allows input floats
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()

        