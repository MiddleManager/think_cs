import sys

def test(did_pass):
    """ Print the results of a test"""
    linenum = sys._getframe(1).f_lineno # Get caller's linenum

    if not did_pass:
        #msg = ("Test at line {0} ok".format(linenum))
    #else:
        msg = ("Test at line {0} FAILED".format(linenum))
        print (msg)
    #print (msg)
