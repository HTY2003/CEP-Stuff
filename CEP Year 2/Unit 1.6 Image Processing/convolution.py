import math
from cImage import *
filterWidth = 3
filterHeight = 3

#This filter does nothing more than returning the original image
#since only the center value is 1 so every pixel is multiplied with 1.
identityMask = [[-1,0,0],\
                [0,1,0],\
                [0,0,0]]

#Blurring is done for example by taking the average of
#the current pixel and its 4 neighbors. Take the sum of
#the current pixel and its 4 neighbors, and divide it through 5,
#or thus fill in 5 times the value 0.2 in the filter
blurMask3x3 = [ [0.0,0.2,0.0],\
                [0.2,0.2,0.2],\
                [0.0,0.2,0.0]]


#With a bigger filter you can blur it a bit more 
#(don't forget to change the filterWidth and filterHeight values):
blurryMask5x5 =[[-1,-1,-1,-1,-1],\
                [-1,2,2,2,-1],\
                [-1,2,6,2,-1],\
                [-1,2,2,2,-1],\
                [-1,-1,-1,-1,-1] ]

'''
#Motion blur is achieved by blurring in only 1 direction.
#Here's a 9x9 motion blur filter
'''
motionBlur9x9 = [ [1,0,0,0,0,0,0,0,0],\
                  [0,1,0,0,0,0,0,0,0],\
                  [0,0,1,0,0,0,0,0,0],\
                  [0,0,0,1,0,0,0,0,0],\
                  [0,0,0,0,1,0,0,0,0],\
                  [0,0,0,0,0,1,0,0,0],\
                  [0,0,0,0,0,0,1,0,0],\
                  [0,0,0,0,0,0,0,1,0],\
                  [0,0,0,0,0,0,0,0,1]]
ContrastBlur = [ [1,1,0,0,0,0,0,-1,-1],\
                  [1,1,0,0,0,0,0,-1,-1],\
                  [1,1,0,0,0,0,0,-1,-1],\
                  [1,1,0,0,-1,0,0,-1,-1],\
                  [1,1,0,-1,8,-1,0,-1,-1],\
                  [1,1,0,0,-1,0,0,-1,-1],\
                  [1,1,0,0,0,0,0,-1,-1],\
                  [1,1,0,0,0,0,0,-1,-1],\
                  [1,1,0,0,0,0,0,-1,-1]]
CalligraphyBlur = [ [1,1,1,1,1,1,1,1,1],\
                  [1,1,1,1,1,1,1,1,1],\
                  [0,0,0,0,0,0,0,0,0],\
                  [0,0,0,0,-0.25,0,0,0,0],\
                  [0,0,0,-0.25,6,-0.25,0,0,0],\
                  [0,0,0,0,-0.25,0,0,0,0],\
                  [0,0,0,0,0,0,0,0,0],\
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],\
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
#The reason why this filter can find horizontal edges, is that the
#convolution operation with this filter can be seen as a sort of discrete
#version of the derivative: you take the current pixel and subtract the value
#of the previous one from it, so you get a value that represents the difference
#between those two or the slope of the function.
xMask = [ [-1, 0, 1],\
          [-1, 0, 1],\
          [-1, 0, 1]]

#Here's a filter that'll find vertical edges instead,
#and uses both pixel values below and above the current pixel
yMask = [ [0,-1, 0],\
          [0, 0, 0],\
          [0, 1, 0]]


'''
To sharpen the image is very similar to finding edges, add the original image, and the image
after the edge detection to each other, and the result will be a new image where the edges
are enhanced, making it look sharper. Adding those two images is done by taking the edge
detection filter from the previous example, and incrementing the center value of it with 1.
Now the sum of the filter elements is 1 and the result will be an image with the same brightness
as the original, but sharper.
'''
sharpenMask = [ [-1,-1,-1],\
                [-1, 9,-1],\
                [-1,-1,-1]]

sharpenMask2 = [[ 0,-1, 0],\
                [-1, 5,-1],\
                [ 0,-1, 0]]

sharpenMask3 = [[    0,-0.25,    0],\
                [-0.25,    2,-0.25],\
                [    0,-0.25,    0]]


'''
Apart from using a filter matrix, it also has a multiplier factor and a bias. After applying the filter,
the factor will be multiplied with the result, and the bias added to it. So if you have a filter with an
element 0.25 in it, but the factor is set to 2, all elements of the filter are in theory multiplied by two
so that element 0.25 is actually 0.5. The bias can be used if you want to make the resulting image brighter.
'''

factor = 1.0 
bias = 0.0

def convolve(anImage,pixelRow,pixelCol,kernel):
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1
    
    rsum = 0
    gsum = 0
    bsum = 0
    
    for row in range(kernelRowBase,kernelRowBase+filterWidth):
        for col in range(kernelColumnBase,kernelColumnBase+filterHeight):
            kColIndex = col-kernelColumnBase
            kRowIndex = row-kernelRowBase
            
            apixel = anImage.getPixel(col,row)
            rintensity = apixel.getRed()
            gintensity = apixel.getGreen()
            bintensity = apixel.getBlue()
            
            rsum = rsum + rintensity * kernel[kRowIndex][kColIndex]
            gsum = gsum + gintensity * kernel[kRowIndex][kColIndex]
            bsum = bsum + bintensity * kernel[kRowIndex][kColIndex]

    red = min(max(int((factor * rsum) + bias), 0), 255)
    green = min(max(int((factor * gsum) + bias), 0), 255)
    blue = min(max(int((factor * bsum) + bias), 0), 255)
    return red, green, blue

def applyFilter(theImage, ifilter):
    newim = EmptyImage(theImage.getWidth(), theImage.getHeight())
    ignore = filterWidth - 2
    for row in range(1,theImage.getHeight()-ignore):    
        for col in range(1,theImage.getWidth()-ignore):
            red,green,blue = convolve(theImage, row, col, ifilter)
            newim.setPixel(col,row,Pixel(red,green,blue))
    return newim
                           



###Identity Filter
##image = FileImage("RIShield.gif")
##myimagewindow = ImageWin("Identity Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, identityMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
##
###Blur3x3 Filter
##image = FileImage("RIShield.gif")
##myimagewindow = ImageWin("Blur3x3 Filter", image.getWidth(), image.getHeight())
####filterWidth = 5
####filterHeight = 5
####factor = 1.0 / 13.0
####bias = 0.0
##newimage = applyFilter(image, blurMask3x3)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
##
#Blur5x5 Filter
##image = FileImage("RIShield.gif")
##myimagewindow = ImageWin("Blur5x5 Filter", image.getWidth(), image.getHeight())
##filterWidth = 5
##filterHeight = 5
###factor = 1.0 / 13.0
##bias = 0.0
##newimage = applyFilter(image, blurMask5x5)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
##


##image = FileImage("RIShield.gif")
##myimagewindow = ImageWin("Identity Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, identityMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
##
###Blur5x5 Filter
##image = FileImage("RIShield.gif")
##myimagewindow = ImageWin("Blur5x5 Filter", image.getWidth(), image.getHeight())
##filterWidth = 5
##filterHeight = 5
##factor = 1.0 / 13.0
##bias = 0.0
##newimage = applyFilter(image, blurMask5x5)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
motionBlurry9x9 = [[1,0,0,0,-1,0,0,0,1],\
                  [0,1,0,0,-1,0,0,1,0],\
                  [0,0,1,0,-1,0,1,0,0],\
                  [0,0,0,1,-1,1,0,0,0],\
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],\
                  [0,1,0,1,-1,1,0,0,0],\
                  [0,0,1,0,-1,0,1,0,0],\
                  [0,1,0,0,-1,0,0,1,0],\
                  [1,0,0,0,-1,0,0,0,1]]
##MotionBlur9x9 Filter
image = FileImage("apple.gif")
myimagewindow = ImageWin("motionBlur9x9", image.getWidth(), image.getHeight())
filterWidth = 9
filterHeight = 9
factor = 1.0 / 9.0
bias = 4.0
newimage = applyFilter(image, ContrastBlur)
newimage.draw(myimagewindow)
newimage.save("alienapple.gif")

##image = FileImage("bigapple.gif")
##myimagewindow = ImageWin("Identity Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, identityMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()

##image = FileImage("apple.gif")
##myimagewindow = ImageWin("xMask Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, xMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()

##image = FileImage("bigapple.gif")
##myimagewindow = ImageWin("yMask Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, yMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
##
##image = FileImage("bigapple.gif")
##myimagewindow = ImageWin("xyMask Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, xMask)
##newimage = applyFilter(newimage, yMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()


##image = FileImage("cuteanimal.gif")
##myimagewindow = ImageWin("Identity Filter", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, identityMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
##
##image = FileImage("cuteanimal.gif")
##myimagewindow = ImageWin("Sharpen Filter 1", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, sharpenMask)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()

##image = FileImage("cuteanimal.gif")
##myimagewindow = ImageWin("Sharpen Filter 3", image.getWidth(), image.getHeight())
##newimage = applyFilter(image, sharpenMask3)
##newimage.draw(myimagewindow)
##myimagewindow.exitOnClick()
