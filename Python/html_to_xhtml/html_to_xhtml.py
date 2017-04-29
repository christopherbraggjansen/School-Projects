'''
Author: Christopher Jansen
Python Version: 2.7
Purpose: To take a file containing HTML source code and change it to be XHTML compatible by modifying the following tags
<meta>,<img src>,<br>,<hr>
Acknowledgments: testit function taken  from code written by Dr. Scott Heggen
'''

import sys  # The sys library is used to get the callers line number in the testit function as well as exit the program
import os.path # This library is used to check if a file exists.

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

def xhtml_test_suite():  # This test suite is used to test each function while it is being developed
    samplehtmllist0 = ['<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n',
                      '<html xmlns="http://www.w3.org/1999/xhtml">\n', '<head>  \n',
                      '  <meta content="text/html;charset=UTF-8" http-equiv="Content-Type">\n',
                      '  <title>Basic Web Page</title>\n', '</head>\n', '<body>\n', '<h3>A Basic Web Page</h3>\n',
                      '\n', '<p>A basic web page looks something like this. It might have\n', 'images like:<br>\n',
                      '\n', '<img style="width: 66px; height: 44px;" alt="WC3 image" src="wc3.gif">\n', '<br>\n',
                      'And it might have a line like:\n', '</p>\n', '\n', '<hr>\n',
                      '<p>Be sure to "view source" of this page.</p>\n', '</body>\n', '</html>']
    samplehtmllist1 = ['<html>\n', '<head>\n', '<title>\n', 'A test web page\n', '</title>\n', '</head>\n', '</html>']

    testit(is_valid_file('basic.html')== True)
    testit(is_valid_file('nosuchfile.html')==False)
    testit(file_to_list('test.html')== samplehtmllist1)
    testit(find_meta(samplehtmllist0) == [3])
    testit(find_meta(samplehtmllist1)== ("none"))
    testit(find_img_src(samplehtmllist0)==[12])
    testit(find_img_src(samplehtmllist1)==("none"))
    testit(find_br(samplehtmllist0)==[10, 13])
    testit(find_br(samplehtmllist1)==("none"))
    testit(find_hr(samplehtmllist0)== [17])
    testit(find_hr(samplehtmllist1)==("none"))
def is_valid_file(filename):
    '''
    This function tests whether the file the user specified exits or not.
    :param filename: The filename of the file you would like to test
    :return: True or False
    '''
    return os.path.isfile(filename)

def file_to_list(filename):
    """
    This function converts a html file to a list with every line as a different element in that list.
    :param filename:  The filename of the file you would like to convert
    :return: A list with every line as a different element of that list
    """
    htmlfile = open(filename, "r")
    htmllist = htmlfile.readlines()
    htmlfile.close()
    return htmllist

def find_meta(htmllist):
    """
    This function finds instances of the meta tag given a list containing html and returns what line number (item in the
    list) an instance was found.
    :param htmllist: The html file is list format you would like to test
    :return: "None" or list index
    """
    listoflines = []
    for i in range(len(htmllist)):
        if "<meta" in htmllist[i]:
            listoflines.append(i)
    if listoflines == []:
        return "none"
    else:
        return listoflines

def find_img_src(htmllist):
    """
    This function finds instances of the img src tag given a list containing html and returns what line number
     (item in the list) an instance was found.
    :param htmllist: The html file is list format you would like to test
    :return: "None" or list index
    """
    listoflines = []
    for i in range(len(htmllist)):
        if "<img" in htmllist[i]:
            listoflines.append(i)
    if listoflines == []:
        return "none"
    else:
        return listoflines

def find_br(htmllist):
    """
    This function finds instances of the br tag given a list containing html and returns what line number (item in the
    list) an instance was found.
    :param htmllist: The html file is list format you would like to test
    :return: "None" or list index
    """
    listoflines = []
    for i in range(len(htmllist)):
        if "<br" in htmllist[i]:
            listoflines.append(i)
    if listoflines == []:
        return "none"
    else:
        return listoflines

def find_hr(htmllist):
    """
    This function finds instances of the hr tag given a list containing html and returns what line number (item in the
    list) an instance was found.
    :param htmllist: The html file is list format you would like to test
    :return: "None" or list index
    """
    listoflines = []
    for i in range(len(htmllist)):
        if "<hr" in htmllist[i]:
            listoflines.append(i)
    if listoflines == []:
        return "none"
    else:
        return listoflines

def fix_meta(htmllist, lines):
    """
    This function takes the lines from a html file in list for and changes any instances of html style meta tags and
    changes them into xhtml style by adding a slash
    :param htmllist: The html file you would like to modify with each line of the source as a string
    :param lines: The lines which contain the tag your looking for
    :return: A modified htmllist containing the changed code.
    """
    for m in lines:
        line = htmllist[m]
        if ">" in line:
            for i, c in enumerate(line):
                if c == ">":
                    newline = line[0:i] + " /" + line[i:len(line)+1]
                    htmllist[m] = newline
        else: return htmllist
    return htmllist

def fix_img_src(htmllist, lines):
    """
    This function takes the lines from a html file in list for and changes any instances of html style img src tags
     and changes them into xhtml style by adding a slash
    :param htmllist: The html file you would like to modify with each line of the source as a string
    :param lines: The lines which contain the tag your looking for
    :return: A modified htmllist containing the changed code.
    """
    for m in lines:
        line = htmllist[m]
        if ">" in line:
            for i, c in enumerate(line):
                if c == ">":
                    newline = line[0:i] + " /" + line[i:len(line)+1]
                    htmllist[m] = newline
        else: return htmllist
    return htmllist

def fix_br(htmllist, lines):
    """
    This function takes the lines from a html file in list for and changes any instances of html style br tags and
    changes them into xhtml style by adding a slash
    :param htmllist: The html file you would like to modify with each line of the source as a string
    :param lines: The lines which contain the tag your looking for
    :return: A modified htmllist containing the changed code.
    """
    for m in lines:
        line = htmllist[m]
        if ">" in line:
            for i, c in enumerate(line):
                if c == ">":
                    newline = line[0:i] + " /" + line[i:len(line)+1]
                    htmllist[m] = newline
        else:
            return htmllist
    return htmllist

def fix_hr(htmllist, lines):
    """
    This function takes the lines from a html file in list for and changes any instances of html style hr tags and
    changes them into xhtml style by adding a slash
    :param htmllist: The html file you would like to modify with each line of the source as a string
    :param lines: The lines which contain the tag your looking for
    :return: A modified htmllist containing the changed code.
    """
    for m in lines:
        line = htmllist[m]
        if ">" in line:
            for i, c in enumerate(line):
                if c == ">":
                    newline = line[0:i] + " /" + line[i:len(line)+1]
                    htmllist[m] = newline
        else: return htmllist
    return htmllist

def run_functions(oldfile, newfile):
    '''
    This function runs the other function necessary to accomplish the goal of translating html to xhtml
    :param oldfile: The file you wish to convert.
    :param newfile:  The file you wish to output to.
    :return: None
    '''
    if is_valid_file(oldfile):
        htmllist = file_to_list(oldfile)
        metalist = find_meta(htmllist)
        imglist = find_img_src(htmllist)
        brlist = find_br(htmllist)
        hrlist = find_hr(htmllist)
        htmllist = fix_meta(htmllist, metalist)
        htmllist = fix_img_src(htmllist, imglist)
        htmllist = fix_br(htmllist, brlist)
        htmllist = fix_hr(htmllist, hrlist)
        htmlliststring = ''.join(htmllist)
        newxhtml = open(newfile, "w")
        newxhtml.write(htmlliststring)
        print("Your file conversion is complete.")
    else:
        print("The file you specified is not valid. Program will exit now")
        sys.exit()

def main():
    #  xhtml_test_suite()   # Uncomment to use interactively.

    oldhtm = raw_input("What is the name of the html file you would like to open?\n"
                       "Please put this in the name.htm or name.html format:")
    newxhtml = raw_input("What is the name of new file you would like to create?\n"
                        "Please put this in the name.html or name.html format:")
    run_functions(oldhtm, newxhtml)

main()
