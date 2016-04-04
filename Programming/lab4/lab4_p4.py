#Tempreture conversion program
#Error checking

#Display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

#Gwt temperature to convert
which = input('Enter selection: ')

while which != 'F' and which != 'C':
    which = input("Please enter 'F' or 'C': ")

temp = int(input('Enter temperature to convert: '))

#Error check
if which == 'F' and temp < (-459.67):
    while temp < -459.67:
        temp = int(input('Enter temperature to convert: '))
elif which == 'C' and temp < -273.15:
    while temp < -273.15:
        temp = int(input('Enter temperature to convert: '))



#Determine temperature conversion needed and display results
if which == 'F':
    converted_temp = format((temp - 32)* 5/9, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    converted_temp = format((9/5 * temp) + 32, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
