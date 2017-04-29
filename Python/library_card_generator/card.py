"""
Author: Christopher Jansen
Assignment: Final Project
Purpose: This class seeks to meet the requirements of the Final Lab Project while extending work that I did for Lab 2
to create a class which creates a library card. This project is mainly proof of concept. The barcode does not follow the
UPC standard so could not be read by most bar code scanners. It uses the same binary for numbers on the right and left
sides of the barcode as well as the Left Hand and Right Hand Guard Bars and the Center Bars, and thus is very similar to
a UPC code and a program could be written to read this type of barcode.
Acknowledgements:
Information about assignment requirements from http://cs.berea.edu/courses/csc226/tasks/FP.finalproject.html
Information about Luhn / Mod 10 algorithm from https://en.wikipedia.org/wiki/Luhn_algorithm
Code for luhn_checksum method, is_luhn)valid method and calculate_luhn taken directly from
https://en.wikipedia.org/wiki/Luhn_algorithm
Information for Luhn Checksum also found on http://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers
digit_conv_right, digit_conv_left, draw_upc,draw_bars, draw_down_line, draw_up_line are modified from code which I wrote
for Lab 2 with information for them taken from http://cs.berea.edu/courses/csc226/tasks/L2.upc.html
Information for using date time library from code academy Python course Date and Time section
Information on zfill from http://stackoverflow.com/questions/21620602/add-leading-zero-python
Code to convert list to a string taken directly from http://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
Library Card.gif created by me with inspiration and quotes modified from Welcome to Night Vale which can be found
at http://commonplacebooks.com/
Inspiration for look of card from http://www.triplethreatlibrarian.com/2014/09/night-vale-public-library-card-diy.html
"""
import turtle  # Used to draw Library card with barcode
import random  # Used to create random card number
from datetime import datetime  # Used to calculate the expiration date three years from today's date.


class Card:
    def __init__(self, name, library_name = 'Public Library', number=None):
        """
        This method sets up a object for the Card class
        :param name:  The patrons name for the library card.
        :param library_name:  The name of the library you would like to appear on the card
        :param number: An optional number you can provide.
        :return:
        """
        # First set the name on the library card
        self.name = name

        # Next we set the name of the library
        self.library = library_name

        # Next set the number on the library card, the user has the option of specifying the number they want, but it
        # Must pass the mod 10 check. Otherwise a random number will be provided which passes this test. My program
        # Which uses this class also tests the number before passing it to the program.
        if number != None:  # Checks to see if number was provided
            if self.is_luhn_valid(number):  # If number passes test use it for self.number
                self.number = number
            else:
                self.number = self.make_random_number()  # If number does not pass test use a random number
        else:
            self.number = self.make_random_number()  # If user did not specify a number use a random number

        # Next we split the number for use in drawing the bar code
        self.libleft = self.number[0:8]
        self.libright = self.number[8:17]

        # Now we need to convert both sides to binary we do this using two functions
        self.leftbinary = self.digit_binary_conv_left()
        self.rightbinary = self.digit_binary_conv_right()

        # Next the expiration date is set, we assume library cards are good for 3 years. Follows MM/YY format.
        # Information for this section from code academy Python course Date and Time section
        nowdate = datetime.now()
        month = nowdate.month
        year = nowdate.year
        expmonth = str(month)
        expmonth = expmonth.zfill(2)  # zfill adds a leading zero if one is needed information for zfill found on
        # http://stackoverflow.com/questions/21620602/add-leading-zero-python
        expyearint = int(year) + 3  # Change the 3 to something else if you want the card to expire in more or less than 3 years.
        expyear = str(expyearint)
        expyear = expyear [2:4]  # Makes the Year a two digit number.

        self.exp_date = str(str(expmonth)+"/"+str(expyear))

        # Next we set the pin for the library card
        pin = random.randrange(0, 999)
        pinstring = str(pin)
        pinstring = pinstring.zfill(3)
        self.pin = str(pinstring)

    def make_random_number(self, firstdigit=None):
        """
        This function creates a random number that is 16 digits long which passes the mod 10 test. It allows the user to
        specify a starting digit if they would like to. This could be used for example to give different kinds of
        library patrons different starting digits. I did not implement an option to choose the first number without
        modifying the code, so it is here mainly for possible future use.
        :return: A valid 16 digit number
        """
        random_number = []
        # First take care of the first digit
        # If the user did not specify a starting digit a digit is provided.
        if firstdigit != None:
            random_number.append(firstdigit)
        else:
            random_number.append(random.randrange(1, 10))  # I don't which to have numbers with a leading 0

        # Now find next 14 digits
        for n in range(14):
            random_number.append(random.randrange(0, 10))

        # Now we need to convert list of 15 numbers to string so we can pass them to luhn_checksum we use the ''.join
        # function. Code take directly from http://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
        str1 = ''.join(str(e) for e in random_number)

        #  Now we need to calculate the check digit which is the final digit.
        def calculate_luhn(self, partial_card_number):
            # This function taken directly from https://en.wikipedia.org/wiki/Luhn_algorithm
            check_digit = self.luhn_checksum(int(partial_card_number) * 10)
            return check_digit if check_digit == 0 else 10 - check_digit

        last_digit = calculate_luhn(self, str1)

        random_number.append(last_digit)

        # Now we convert the whole number to a string and return it as long as it passes the test.

        validnumber = ''.join(str(e) for e in random_number)  # Code take directly from http://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
        if self.is_luhn_valid(validnumber):
            return validnumber
        else:
            print("There has been an error Trying to calculate a new card number")
            self.make_random_number()

    def luhn_checksum(self, card_number):  # Code and method docstring taken directly from https://en.wikipedia.org/wiki/Luhn_algorithm
        """
        This code checks the validity of an input with a check digit.
        :param card_number: The number you would like to check
        :return: The checksum for the number should be zero for a valid number.
        """
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10

    def is_luhn_valid(self, card_number):  # Code taken directly from https://en.wikipedia.org/wiki/Luhn_algorithm
        """
        This function simply checks whether the checksum of the whole number is zero as it should be
        :param card_number: The number you would like to check.
        :return: True or False to whether it passed the test
        """
        return self.luhn_checksum(card_number) == 0

    def make_card(self):
        """
        This method calls all the other methods necessary to display the library card it also
        # prints the text on the card.
        :return: None
        """
        wn = turtle.Screen()
        screensizex = 850  # I made the turtle screen slightly bigger than my background so you could see the whole background.
        screensizey = 650
        wn.setup(screensizex, screensizey)
        wn.bgpic('Library Card.gif')
        textturt = turtle.Turtle()
        textturt.hideturtle()
        textturt.penup()
        # We specify the font size used to write the name of library so that it does not go off the screen
        if len(self.library) > 15:
            fontsize = 30
        elif len(self.library) > 20:
            fontsize = 24
        else:
            fontsize = 36
        # The code below writes everything on to the turtle screen and then calls the function to draw the barcode.
        textturt.goto(-40, 230)
        textturt.write(self.library,align='center', font=('stencil', fontsize))
        textturt.goto(-385, 180)
        textturt.write('Patron Name: '+ str(self.name), align='left', font=("Stencil", 24))
        textturt.goto(-385, 150)
        textturt.write('Card Number: '+ str(self.number), align='left', font=("Stencil", 24))
        textturt.goto(-385, 120)
        textturt.write('Expiration Date: '+ str(self.exp_date), align='left', font=("Stencil", 24))
        textturt.goto(-385, 90)
        textturt.write('Pin: '+ str(self.pin), align='left', font=("Stencil", 24))
        self.draw_upc()
        wn.exitonclick()  # Aborts the turtle process and allows for the screen to be closed.

    def digit_binary_conv_right(self):
        '''
        This function converts the right side of the library number into binary
        :return: The binary digits associated with the right side of the number.
        '''
        rightbinary = []
        for i in self.libright:
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
    def digit_binary_conv_left(self):
        '''
        This function converts the right side of the library card number into binary
        :return: The binary digits associated with the right side of the upc.
        '''
        leftbinary = []
        for i in self.libleft:
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
        return leftbinary

    def draw_upc(self):
        '''
        This function draws a upc given the binary for both the right and left sides.
        :param upcrightb: The binary for the right half of the upc in this case pulled from the object attribute
        :param upcleftb: The binary for the left half of the upc in this case pulled from the object attribute
        :return: None
        '''
        upcrightb = self.rightbinary
        upcleftb = self.leftbinary
        tess = turtle.Turtle()
        tess.hideturtle()
        tess.pensize(3)  # This makes every bar 3 pixels wide used for the calculation of the placement of other elements
        tess.speed(0)
        # The second part of the code starts the UPC by calling functions to draw
        #  the Left Hand Guard Bars, Tall Center Bars, and Right Hand Guard bars
        startx = -30
        starty = -97
        # The location for every element is found by first calculating the number of bars assuming 7 bars per number. We
        # Then multiple number of pixels per bar to calculate number of pixels. I also added 10 pixel buffers between the
        # Guard bars and the first and last digit. I did this all ahead of time although the code could be modified to do
        # This in real time.
        # Draw Left Hand Guard Bars
        tess.penup()
        tess.goto(startx, starty)  # Starting location for the UPC
        self.draw_bars(tess, '101', 180)
        # Draw Right Hand Guard Bars
        tess.penup()
        tess.goto(startx + 380, starty)
        self.draw_bars(tess, '101', 180)
        # Draw Center
        tess.penup()
        tess.goto(startx + 187, starty)
        self.draw_bars(tess, '01010', 180)
        # Draw First digit of number
        tess.penup()
        tess.goto(startx + 19, starty)
        firstdigit = upcleftb[0]
        self.draw_bars(tess,firstdigit, 180)
        # Draw Modulo Check Bars
        tess.penup()
        tess.goto(startx + 349, starty)
        modulocheck = upcrightb[-1]
        self.draw_bars(tess, modulocheck, 180)
        # Draw left
        tess.penup()
        tess.goto(startx + 40, starty)
        for i in range(1,8):
            self.draw_bars(tess, upcleftb[i], 150)
        # Draw right
        tess.penup
        tess.goto(startx + 202, starty)
        for n in range(0,8):
            self.draw_bars(tess, upcrightb[n], 150)

    def draw_bars(self, turtle, binary, length):
        '''
        This function draws the bars for a UPC given the turtle to use, the binary associated with the bars and the length
        the width of every bar will be 3 pixels wide White = 0 Black = 1 Direction 0 = down Direction 1 = up
        :param turtle: The turtle to use
        :param binary: A string containing the binary digits to be drawn
        :param length: The length of the line from top to bottom in pixels
        :return: None
        '''
        starty = -97
        direction = 0
        x = turtle.position()[0]
        turtle.setposition(x,starty)  # I reset the top of the UPC (y coordinate) each time because the bar code was being draw
        # like stair steps because it was starting at the bottom where the other section left off.
        for i in (binary):
            if i == '0':
                color = ('white')
            elif i == '1':
                color = ('black')
            else:
                color = ('red')  # Only here for error checking if I see red bars I know something is wrong.
            if direction == 0:
                self.draw_down_line(turtle, color, length)
                direction = 1
            elif direction == 1:
                self.draw_up_line(turtle, color, length)
                direction = 0

    def draw_down_line(self, turtle, color, long):  # This function works correctly
        '''
        Simply draws a line going down and then turns to prepare for the next line to be drawn
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

    def draw_up_line(self, turtle, color, long):  # This function works correctly
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
