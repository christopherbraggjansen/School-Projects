######################################################################
# Author: Christopher Jansen
#Python Version: 2.7
# Purpose: To learn more about lists of lists and deep copies by editing images
#in the ppm format
######################################################################
# Acknowledgements:
# Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
# working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter
#   Modified from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-L3-ppm.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################

import time
from ppm import *
# Be sure you work with a single ppm object at a time

def main():
    '''
    This function sets up a ppm object and calls the method that the use would like to run on the object.
    '''

    wn = PPM_set_up()

    print("\nWelcome to the PPM introduction!\n")

    ppmdefault=PPM(wn) # uses default file
    ppmdefault.PPM_display()
    print("---")

    filename=raw_input("Please input name of PPM-P3 file: ")
    operation=raw_input('What would you like to do to the image?\n[1]Make red\n[2]Grey scale\n[3]Negative\n'
                        '[4]Flip Horizontal\n[5]Rotate Clockwise\n[6]Salt and Pepper Noise\nPlease Enter Selection:')
    ppmobject=PPM(wn, filename)
    if int(operation) == 1:
        ppmobject.PPM_make_red()
    elif int(operation) == 2:
        ppmobject.PPM_greyscale()
    elif int(operation) == 3:
        ppmobject.PPM_negative()
    elif int(operation) == 4:
        ppmobject.PPM_flip_horizontal()
    elif int(operation) == 5:
        ppmobject.PPM_rotateclockwise()
    elif int(operation) == 6:
        noise = raw_input('How much noise would you like to have in your picture 1 is little 5 is lots:')
        if int(noise) == 1:
            ppmobject.PPM_salt_pepper(50)
        elif int(noise) == 2:
            ppmobject.PPM_salt_pepper(30)
        elif int(noise) == 3:
            ppmobject.PPM_salt_pepper(20)
        elif int(noise) == 4:
            ppmobject.PPM_salt_pepper(10)
        elif int(noise) == 5:
            ppmobject.PPM_salt_pepper(6)
        else:
            ppmobject.PPM_salt_pepper(10)
    ppmobject.PPM_display()


    print("---")

    ppmtestlist=PPM(wn) # uses default file
    # The following is a very small image list which differs from the default image
    testlist=[[[0, 0, 255], [0, 255, 0], [0, 30, 30]],
    [[40, 40, 40], [50, 50, 50],[60, 60, 60]]]
    ppmtestlist.PPM_updatefrompixellist(testlist, "very_small.ppm")
    ppmtestlist.PPM_display()

    print("\nPush the Quit button to exit all files.")

    PPM_render(wn) # needed to render all of the images you have instantiated

main()
