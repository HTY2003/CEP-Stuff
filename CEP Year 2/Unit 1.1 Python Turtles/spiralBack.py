from turtle import *
def spiralBack(sideLen, angle, scaleFactor, minLength):
    '''Draws a spiral. The state of the turtle (position,
       direction) after drawing the spiral should be the 
       same as before drawing the spiral. '''
    # solution
    if sideLen >= minLength:
        fd(sideLen)
        lt(angle)
        spiralBack(sideLen*scaleFactor, angle, scaleFactor, minLength)
        pu()
        rt(angle)   
        bk(sideLen)
        pd()  # the last four lines retrace position without drawing


setup(1.0,1.0)
clear()
reset() 
spiralBack(200,95,0.93,10)
