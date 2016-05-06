import turtle

def drawCircle(myturtle, x, y, r):
    """ Draw a circle on the screen.

        turtle is the drawing object to be used.
        x and y are the x and y coordinates of the circle's center.
        r is the radius of the circle.
        All measures are given in units of pixels.
    """

    #Getting new turtle object and draws circle
    myturtle.penup()
    myturtle.setposition(x, y)
    myturtle.pendown()
    myturtle.circle(r)
