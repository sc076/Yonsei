# Fahrenheit to Celsius conversion program

fahren = float(input('Enter degrees Fahrenheit: '))
celsius = (fahren - 32) * 5 / 9
print(fahren, 'degrees Fahreheit equals',
      format(celsius, '.1f'), 'degrees Celsius')
