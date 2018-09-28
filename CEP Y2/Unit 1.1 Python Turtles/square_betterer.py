from turtle import *
def square(size):
    '''
    draw a square using
    square function that
    accepts a size parameter
    with loop
    '''
    for i in range(4):
        fd(size)
        rt(90)
    


setup(1.0,1.0)
square(50)
square(100)
square(150)
exitonclick()


