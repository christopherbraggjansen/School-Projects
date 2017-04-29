'''
Author: Christopher Jansen
Python Version: 2.7
Acknowledgments: Life path numbers based on http://www.tokenrock.com/numerology/life-path-2.html
Based on and function descriptions taken from http://cs.berea.edu/courses/csc226/tasks/a9.lifepath.html
'''
def main():
    """
    Main function calls all the other functions and sets up variables that will be based to the functions
    """
    byear = raw_input("What is the Year of Your Birthday in YYYY format?:")  # Has the user input their birth year
    bmonth = raw_input("What is the Month of Your Birthday in MM format?:")  # Has the user input their birth month
    bday = raw_input("What is the day of your birthday in DD format?:")  # Has the user input their birth day
    bmonth = month(bmonth)  # Calls the month function and then sets bmonth equal to the output of the month function
    bday = day(bday)  # Calls the day function and then sets bday equal to the output of the day function
    byear = year(byear)  # Calls the year function and then sets byear equal to the output of the year function
    number = total(bmonth, bday, byear)  # Calls the total function and sets number equal to the output of the function.
    print("Your life path number is " + str(number))  # Gives the user their life path number
    print("To find out more about your life path number visit " + "http://www.tokenrock.com/numerology/life-path-" +
          str(number) + ".html")  # Displays a url where the user can find out more information about.
    # This is here to meet the requirement Does something creative and interesting while informing the user of their Life Path Number.

def month(MM):
    """
     This function Converts the number of the birth month to digits and sum them unless the month is November,
      in which case it is left as an 11.
      MM: Month input above
      returns sum of digits or 11
    """
    if int(MM) == 11:
        print("You have a power month")
        return int(11)
    else:
        M0 = str(MM)[0]
        M1 = str(MM)[1]
        MT = int(M0) + int(M1)
        return MT
def day(DD):
    """
    This function Converts the birthday day to digits and sum these unless the day is the 11th or the 22nd,
     in which case the 11 and 22 are left as an 11 or a 22.
     DD: Day input from above
     returns sum of digits or 22 or 11
    """
    if int(DD) % 11 == 0:
        print ("You have a power day")
        return int(DD)
    else:
        D0 = str(DD)[0]
        D1 = str(DD)[1]
        DT = int(D0) + int(D1)
        return int(DT)
def year(YYYY):
    """
    This function Converts the year to 4 digits, and sum the four digits.
    YYYY: The year input from above
    returns sum of digits of year
    """
    Y0 = str(YYYY)[0]
    Y1 = str(YYYY)[1]
    Y2 = str(YYYY)[2]
    Y3 = str(YYYY)[3]
    YT = int(Y0) + int(Y1) + int(Y2) + int(Y3)
    if int(YT) % 11 == 0:
        return YT
    elif YT > 9:
        YT0 = str(YT)[0]
        YT1 = str(YT)[1]
        YTT = int(YT0) + int(YT1)
        if int(YTT) < 10:
            return int(YTT)
        else:
            YTT0 = str(YTT)[0]
            YTT1 = str(YTT)[1]
            YTTT = int(YTT0) + int(YTT1)
            return YTTT
    else:
        return YT
def total (MM, DD, YYYY):
    """
    This function Adds all the digits together from Steps 1, 2, and 3. Reduces this total sum further
     by adding the remaining digits together until a single digit or a Master Number is obtained.
     MM: Output of Month function
     DD: Output of Day function
     YYYY: Output of Year function
     returns master number
    """
    t = int(MM) + int(DD) + int(YYYY)
    if int(t) % 11 == 0:
        return t
    elif t > 9:
        T0 = str(t)[0]
        T1 = str(t)[1]
        TT = T0 + T1
        if TT > 9:
            TT0 = str(TT)[0]
            TT1 = str(TT)[1]
            TTT = int(TT0) + int(TT1)
            return TTT
        else:
            return TT
    else:
        return t
main()

