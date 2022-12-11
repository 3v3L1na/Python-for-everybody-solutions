def check_for_float(input1, exit = True):
    """
    Checks if the type of "input1" is a float and returns the value if so.
    Input:    input1 -- variable to check
    Output: val -- value of float
    """
    try:
        val = float(input1)                   # Only allows input floats
        return val
    except (ValueError, TypeError):
        print('Error, please enter numeric input')
        if exit:
            quit()
        return False


# Check module name since check_for_float is being imported in the next
# exercise. See also, https://www.youtube.com/watch?v=sugvnHA7ElY (video)
# or https://www.tutorialspoint.com/python/python_modules.htm (text)
if __name__ == "__main__":
    count = 0                                 # Initializes values
    total = 0.0
    average = 0.0

    while True:                               # Stays in loop until break
        input_number = input('Enter a number: ')
        if input_number == 'done':
            break                             # Exits the while loop

        number = check_for_float(input_number, False)
        if not number:
            continue

        count += 1                            # Counter
        total = total + number                # Running total

    # Ensures count is not 0 which would cause division error
    if count:
        average = total / count               # Computes the average

    print(total, count, average)