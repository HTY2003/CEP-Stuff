# PS1 Turtle Graphics
# Name: Heng Teng Yi
# Class: 2J

from turtle import *

# Tests are at the bottom in the run function.

# Provided helper function
# You can, but don't need to, change anything in this function
def intializeTurtle():
    ''' Initialize turtle on canvas before drawing '''

    setup(800,600) # Create a turtle window
    reset() # Show turtle window and turtle
    pencolor('black') # You can change the pencolor, if you so choose

    # Set the speed; 0=No animation, 1=slowest, 6=normal, 10=fast, etc.
    speed(100) # can change this to vary the speed of your turtle

    # Turtle, by default, starts roughly in center of canvas
    pu()

    # Put turtle in bottom left cornerish to better fit the pattern
    setx(-200)
    sety(-200)
    pd()

    # Magical statements to make turtle window come to top of screen.
    getscreen()._root.attributes('-topmost', True)
    getscreen()._root.attributes('-topmost', False)


# ------------------------------------
# Task 1
# ------------------------------------
def square(length):
    # Copy and paste the version of square you want to use
    for i in range(4):
        fd(length)
        lt(90)

    #pass   

# ------------------------------------
# Task 2
# ------------------------------------
def row(number, size):
    if number>=1:
        square(size)
        fd(size)
        number=number-1
        row(number, size)
    home()
    position()
    (-200,-200)
    

row(6,60)

''' Recursively draw a row of squares (like asteriskLine), maintains a position invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 3
# ------------------------------------
def spacedRow(number, size):
    for i in range(number):
        square(size)
        fd(size)
        pu()
        fd(10)
        pd()

''' Recursively draw a row of squares with a constant space in between squares
    and maintians a posiion invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 4
# ------------------------------------
def decreasingRow(number, size):
    for i in range(number):
        square(size)
        fd(size)
        size = size/2
    
''' Recursively draw a row of squares that get progressively smaller by 1/2 each time
    and maintains a position invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 5
# ------------------------------------
def nestedSquares(number, size):
        for i in range(number):
           square(size)
           size = size/2

''' Recursively draw nested squares that get progressively smaller by 1/2 each time
    anchored in the lower left corner '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 6
# ------------------------------------
def diagonal(number, size):
    for i in range(number):
           square(size)
           fd(size)
           lt(90)
           fd(size)
           rt(90)
           size = size/2

''' Recursively draw a row of squares that get progressively smaller by 1/2 each time
    where each successive square is anchored on the upper right corner of the previous square.
    Maintains a position invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 7
# ------------------------------------
def superDiagonal(number, size):
    ''' Recursively draw a row of squares that get progressively smaller by 1/2 each time
    where each successive square is anchored on the upper right corner of the previous square
    and the upper left corner of the previous square '''
    # Fill in your solution and comment out pass by adding a # in front
    pass


def run():
    intializeTurtle()

    # tests
    """square(100)
    row(5, 100)
    spacedRow(5, 100)
    decreasingRow(5, 100)
    nestedSquares(5, 100)
    diagonal(5, 100)
    superDiagonal(5, 100)"""

    done() # Done makes it so we don't have to restart the kernel

# Invoke run() to run your turtle program
run()



# ------------------------------------
# Task 8
# ------------------------------------
def myGreetingCard():
    ''' Write your codes for drawing the greeting card here. You are allowed to
    include other functions that you choose to implement to make this main code
    readable. '''
    pass


myGreetingCard()
