input_hours = input('Enter Hours: ')
try:
    hours = float(input_hours)              # Only allows input floats
except ValueError:
    print('Error, please enter numeric input')
    quit()

input_rate = input('Enter Rate: ')
try:
    rate = float(input_rate)                # Only allows input floats
except ValueError:
    print('Error, please enter numeric input')
    quit()

if hours < 40:
    pay = rate * hours                      # No overtime calculation
else:
    overtime = hours - 40                   # Calculate amount of overtime
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print('Pay: ', pay)