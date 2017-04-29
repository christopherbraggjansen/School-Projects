###################################################################
#Author: Christopher Jansen: jansenc
#Python Version:2.7
#Purpose: To test practice using functions by playing a guessing game
##################################################################
#Acknowledgements: John Hellrung This code is based on code that John Hellrung showed me.
#I then wrote the code on my own from scratch. John then helped me troubleshoot the code and taught me about the return function.
#Based on instruction found at http://cs.berea.edu/courses/csc226/tasks/a6.functions-shellgame.html
#####################################################################
import random #Imports that random library in order to pick a random shell
import sys #Imports the sys library in order to use sys.exit() if the user wants to exit# import paypal this line imports paypal to facilitate actual betting of money implement in the future (Joke)
def startgame():
    '''
    Asks the user if they would like to play the game. Also keeps track of how many times the user
    has played the game. Does not allow the user to play more than 10 times.
    :return:
    '''
    print ("Lets Play The Shell Game")
    count = 0 # Count of how many times user has played the game
    for n in range(10): # Loop to let the user play only 10 times
        count = count + 1 # Adds 1 to the count to keep track of how many times the user has played.
        play = raw_input ("Do you which to play Y or N?").lower() # .lower() makes input lower case regardless of how it was entered
        if play == "y":
            print ("Good Luck")
            betting() #Calls the betting function with no parameters
        elif play == "skip": #This line of code was used for testing the loop above without having to play the whole game
            print("Skip")
        else: #If user enters N or other character ends the program
            print("Goodbye")
            sys.exit()
        print ("You have played " + str(count) + " times.") # Prints the amount of times the user has played
def betting():
    '''
    The betting function asks the user how much money they have and how much they would like to bet
    sets up the variable tmoney for Total Money and bet for How much the user wants to Bet.
    :return:
    '''
    tmoney = int(raw_input("How much money do you have?:"))
    if tmoney <= 0: # Checks to make sure that the user has money and didn't enter a negative number
        print ("You have to have some money if you want to play!")
        betting() # Calls the betting function again so the user can enter a valid amount
    while tmoney > 0: #If the user has money then asks for a bet
        bet = int(raw_input("How much money would you like to bet?"))
        if tmoney < bet: #Assures that user is not betting more money than they have
            print("You can't bet more money than you have")
        elif tmoney == bet: #Checks if user is betting all their money not necessary, but I wanted to include it
            print ("Putting it all on the line I see. Good Luck!")
            tmoney = guess(bet, tmoney) # Passes parameters bet and tmoney into guess
            print tmoney
        else:
            tmoney = guess(bet, tmoney) # Passes parameters bet and tmoney into guess
            print tmoney



def guess(bet, tmoney):
    '''
    This function lets the user input their guess for what shell they think will be the winner
    :param bet: int Money the user bet
    :param tmoney: int  Total Money
    :return:
    '''
    shell = raw_input("What shell would you like to pick? Left or Center or Right")
    return pc (shell, bet, tmoney)#Calls the pc function with parameters for shell bet and total money
def pc (shell, bet, tmoney):
    '''
    This function has the computer pick a random shell
    :param shell: Users choice of a shell
    :param bet: Users Bet
    :param tmoney: Users Total Money
    :return:
    '''
    pcshell = random.choice(['left', 'center', 'right']) #This code lets the computer pick a random shell from the choice listed
    print ("The computer picked the " + str(pcshell)+ " shell") #Prints out what shell the computer has picked so the user can see that the computer is not cheating.
    return win_lose(shell, pcshell, bet, tmoney) #calls the win_lose function with the parameters shell, pcshell, bet, and tmoney
def win_lose (shell, pcshell, bet, tmoney):
    '''
    This function determines whether the user has won or lost the game by comparing their guess with the computers choice.
    :param shell:  Users choice of a shell
    :param pcshell: Computers pick for a shell
    :param bet:  Users bet
    :param tmoney:  Users Total Money
    :return:
    '''
    if shell.lower() == pcshell: #Compares the computers choice with the users guess
        print ("You Win")
        print ("You currently have")
        tmoney = tmoney + bet # Implements 2:1 betting
        return tmoney
    else:
        print("You Lose")
        print ("You currently have")
        tmoney = tmoney - bet
        return tmoney
def main ():
    '''
    Calls the start game function in order to start the game
    :return:
    '''
    startgame() #Starts the game
main() #Calls Main




