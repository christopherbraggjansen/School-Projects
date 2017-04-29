#################################################################################
# Author: Christopher Jansen
# Python Version: 2.7
#Purpose: A python implementation of Dr. Nim
#################################################################################
import random
import sys
def main():
    x = setup()
    print ("Ok so your starting the game with " + str(x) + " balls. Good Luck!")
    while x != "userwins" and x != "pcwins":
        x = usersturn(x)
        if x != 0:
            print ("Its the computers turn")
            x = pcsturn(x)
        elif x == 0:
            x = "userwins"
    if x == "userwins":
        print("You took the last ball you win")
    elif x == "pcwins":
        print ("The computer took the last ball you lose")
def setup():
    """
    This function aks the user for input to set up how many balls the game will start with.
    :return: Total Starting balls
    """
    play = raw_input("Would you like to play a game (yes or no):").lower()
    if play == "no" or play == "n":
        print("Fine then I have it your way good bye you ungrateful person.")
        sys.exit()
    elif play == "yes" or play == "y":
        print ("Ok Lets play to play simply select how many balls you would like to take on your turn then"
               " the computer will do the same, if you take the last ball you win.")
    else:
        setup()
    balls = 0  # Sets the ball count to zero so below loop will work.
    while balls < 15:
        balls = int(raw_input("How many balls would you like to start the game with? the number must be greater than or"
                              " equal to 15:"))
    return balls

def usersturn(tballs):
    """
    This function takes the input of the number of balls the user would like to take
    :param tballs:  Total Balls before user's current turn
    :return: Total Balls left after users selection
    """
    uballs = 0
    while uballs >4 or uballs <1:
        uballs = int(raw_input("How many balls would you to take between 1 and 4"))
    if uballs > tballs:
        print("You can't take more balls than the total")
        usersturn(tballs)
    else:
        print("You are choosing to take " + str(uballs) + " Balls")
        tballs = tballs - uballs
        print ("There are " + str(tballs) + " Balls Left")
        return tballs

def pcsturn(tballs):
    """
    This function calculates how many balls the computer would like to take.
    :param tballs: Total Balls before computer's current turn
    :return: Total Balls left after the users selection, or that the computer has won.
    """
    left = tballs % 5
    if left >= 1:
        took = left
        tballs = tballs - took
    else:
        took = random.randint(1, 4)
        tballs = tballs - took
    print ("The computer took " + str(took) + " ball/s. There are " + str(tballs) + " Left")
    if tballs > 0:
        return tballs
    elif tballs == 0:
        return "pcwins"
    else:
        print "Sorry an error has occurred the pc tried to take more balls than there were"
        sys.exit()  # In place for testing to prevent an error and let me know what was happening.
main()
