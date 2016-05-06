import turtle

def drawSquare(myturtle, x, y, a):
    """Draw a square on the screen.

        turttle is the drawing object to be used.
        x and y specify the x and y coordinates of the
        lower left corner of the square.
        a is the length of each side of the square.
        x, y, and a are given in units of pixels.
    """

    #Start drawing the square with visible pointer
    myturtle.penup()
    myturtle.setposition(x, y)
    myturtle.pendown()
    myturtle.setposition(x+a, y)
    myturtle.setposition(x+a, y+a)
    myturtle.setposition(x, y+a)
    myturtle.setposition(x, y)
