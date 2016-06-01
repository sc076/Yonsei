""" Program that allows user to enter 6 digit
hexadecimal RGB color and converts them to base 10.
1. First two represent - RED
2. Second two - GREEN
3. Third two - BLUE"""

hexadec = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def convert(color):
    """ Converts the colors depending on their hexadecimal
        representation
    """

    col1 = 0
    col2 = 0
    if color[0].isalpha():
        col1 = hexadec.get(color[0])
    else:
        col1 = int(color[0])

    if color[1].isalpha():
        col2 = hexadec.get(color[1])
    else:
        col2 = int(color[1])

    value = col1*16 + col2
    return value

# --- MAIN

color = (input('Enter a color: ')).upper()
red = convert(color[0:2])
green = convert(color[2:4])
blue = convert(color[4:6])

# Outputs the result
print('Red:', red)
print('Blue:', blue)
print('Green:', green)
