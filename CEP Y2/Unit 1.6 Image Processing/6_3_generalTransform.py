from cImage import *
def negativePixel(oldPixel):
    newred = 255 - oldPixel.getRed()
    newgreen = 255 - oldPixel.getGreen()
    newblue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel


def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + \
                   oldpixel.getBlue()
    aveRGB = intensitySum // 3

    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel

def sepiaPixel(oldpixel):
    R=oldpixel.getRed()
    B=oldpixel.getBlue()
    G=oldpixel.getGreen()
    newR = (R*0.393 + G*0.769 + B*0.189)
    newG= (R*0.349 + G*0.686 + B*0.168)
    newB = (R*0.272 + G*0.534 + B*0.131)
    for i in range(0,256,-1):
        if newR < i:
            newR=i
        if newG < i:
            newG=i
        if newB < i:
            newB=i
    newPixel = Pixel(newR,newG,newB)
    return newPixel


def pixelMapper(oldimage,rgbFunction):
    width = oldimage.getWidth()          
    height = oldimage.getHeight()
    newim = EmptyImage(oldimage.getWidth(),oldimage.getHeight())     

    for row in range( oldimage.getHeight()):
        for col in range(oldimage.getWidth()):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = rgbFunction(originalPixel)          
            newim.setPixel(col,row,newPixel)
            
    return newim


def generalTransform(imageFile,mapper):
    oldimage = FileImage(imageFile)
    myimagewindow = ImageWin("Image Processing",oldimage.getWidth()*2,oldimage.getHeight())
    oldimage.draw(myimagewindow)
    
    newimage = pixelMapper(oldimage,mapper)       
    newimage.setPosition(oldimage.getWidth()+1,0)
    newimage.draw(myimagewindow)
    myimagewindow.exitOnClick()
generalTransform("apple.gif",sepiaPixel)
