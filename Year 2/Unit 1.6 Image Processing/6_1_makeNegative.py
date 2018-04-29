from cImage import *

def negativePixel(oldPixel):
    newred = 255 - oldPixel.getRed()
    newgreen = 255 - oldPixel.getGreen()
    newblue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel


def makeNegative(imageFile):
    oldimage = FileImage(imageFile)
    myimagewindow = ImageWin("Image Processing",oldimage.getWidth()*2,oldimage.getHeight())   
    
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = EmptyImage(width,height)       

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)    
            newPixel = negativePixel(originalPixel)
            newim.setPixel(col,row,newPixel)     

    newim.setPosition(width+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()

makeNegative("yeah.gif")
