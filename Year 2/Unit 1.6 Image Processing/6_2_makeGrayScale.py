from cImage import *

def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + \
                   oldpixel.getBlue()
    aveRGB = intensitySum // 3

    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel

def makeGrayScale(imageFile):
    oldimage = FileImage(imageFile)            
    myimagewindow = ImageWin("Image Processing",oldimage.getWidth()*2,oldimage.getHeight())
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = grayPixel(originalPixel)         
            newim.setPixel(col,row,newPixel)
    return newim

    newim.setPosition(width+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()
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
    return newim
makeNegative(makeGrayScale(makeNegative("cuteanimal.gif")))
