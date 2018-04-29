from turtle import *
def spiral(sideLen, angle, scaleFactor, minLength):
    '''sideLen is the length of the current side;
       angle is the amount the turtle turns left to draw the next side;
       scaleFactor is the multiplicative factor by which to scale the next side 
       (it is between 0.0 and 1.0);
       minLength is the smallest side length that the turtle will draw.
    '''
    # solution
    if sideLen >= minLength:
        fd(sideLen)
        lt(angle)
        spiral(sideLen*scaleFactor, angle, scaleFactor, minLength)

setup(1.0,1.0) #full screen
spiral(200,90,0.9,10)
clear()
reset()
spiral(200,72,0.97,10)
clear()
reset()
spiral(200,80,0.95,10)
clear()
reset()
spiral(200,121,0.95,15)
clear()
reset()
spiral(200,95,0.93,10)
