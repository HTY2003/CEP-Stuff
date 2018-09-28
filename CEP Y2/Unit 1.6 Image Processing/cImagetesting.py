from cImage import *
def smileyFace():
    smileywin=ImageWin("Smiley",385,330)#window set up
    smiley=EmptyImage(385,330)          #image set up
    black=Pixel(0,0,0)
    white=Pixel(255,255,255)
    for col in range(385):
        for row in range(330):
            smiley.setPixel(col,row,white)
    def drawrect(length,width,strow,stcol):
       for l in range(0,length):
           for w in range(0,width):
               smiley.setPixel(stcol+w,strow+l,black)
    def drawingsmiley():
        x=20
        y=35
        def drawsmileybox(strow,stcol):
            drawrect(x,y,strow,stcol)
        for r in range(1,10,8):         #1st and 9th row
            for i in range(4,12):
                drawsmileybox(i*x,r*y)
        for r in range(2,9,6):          #2nd and 8th row
            for i in range(3,13,9):
                drawsmileybox(i*x,r*y)
        for r in range(3,8,4):          #3rd and 7th row
            for i in range(2,14,11):
                drawsmileybox(i*x,r*y)
        for r in range(4,7):            #middle 3 rows
            for i in range(1,15,13):
                drawsmileybox(i*x,r*y)  #face shape is done!
        for r in range(4,7,2):          #eyes
            for i in range(5,7):
                drawsmileybox(i*x,r*y)
        for i in range(3,8,4):          #mouth
            drawsmileybox(9*x,i*y)
        for i in range(4,7):
            drawsmileybox(10*x,i*y)        
    drawingsmiley()
    smiley.draw(smileywin)
smileyFace()

