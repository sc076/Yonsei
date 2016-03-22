#Asks the user for EAN
ean = input('Enter the first 12 digits of an EAN: ')

#Checks if it is 12 digits
while len(ean) == 12:
    ean = input('Enter the first 12 digits of an EAN: ')

#Sums even and odd numbers
i = 1
odd = 0
even = 0
for num in ean:
    if i%2 == 0:
        even += int(num)
    else:
        odd += int(num)
    i += 1

#Makes calculations following the given steps
odd += (even*3) 
odd -= 1
reminder = odd%10
reminder = 9 - reminder

#Outputs the results
print('Check digit:', reminder)
