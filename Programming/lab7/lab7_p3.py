import turtle

#set windows size
turtle.setup(800, 600)
window = turtle.Screen()

#Initializes a turtle
drawing = turtle.getturtle()
drawing.hideturtle()            #hides the turtle (i.e. the cursor)

#Drawing
drawing.penup()                 #Lifts pen up in order not to draw additional lines
drawing.setposition(-400,300)   #Goes to the top-left corner
drawing.pendown()
drawing.setposition(400,-300)   #Goes to the bottom-right corner drawing line
drawing.penup()
drawing.setposition(400, 300)   #While pen up goes to the top-right corner
drawing.pendown()
drawing.setposition(-400,-300)  #While pen down goes to the bottom left corner drawing a line
turtle.exitonclick()            #Waits for the user to click in order to exit
