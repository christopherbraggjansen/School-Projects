######################################################################
# Author: Christopher Jansen
#Python version: 2.7
# Purpose: To test out the installation of python and the pyscripter ide
# and to play around with a few features of the python language.
######################################################################
# Acknowledgements:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/courses/csc226/tasks/yourusername-A0.py
######################################################################
import random #This imports the random library to produce a random number for the greeting


# This is how to ask for input from the keyboard:
myname = raw_input('Please enter your name: ')

print('') # This prints a blank line.

#This is a python conditional statement
if myname == 'Chris':
    print('Hello,' + myname + '!' )

elif myname == 'Hacker': # else if
    print('Hacker?')
    print('What are you doing on my computer?')
    print('Get off now!!!')

#This message will display if neither of the above conditions are met
else:
    print('Hello, ' + myname + '!')

#define 4 variables for use in greeting 
greeting1='How are you today?'
greeting2='What is up?'
greeting3='Have a nice day'
greeting4='Howdy'

#Randomly select a greeting from the 4 choices
greetingchoice = random.choice([greeting1,greeting2,greeting3,greeting4])
#Prints the selected greeting
print("\n"+greetingchoice) #The \n tells python to go to a new line before printing the message
