pay = 0.0                                   # Initialize variables

input_hours = input('Enter Hours: ')
input_rate = input('Enter Rate: ')
hours = float(input_hours)                  # Only allows input floats
rate = float(input_rate)                    # Only allows input floats

if hours < 40:
    pay = rate * hours                      # No overtime calculation
else:
    overtime = hours - 40                   # Calculate amount of overtime
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print('Pay: ', pay)