from polygon import *

def polyFlow(numPetals, petalSides, petalLen):
    '''Draws "flowers" with numPetals arranged around
    a center point. Each petal is a polygon with
    petalSides sides of length petalLen.'''
    # solution
    angle = 360.0/numPetals   #angle to turn after each petal
    for i in range(numPetals):
        polygon(petalSides, petalLen)
        lt(angle)


        
if __name__ == "__main__":
    setup(1.0,1.0)
    clear()
    reset() 
    polyFlow(7,4,80)
    clear()
    reset() 
    polyFlow(10,5,75)
    clear()
    reset() 
    polyFlow(11,6,60)
    exitonclick()
