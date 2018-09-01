# PS1 Turtle Graphics
# Name: Heng Teng Yi
# Class: 2J

from turtle import *

# Tests are at the bottom in the run function.

# Provided helper function
# You can, but don't need to, change anything in this function
def initializeTurtle():
    ''' Initialize turtle on canvas before drawing '''

    setup(800,600) # Create a turtle window
    reset() # Show turtle window and turtle
    pencolor('black') # You can change the pencolor, if you so choose

    # Set the speed; 0=No animation, 1=slowest, 6=normal, 10=fast, etc.
    speed(0) # can change this to vary the speed of your turtle

    # Turtle, by default, starts roughly in center of canvas
    pu()

    # Put turtle in bottom left cornerish to better fit the pattern
    setx(-200)
    sety(-200)
    pd()

    # Magical statements to make turtle window come to top of screen.
    getscreen()._root.attributes('-topmost', True)
    getscreen()._root.attributes('-topmost', False)

initializeTurtle()


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
    pd()
    if number > 0:
       square(size)
       fd(size)
       row(number-1,size)
       pu()
       bk(size)
       rt(90)
       bk(size)
       rt(90)
       bk(size)
       rt(90)
       bk(size)
       rt(90)
       bk(size)
    pd()
''' Recursively draw a row of squares (like asteriskLine), maintains a position invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 3
# ------------------------------------
def spacedRow(number, size):
    if number > 1:
        square(size)
        fd(size)
        pu()
        fd(10)
        pd()
        spacedRow(number-1,size)
        pu()
        bk(10)
        bk(size)
        rt(90)
        bk(size)
        rt(90)
        bk(size)
        rt(90)
        bk(size)
        rt(90)
        bk(size)
    pd()
    

''' Recursively draw a row of squares with a constant space in between squares
    and maintians a posiion invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 4
# ------------------------------------
def decreasingRow(number, size):
    pd()
    if number >= 1:
        square(size)
        fd(size)
        size = size/2
        number=number-1
        decreasingRow(number,size)
        pu()
        bk(size*2)
        rt(90)
        bk(size*2)
        rt(90)
        bk(size*2)
        rt(90)
        bk(size*2)
        rt(90)
        bk(size*2)
    pd()
''' Recursively draw a row of squares that get progressively smaller by 1/2 each time
    and maintains a position invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 5
# ------------------------------------
def nestedSquares(number, size):
    if number > 1:
        square(size)
        size = size/2
        number=number-1
        nestedSquares(number,size)
''' Recursively draw nested squares that get progressively smaller by 1/2 each time
    anchored in the lower left corner '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 6
# ------------------------------------
def diagonal(number, size):
    if number >= 1:
           square(size)
           fd(size)
           lt(90)
           fd(size)
           rt(90)
           size = size/2
           number=number-1
           diagonal(number,size)
           lt(90)
           bk(size*2)
           rt(90)
           pu()
           bk(size*2)
           rt(90)
           bk(size*2)
           rt(90)
           bk(size*2)
           rt(90)
           bk(size*2)
           rt(90)
           bk(size*2)

''' Recursively draw a row of squares that get progressively smaller by 1/2 each time
    where each successive square is anchored on the upper right corner of the previous square.
    Maintains a position invariant '''
    # Fill in your solution and comment out pass by adding a # in front
#pass


# ------------------------------------
# Task 7
# ------------------------------------
def superDiagonal(number, size):
    pu()
    home()
    pd()
    def blSquare(size):
        for i in range(4):
           rt(90)
           fd(size)
    def spread(number,size):
        if number > 2:
           blSquare(size)
           square(size/2)
           fd(size/2)
           lt(90)
           fd(size/2)
           rt(90)
           square(size/4)
           rt(90)
           fd(size/2)
           rt(90)
           fd(size/2)
           rt(180)
           blSquare(size/4)
           rt(90)
           fd(size)
           rt(90)
           fd(size)
           rt(180)
           number=number-1
           size=size/2
           spread(number,size)
        elif number > 1:
           blSquare(size)
           square(size/2)
           rt(90)
           fd(size)
           rt(90)
           fd(size)
           rt(180)
           spread(number-1,size/2)
        elif number > 0:
           blSquare(size)
           rt(90)
           fd(size)
           rt(90)
           fd(size)
           rt(180)
           spread(number-1,size)
    spread(number,size)
    pu()
    home()
    pd()
    rt(90)
    fd(size)
    rt(90)
    fd(size)
    spread(number,size)
    pu()
    home()
    pd()
  #pass
           
        
           

''' Recursively draw a row of squares that get progressively smaller by 1/2 each time
    where each successive square is anchored on the upper right corner of the previous square
    and the upper left corner of the previous square '''
    # Fill in your solution and comment out pass by adding a # in front
    #pass


def run():
    # tests
    square(100)
    clear()
    row(5, 100)
    clear()
    spacedRow(5, 100)
    clear()
    decreasingRow(5, 100)
    clear()
    nestedSquares(5, 100)
    clear()
    diagonal(5, 100)
    clear()
    superDiagonal(5, 100)
    clear()

    #done() # Done makes it so we don't have to restart the kernel
# Invoke run() to run your turtle program
run()

# ------------------------------------
# Task 8
# ------------------------------------
def myGreetingCard():
    initializeTurtle()
    pd()
    pencolor("red")
    fillcolor("red")
    begin_fill()
    fd(300)
    lt(90)
    fd(500)
    lt(90)
    fd(300)
    lt(90)
    fd(500)
    end_fill() #red packet shape and colour
    pu()
    pensize(10)
    pencolor("DarkRed")
    lt(180)#田
    fd(300)
    rt(90)
    fd(50)
    pd()
    row(2,60)
    rt(90)
    fd(60)
    lt(90)
    row(2,60)
    rt(90)
    pu() #口
    fd(30)
    lt(90)
    fd(20)
    pd()
    fd(75)
    rt(90)
    fd(50)
    rt(90)
    fd(75)
    rt(90)
    fd(50)
    rt(180) 
    pu()  #一
    fd(70)
    pd()
    lt(90)
    fd(75) 
    pu() #the rest
    fd(90)
    rt(90)
    fd(10)
    lt(90)
    pd()
    lt(135)
    fd(30)
    rt(135)
    pu()
    fd(40)
    lt(90)
    fd(20)
    lt(90)
    pd()
    fd(75)
    rt(135)
    fd(135)
    lt(180)
    fd(80) 
    rt(135)
    fd(145)
    rt(180)
    fd(145)
    rt(135)
    fd(50) 
    rt(135)
    pu()
    pencolor("gold3")#drawing of red diamond/square
    pensize(5)
    setx(-200)
    sety(-200)
    pd()
    pu()
    lt(90)
    fd(350)
    rt(40)
    pd()
    fd(195)
    rt(50)
    pu()
    fd(50)
    pd()
    rt(50)
    fd(195)
    rt(40)
    pu()
    fd(200)
    rt(40)
    pd()
    fd(195)
    rt(50)
    pu()
    fd(50)
    pd()
    rt(50)
    fd(195)
    rt(40)
    pu()
    shape("turtle")  #turtle decorations
    fillcolor("gold3")
    pencolor("gold3")
    fd(250)
    rt(40)
    fd(75)
    stamp()
    fd(75)
    rt(50)
    fd(100)
    rt(50)
    fd(75)
    stamp()
    fd(75)
    rt(40)
    fd(300)
    rt(40)
    fd(75)
    stamp()
    fd(75)
    rt(50)
    fd(100)
    rt(50)
    fd(75)
    stamp()
    fd(75)
    rt(40)
    rt(90)
    shape("arrow")
    setx(-200)
    sety(-200)
    begin_fill()
    rt(90)
    fd(100)
    lt(90)
    fd(300)
    lt(90)
    fd(100)
    lt(90)
    fd(300)
    end_fill()
    rt(180)
    fd(10)
    rt(90)
    fd(10)
    pencolor("red")
    pensize(3)
    pd()
    fd(80)
    lt(180)
    fd(40)
    rt(90)
    fd(40)
    lt(90)
    fd(40)
    lt(180)
    fd(80)
    pu()
    lt(90)
    fd(5)
    lt(90)
    pd()
    fd(80)
    rt(90)
    fd(40)
    rt(90)
    fd(40)
    rt(90)
    fd(40)
    lt(180)
    fd(40)
    rt(90)
    fd(40)
    pu()
    lt(90)
    fd(5)
    lt(90)
    pd()
    fd(80)
    rt(90)
    fd(40)
    rt(90)
    fd(40)
    rt(90)
    fd(40)
    lt(180)
    fd(40)
    pu()
    rt(90)
    fd(40)
    lt(90)
    fd(5)
    lt(90)
    pd()
    fd(80)
    rt(90)
    fd(40)
    rt(90)
    fd(40)
    rt(90)
    fd(40)
    lt(180)
    fd(40)
    pu()
    rt(90)
    fd(40)
    lt(90)
    fd(20)
    lt(90)
    pd()
    fd(40)
    lt(90)
    fd(20)
    rt(90)
    fd(40)
    lt(180)
    fd(40)
    lt(90)
    fd(40)
    lt(90)
    fd(40)
    lt(180)
    pu()
    fd(80)
    lt(90)
    fd(5)
    lt(90)
    pencolor("yellow")
    fd(80)
    rt(90)
    pd()
    fd(40)
    lt(180)
    fd(40)
    lt(90)
    fd(25)
    lt(90)
    fd(40)
    pencolor("pink")
    rt(90)
    pu()
    fd(2)
    pd()
    fd(25)
    rt(120)
    fd(45)
    lt(120)
    fd(25)
    pencolor("blue")
    lt(60)
    fd(25)
    lt(60)
    fd(25)
    lt(180)
    fd(25)
    lt(60)
    fd(12.5)
    pu()
    lt(90)
    fd(35)
    lt(90)
    pd()
    pencolor("black")
    fd(10)
    pu()
    fd(10)
    pd()
    fd(60)
    
    
    

myGreetingCard()

''' Write your codes for drawing the greeting card here. You are allowed to
    include other functions that you choose to implement to make this main code
    readable. '''
#pass

