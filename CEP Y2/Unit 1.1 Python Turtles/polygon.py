from turtle import *


def polygon(numSides, sideLength):
    '''
        Draws a polygon with the specified number 
        of sides, each with the specified length.'''
    # solution
    angle = 360.0/numSides   #angle to turn at each side
    for i in range(numSides):
        fd(sideLength)
        lt(angle)

        
if __name__ == "__main__":
    setup(400,400)
    for sides in range(3,10):
        clear()
        reset() 
        polygon(sides,100)
    exitonclick()
