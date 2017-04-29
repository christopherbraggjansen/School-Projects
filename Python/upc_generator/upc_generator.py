'''
Author: Christopher Jansen
Assignment: CSC 226 Lab 2
Purpose: To take a file containing UPCs in the UPC-A format,to check if the UPC is valid and then either draw the
valid UPC on the screen using the turtle library or draw an error on the screen using the turtle library.
Acknowledgments:
listsum function taken from http://interactivepython.org/ Copyright 2014 Brad Miller,
David Ranum. Created using Sphinx 1.2.2.
testit function taken  from code written by Dr. Scott Heggen
'''
import turtle  # The turtle library is used to draw the error message or the UPC to the screen
import sys  # The sys library is used to get the callers line number in the testit function
def testit(did_pass):   # Taken directly from code written by Dr. Scott Heggen
    '''
    You can call this function to let you know whether a test passed or not
    :param did_pass: True or False
    :return: None prints the results on the screen.
    '''
    """ Print the result of a unit test. """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)  # Prints the passed message
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))  # Prints the failed message
    print(msg)
def upc_test_suite(): # Tests everything that it needs
  testit(open_file("upc-input1.txt", 0)==str("886971299922"))
  testit(open_file("upc-input2.txt", 0)==str("071915024696"))
  testit(open_file("upc-input3.txt", 1)==str("071915024696"))
  testit(remove_newline('123456789012\n')=='123456789012')
  testit(is_UPC_valid('886971299922')==True)
  testit(is_UPC_valid('00001234567') == False)
  testit(is_UPC_valid('123456789013') == False)
  testit(listsum([4,4,4,4]) == 16)
  testit(split_left_right('123456789013') == ['123456', '789013'])
  testit(digit_binary_conv_right('071915')== ['1110010', '1000100', '1100110', '1110100', '1100110', '1001110'])
  testit(digit_binary_conv_left('024696') == ['0001101', '0010011', '0100011', '0101111', '0001011', '0101111'])
  draw_error()  # This calls the function to draw the error on the screen after the user clicks exit on the turtle window
  # This next line runs.
  run_functions('upc-input4.txt', 0)  # This tests the run_functions function to simulate a user imputing correct data.
  draw_upc(  # This tests the draw upc function given the binary for the left and right sides.
    ['1110010', '1000100', '1100110', '1110100', '1100110', '1001110'],
    ['0001101', '0010011', '0100011', '0101111', '0001011', '0101111']
    )
def run_functions(filename, line):
    '''
    This function takes input about what file to open and what line to read and then calls the necessary functions to
    test if the UPC is valid and then if so draw the upc or if not draw an error message. I created this function to
     clean up the main function so that not as much code was under main.
    :param filename: The name of the file as a string that you would like to open make sure that it also includes .txt
    :param line: An integer specifying what line of the file you would like to read the first line is line 0
    :return:
    '''
    upcstring = open_file(filename, int(line))  # Calls open_file function
    if is_UPC_valid(upcstring):  # Calls the is_UPC_valid function
        upclist = []  # Creates an empty list called upclist
        upclist = split_left_right(upcstring)  # adds the output of split_left_right to the upclist
        upcleftb = digit_binary_conv_left(upclist[0]) # returns the binary for the left side
        upcrightb = digit_binary_conv_right(upclist[1]) #returns the binary for the right side
        draw_upc(upcrightb, upcleftb)  # Draws the upc based upon the binary
    else:
        draw_error()  # If UPC is not valid draws an error.
def open_file(filename, line):  # Function works as it should
    '''
    This function opens a file for reading and then passes on one line of that file to the remove_newline function this
    function then returns the specified line from the file without any newline characters.
    :param filename: A string specifying the filename to be opened.
    :param line: The line number of the file that you would like to read.
    :return: The specified line of the specified file minus any newline characters.
    '''
    upcfile = open(filename, "r")
    upclist = upcfile.readlines()
    upcfile.close()
    linenum = int(line)
    upcline = upclist[linenum]  # I chose to read all lines from the file and then just grab the one I needed, I could
    # have also just grabbed one line from the file.
    return remove_newline(upcline)
def remove_newline(upcline):  # This function works correctly
    '''
    This function takes a line read from a file and removes any newline characters. This is useful because newline
    # Characters make the line contain more than just the upc and breaks the functions that are meant to process only
    # numbers. I could have also only taken a slice of the line, but this would have the effect of letting a non valid
    upc that is to long pass because the slice would shorten it.
    :param upcline: The line from the upc file that may contain new line characters.
    :return: upcclean a upc with any newline characters removed.
    '''
    upcclean = ""
    for letter in upcline:
        if letter != "\n":
            upcclean += letter
    return upcclean
def is_UPC_valid(upc):  # This function works as it should
    '''
    Takes one UPC and determines if it is valid using the Modulo Check Character
    returns True or False
    :param upc: The upc that you would like to check if it is valid
    :return: True or False depending on whether the upc is valid or not.

    '''
    if len(upc) == 12:  # The first step is to check if the UPC is 12 digits long because a valid UPC-A code is 12 digits
       # The code bellow uses the Modulo check character as described at http://cs.berea.edu/courses/csc226/tasks/L2.upc.html
        slice = 0
        upc_odd = []
        while len(upc_odd) < 6:
            upc_odd.append(upc[slice])
            slice = slice + 2
        oddsum = listsum(upc_odd)
        oddsum = oddsum * 3
        slice = 1
        upc_even = []
        while len(upc_even) < 5:
            upc_even.append(upc[slice])
            slice = slice + 2
        evensum = listsum(upc_even)
        upcsum = evensum + oddsum
        upcremander = int(upcsum) % 10
        if upcremander == 0:
            upcremander = 0
        else:
            upcremander = 10 - upcremander
        if upcremander == int(upc[11]):
            return True
        else:
            checkdigit = upc[11]
            return False
    else:
        return False
def listsum(numList):  # This function works correctly
    '''
    This function is a modified code from http://interactivepython.org/ Copyright 2014 Brad Miller,
    David Ranum. Created using Sphinx 1.2.2.
    This function gives you the sum of a list of numbers.
    :param numList: A list of integers.
    :return: The sum as an integer.
    '''
    theSum = 0
    for i in numList:
        theSum = theSum + int(i)
    return theSum
def split_left_right(upc):  # This function works probably.
    '''
    This function splits the UPC code into the right side and the left side
    :param upc: This upc we would like to split
    :return: upcright The right side of the upc upcleft The left side of the upc both in one list upcsplit
    '''
    upcleft = upc[0:6]
    upcright = upc[6:12]
    upcsplit =[]
    upcsplit.append(upcleft)
    upcsplit.append(upcright)
    return upcsplit
def digit_binary_conv_right(upcright): # This function works correctly
    '''
    This function converts the right side of the UPC into binary
    :param upcright: the right side of the upc code.
    :return: The binary digits associated with the right side of the upc.
    '''
    rightbinary = []
    for i in upcright:
        if i == '0':
            rightbinary.append('1110010')
        elif i == '1':
            rightbinary.append('1100110')
        elif i == '2':
            rightbinary.append('1101100')
        elif i == '3':
            rightbinary.append('1000010')
        elif i == '4':
            rightbinary.append('1011100')
        elif i == '5':
            rightbinary.append('1001110')
        elif i == '6':
            rightbinary.append('1010000')
        elif i == '7':
            rightbinary.append('1000100')
        elif i == '8':
            rightbinary.append('1001000')
        elif i == '9':
            rightbinary.append('1110100')
        else:
            print('A conversion error has occurred')
    return rightbinary
def digit_binary_conv_left(upcleft): # This function works correctly.
    '''
    This function converts the right side of the UPC into binary
    :param upcright: the right side of the upc code.
    :return: The binary digits associated with the right side of the upc.
    '''
    leftbinary = []
    for i in upcleft:
        if i == '0':
            leftbinary.append('0001101')
        elif i == '1':
            leftbinary.append('0011001')
        elif i == '2':
            leftbinary.append('0010011')
        elif i == '3':
            leftbinary.append('0111101')
        elif i == '4':
            leftbinary.append('0100011')
        elif i == '5':
            leftbinary.append('0110001')
        elif i == '6':
            leftbinary.append('0101111')
        elif i == '7':
            leftbinary.append('0111011')
        elif i == '8':
            leftbinary.append('0110111')
        elif i == '9':
            leftbinary.append('0001011')
        else:
            print('A conversion error has occurred')
    return leftbinary
def draw_upc(upcrightb,upcleftb):
    '''
    This function draws a upc given the binary for both the right and left sides.
    :param upcrightb: The binary for the right half of the upc
    :param upcleftb: The binary for the left half of the upc
    :return: None
    '''
    # The first part of the code sets up the turtle screen.
    wn = turtle.Screen()
    wn.bgcolor("white")
    tess = turtle.Turtle()
    tess.hideturtle()
    tess.pensize(3)
    tess.speed(0)
    # The second part of the code starts the UPC by calling functions to draw
    #  the Left Hand Guard Bars, Tall Center Bars, and Right Hand Guard bars
    # Draw Left Hand Guard Bars
    tess.penup()
    tess.goto(-175, 60)  # Starting location for the UPC
    draw_bars(tess, '101', 220)
    # Draw Right Hand Guard Bars
    tess.penup()
    tess.goto(111, 60)
    draw_bars(tess, '101', 220)
    # Draw Center
    tess.penup()
    tess.goto(-35, 60)
    draw_bars(tess, '01010', 220)
    # Draw Number System Character
    tess.penup()
    tess.goto(-161, 60)
    numbersyschar = upcleftb[0]
    draw_bars(tess,numbersyschar, 220)
    # Draw Modulo Check Bars
    tess.penup()
    tess.goto(85, 60)
    modulocheck = upcrightb[5]
    draw_bars(tess, modulocheck, 220)
    # Draw left
    tess.penup()
    tess.goto(-140, 60)
    for i in range(1,6):
        draw_bars(tess, upcleftb[i], 200)
    # Draw right
    tess.penup
    tess.goto(-20, 60)
    for n in range(0,5):
        draw_bars(tess, upcrightb[n], 200)

    wn.exitonclick()
def draw_bars(turtle, binary, length):  #This function works correctly
    '''
    This function draws the bars for a UPC given the turtle to use, the binary associated with the bars and the length
    the width of every bar will be 3 pixels wide White = 0 Black = 1 Direction 0 = down Direction 1 = up
    :param turtle: The turtle to use
    :param binary: A string containing the binary digits to be drawn
    :param length: The length of the line from top to bottom in pixels
    :return: None
    '''
    direction = 0
    x = turtle.position()[0]
    turtle.setposition(x,60)  # I reset the top of the UPC (y coordinate) each time because the bar code was being draw
    # like stair steps because it was starting at the bottom where the other section left off.
    for i in (binary):
        if i == '0':
            color = ('white')
        elif i == '1':
            color = ('black')
        else:
            color = ('red')  # Only here for error checking if I see red bars I know something is wrong.
        if direction == 0:
            draw_down_line(turtle,color, length)
            direction = 1
        elif direction == 1:
            draw_up_line(turtle, color, length)
            direction = 0
def draw_down_line(turtle, color, long):  # This function works correctly
    '''
    Simply draws I line going down and then turns to prepare for the next line to be drawn
    :param turtle: The turtle to use
    :param color: White or Black
    :param long: The length of the bar
    :return:None
    '''
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(long)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(3)
def draw_up_line(turtle, color, long):  # This function works correctly
    '''
    This function simply draws a line going up and then turns to prepare for the the next line to be draws.
    :param turtle: The turtle to use
    :param color: White or black
    :param long: The length of the bar
    :return:None
    '''
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(long)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(3)
def draw_error():  # This function is working correctly.
    '''
    This function draws an error on the screen using turtle.
    :return: None
    '''
    text = ('Error\nThis is not a valid UPC,\nThis UPC is not real,\nThe product that this UPC came from is not real,\n'
            'Nothing is real,\nIn fact how do you even know that you are even real?\n'
            'You are running a computer program right now,\nHow do you know you are not a computer program\n'
            'Good night user, Good night')
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.hideturtle()
    tess.color("white")
    wn.bgcolor('purple')
    tess.write(text, move=False, align= 'center', font=("Arial", 14, "normal"))
    wn.exitonclick()
def main():
    #upc_test_suite() # Uncomment to use the test suite
    
    #Uncomment to use interactively
    filename = raw_input("What is the name of file which contains the upc codes you would like to test?:")
    line = raw_input("What line of the file would you like to read? Remember the first line is line 0?:")
    run_functions(filename, line)
    
main()
