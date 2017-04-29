'''
Author:Christopher Jansen
Assistance with math provided by: Bhawesh Mishra
Purpose: This program helps you calculate x and y coordinates to use in the python turtle library given coordinates
from a photo editing program such as paint. This program works best if your turtle window has a background of a set size
that you can reference you then get the coordinates for the point you want reference in paint and this program will
provide you will the corresponding turtle x, y coordinates. This is necessary because photo editing programs usually set
0, 0 to be the upper left hand corner of a picture. Turtle sets 0, 0 to be the middle of the picture.
Disclaimer: This program is provided as-is the author does not guarantee the accuracy of the result in every case
always double check your work. Paint is a trademark of Microsoft Corporation
This work is licensed under a Creative Commons Attribution 4.0 International License.
'''
def turtle(sx, sy, px, py):
    '''
    This function does the actual mathematical conversion
    :param sx: The width of the turtle canvas
    :param sy: The height of the turtle canvas
    :param px: The x coordinate provided by paint
    :param py: The y coordinate provided by paint
    :return:
    '''
    sx2 = sx/2
    sy2 = sy/2
    if px < sx2:
        tx = (sx2 - px) * -1
        print ("X = " + str(tx))
    elif px == sx2:
        print ("X = 0")
    elif px > sx2:
        tx = px - sx2
        print ("X = " + str(tx))
    ty = sy2 - py
    print ("Y = " + str(ty))
def main():
    screenx = int(raw_input("What is the width of your canvas?:"))
    screeny = int(raw_input("What is the height of your canvas?:"))
    print ("Your canvas size is " + str(screenx) + " X " + str(screeny))
    paintx = int(raw_input("What is the X coordinate given by your photo editor?:"))
    painty = int(raw_input("What is the Y coordinate given by your photo editor?:"))
    print ("The corresponding turtle coordinate is")
    turtle(screenx, screeny, paintx, painty)
main()




























