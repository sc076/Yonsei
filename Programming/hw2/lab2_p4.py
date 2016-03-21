#Temperature conversion Program (Celsius to Fahrenheit)

#Will convert temp entered in Celsius to Fahrenheit

print('This program will convert degrees Celsius to degrees Fahrenheit')

#Get the input from the user
cel = float(input('Enter degrees Celsius: '))

#calculations
fahren = (cel*(9/5))+32

#output
print(cel, 'degrees Celsius equals', format(fahren, '.1f'), 'degrees Fahrenheit')
