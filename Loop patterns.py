count=0
for itervar in (3,41,12,9,74,15):
    count = count +1
print ('Count:', count)


total=0

for itervar in (3,41,12,9,74,15):
    total=total+itervar
print ('Total:', total)

largest = None
print ('Before:', largest)
for itervar in (3,41,12,9,74,15):
    if largest is None or itervar > largest:
        largest=itervar
        print ('Loop:', itervar, largest)
print ('Largest:', largest)

smallest=None
print ('Before:', smallest)
for itervar in (3,41,12,9,74,15):
    if smallest is None or itervar < smallest:
        smallest=itervar
        print ('Loop', itervar, smallest)
print ('Smallest:', smallest)

def min (values):
    smallest=None
    for value in values:
        if smallest is None or value < smallest:
            smallest=value
    return smallest 