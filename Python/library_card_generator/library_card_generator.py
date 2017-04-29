"""
Author: Christopher Jansen
Python Version: 2.7
Purpose: The purpose of this program is to create a library card using the card class.
Acknowledgements: All code for Final Project.py is my original code. Information for mode 10 from
https://en.wikipedia.org/wiki/Luhn_algorithm
Please refer to card.py for full acknowledgements for the Card class, as that class includes other peoples work.
"""
from card import Card  # Imports the Card class from the file card.py

def main():
    name = raw_input('What name would you like on the library card?:\n')  # Input field for patrons name.
    library= raw_input('What is the name of your library?:\n')  # Optional Input field for library name.
    # The code bellow lets a user specify a 16 digit library card number, if they have one. The number must pass the
    # mod 10 test. This is mainly for testing purposes, but could be useful if you want to keep track of what numbers
    # have been issued.
    numberyn = raw_input('Do you have a 16 digit number you would like to use? Y or N:')
    if numberyn.lower() == 'y' or numberyn.lower() == 'yes':
        number = raw_input('What is the number you would like to use?:')
        newcard = Card(name, library, number)  # This creates a newcard object with the given number so that we can test
        # the number.
        if newcard.is_luhn_valid(number):
            newcard = Card(name, library, number)  # If the number passes the test we use it.
        else:
            print('That is not a valid 16 digit number which passes the mod 10 check')
            print('A Random number will be provided for you')
            newcard = Card(name, library)  # If the number does not pass the test we leave the number field blank.
    else:
        newcard = Card(name, library)
    print('Check the Turtle window for your library card')
    newcard.make_card()  # This code calls the make card function in order to make the card on the screen.
main()
