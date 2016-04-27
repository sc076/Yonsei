#Bouncing Balls simulation program
import turtle
import random
import time

def atLeftEdge(ball, screen_width):
    if ball.xcor() < -screen_width /2:
        return True
    else:
        return False

def atRightEdge(ball, screen_width):
    if ball.xcor() > screen_width/2:
        return True
    else:
        return False

def atTopEdge(ball, screen_height):
    if ball.ycor() > screen_height/2:
        return True
    else:
        return False

def atBottomEdge(ball, screen_height):
    if ball.ycor() < -screen_height/2:
        return True
    else:
        return False

def bounceBall(ball, new_direction):
    #Random numbers in order to create color in RGB
    clr_r = random.randrange(0, 257, 10)
    clr_g = random.randrange(0, 257, 10)
    clr_b = random.randrange(0, 257, 10)
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading = 360 - ball.heading()

    #Set the object filling with the randomly generated collor
    ball.color((clr_r, clr_g, clr_b))
    return new_heading

def createBalls(num_balls):
    balls = []
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)
        new_ball.pendown()         #Draws the ball's path
        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)

    return balls

#main
#program greeting
print('This program simulates bouncing balls in a turtle screen')
print('for a specified number of seconds')

#init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)

#create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')
window.colormode(255)

#promt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = int(input('Enter number of balls in simulation: '))

#create balls
balls = createBalls(num_balls)

#set start time
start_time = time.time()

#begin simulation
terminate = False

while not terminate:
    for k in range(0, len(balls)):
        balls[k].forward(15)

        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'right'))
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'left'))
        elif atTopEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'down'))
        elif atBottomEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'up'))

        if time.time() - start_time > num_seconds:
            terminate = True

#exit on close window
turtle.exitonclick()
