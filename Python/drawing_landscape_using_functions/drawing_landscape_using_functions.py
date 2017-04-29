#################################################################################
# Author: Christopher Jansen: jansenc
# Python Version 2.7
#Purpose: To test practice using functions by drawing a landscape
######################################################################
# Acknowledgements: Code original work
# bliss.gif Copywrite Microsoft downloaded from http://windows-xp-bliss-screen-saver.jp.brothersoft.com/screenshot-2975.html
#################################################################################
import turtle
def main():
    '''
    This is the main function it sets up the screen for the turtle to draw in and calls the functions to draw the
    mountains and the stars.
    '''
    wn = turtle.Screen()  # Creates a Screen for the turtle to draw in.
    wn.bgcolor ("green")  
    trt = setuptrt()  # Calls the function to set up the turtle and then sets the turtle as trt so we can call it later
    trt.penup()  # Lifts the pen so we can move into position without drawing on the screen
    trt.setpos(-300, -200)  # Sets up the turtle in the right place
    trt.pendown()  # Puts the pen down so we can draw again
    for n in range(2):  # Calls the mountain function twice with the color brown
        MTN(trt, "brown")
        trt.forward(100)
    for m in range(2):  # Calls the mountain function twice with the color white
        MTN(trt, "white")
        trt.forward(100)
    MTN(trt, "red")  # Calls the mountain function once with the color red
    trt.penup()  # Lifts the pen up so we can move into position for the stars
    trt.setpos(-300,200)  # Positions the turtle to draw the stars
    trt.pendown()
    for x in range(4):  # Calls the star function four times to draw four stars
        Star(trt, "yellow")
        trt.penup()
        trt.forward(150)
        trt.pendown()
    wn.exitonclick()  # Aborts the turtle drawing and prepares screen to close

def setuptrt():
    '''
    This function creates the turtle that we will be using to draw all the shapes.
    '''
    tess = turtle.Turtle()
    tess.hideturtle()
    return tess
def MTN(trt, clr):
    """
    This function draws the mountains
    trt: The turtle that we will use
    clr: The color that we want the mountain to be
    """
    trt.color(clr)
    trt.begin_fill()
    for s in range(3):
        trt.forward(200)
        trt.right (-120)
    trt.end_fill()
def Star(trt, clr):
    """
    This function draws a star
    trt: The turtle we will be using
    clr: The color we want our turtle to be.
    """
    trt.color(clr)
    trt.begin_fill()
    for i in range(5):
        trt.forward(100)
        trt.right (144)
    trt.end_fill()
main()  # Calls main to get the whole program started
