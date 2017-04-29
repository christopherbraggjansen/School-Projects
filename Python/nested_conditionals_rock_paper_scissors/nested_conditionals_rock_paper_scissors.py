######################################################################
# Author: Christopher Jansen
#Python version: 2.7
# Purpose: As a class demonstration of nested if statements
# using multiple elif keywords
######################################################################
# Acknowledgements:Original program from Dr. Jan Pearce.
# Information on exit commands from https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
######################################################################
import time          # import a library with time.sleep()
import random        # import a library with random.choice()

# First the user must choose what character they want to play and we must display this choice.
print('Lets Play Rock Paper Scissors Spock Lizard')
print('The rules of this game can be found online at http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock')
myinput = raw_input('Please choose something from above using all lower case letters:')

# Checks to make sure user enters legal value
if myinput == 'rock' or myinput == 'paper' or myinput == 'scissors' or myinput == 'spock' or myinput == 'lizard':
    print('You Chose: ' + myinput + ' Good Luck!')
else:
    print'Please try entering your choice again insuring correct spelling and the use of all lower case letters'
    exit()

print('') # This prints a blank line.
#Next the computer must choose a character to play this is done using the random library which we imported above.
choice1='rock'
choice2='paper'
choice3='scissors'
choice4="lizard"
choice5="spock"


somechoice = random.choice([choice1, choice2, choice3, choice4, choice5])

time.sleep(0.5)
print('Lets see what the computer chooses')
print('') # This prints a blank line.

# This part of the code compares the users choice with the computer choice and determines a winner
# First the code if the computer choices rock
if somechoice == 'rock':
    print ('The computer chose rock watch out Lizards and Scissors')
    if myinput == 'lizard' or myinput == 'scissors':
        print ('... and you die.')
        exit() # This line of code exits the program so the program does not continue to run and print 'You Won'
    elif myinput == 'rock':
        print ('You tie, you die')
    else:
        print ('You won')
# The code if the computer chooses paper
elif somechoice == 'paper':
    print ('The computer chose paper (Thankfully not the academic kind) watch out Spock and Rock')
    if myinput == 'spock' or myinput == 'rock':
        print ('... and you die.')
        exit()
    elif myinput == 'paper':
        print ('You tie, you die')
    else:
        print ('You won')
# The code if the computer chooses scissors

elif somechoice == 'scissors':
    print ('The computer chose scissors after it runs with them they will cut paper and Lizards')
    if myinput == 'paper' or myinput == 'lizard':
        print ('... and you die.')
        exit()
    elif myinput == 'scissors':
        print ('You tie, you die')
    else:
        print ('You won')
# The code if the computer chooses lizard
elif somechoice == 'lizard':
    print ("The computer chose Lizard don't laugh we might have evolved from them also Lizards kill Spock and Paper")
    if myinput == 'paper' or myinput == 'spock':
        print ('... and you die.')
        exit()
    elif myinput == 'lizard':
        print ('You tie, you die')
    else:
        print ('You won')

# The code if the computer chooses spock
elif somechoice == 'spock':
    print ("The computer chose spock")
    if myinput == 'paper' or myinput == 'spock':
        print ('... and you die.')
        exit()
    elif myinput == 'spock':
        print ('You tie, you die')
    else:
        print ('You won')



