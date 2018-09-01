from cImage import *

def double(oldimage):
    oldw = oldimage.getWidth()    
    oldh = oldimage.getHeight()

    newim = EmptyImage(oldw*2,oldh*2)   

    for row in range(oldh):
        for col in range(oldw):
            oldpixel = oldimage.getPixel(col,row)
            
            newim.setPixel(2*col,2*row,oldpixel)   
            newim.setPixel(2*col+1,2*row,oldpixel)
            newim.setPixel(2*col,2*row+1,oldpixel)
            newim.setPixel(2*col+1,2*row+1,oldpixel)  

    return newim

def makeDouble(imageFile):
    oldimage = FileImage(imageFile)
    myimagewindow = ImageWin("Double Image",
                             oldimage.getWidth()*3,
                             oldimage.getHeight()*2)   
    
    oldimage.draw(myimagewindow)

    newim = double(oldimage)     

    newim.setPosition(oldimage.getWidth()+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()

makeDouble("barbie.gif")
