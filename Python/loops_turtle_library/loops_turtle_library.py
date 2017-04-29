######################################################################
# Author: Christopher Jansen
#Python version: 2.7
# Purpose: To Design a python script that uses loops, and turtle graphics to create something cool.
######################################################################
# Acknowledgements: Original Program by Dr. Jan Pearce
######################################################################
sides=int(raw_input('How many sides would you like your shape to have (3-6)?'))
turtlecolor=str(raw_input("What color would you like your turtle (white will not show on background)?"))
import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window--needed for a clean close
wn.title("Shape")
wn.bgcolor('white')
myturtle = turtle.Turtle()  # create a turtle named myturtle
myturtle.shape('classic')    # shapes possible are 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
myturtle.color(turtlecolor)
myturtle.hideturtle()
myturtle.pensize(5)
myturtle.speed(1)
myturtle.setpos(0,0)
myturtle.begin_fill()
for i in range(sides):
    myturtle.forward(150)
    myturtle.right (360/sides)
myturtle.fill(False)
myturtle.end_fill()
myturtle.up()
myturtle.setpos(50,100)
myturtle.write("Nice Shape",move=False,align='center',font=("Arial",30,("bold","normal")))
wn.exitonclick()            # Added by Dr. Pearce to wait for a user click on the canvas
