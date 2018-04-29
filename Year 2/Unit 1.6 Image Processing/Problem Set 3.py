from cImage import *
def smileyFace():
    smileywin=ImageWin("Smiley",385,330)#window set up
    smiley=EmptyImage(385,330)          #image set up
    black=Pixel(0,0,0)
    white=Pixel(255,255,255)
    for col in range(385):
        for row in range(330):
            smiley.setPixel(col,row,white)#sets background to white
    def drawrect(length,width,strow,stcol):
       for l in range(0,length):
           for w in range(0,width):
               smiley.setPixel(stcol+w,strow+l,black)
    def makesmiley():
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
    makesmiley()                        #creates image
    smiley.draw(smileywin)              #drawing out image on window
    smiley.save("smiley.gif")           #saves image
def rotateImage90CW(filename):
    image=FileImage(filename)
    w=image.getWidth()
    h=image.getHeight()
    newimage=EmptyImage(h,w)
    newimagewin=ImageWin("Rotate",h,w)
    for row in range(h):
        for col in range(w):
            p=image.getPixel(col,row)
            newimage.setPixel(h-row,col,p)
    newimage.save("Rotated " + filename)
    newimage.draw(newimagewin)
def incExposure(filename,factor):
    def incExPixel(oldPixel):         #process for increasing exposure of a pixel
        red = oldPixel.getRed()*factor
        green = oldPixel.getGreen()*factor
        blue = oldPixel.getBlue()*factor
        newred=min(int(red),255)
        newblue=min(int(blue),255)
        newgreen=min(int(green),255)
        newPixel = Pixel(newred,newgreen,newblue)
        return newPixel
    def changeImage(imageFile):        #a bit "copied" from the makeNegative and makeGrayScale function notes
        oldimage = FileImage(imageFile)
        width = oldimage.getWidth()
        height = oldimage.getHeight()
        myimagewindow = ImageWin("Exposure Increase",width,height)   
        newim = EmptyImage(width,height)       
        for row in range(height):
            for col in range(width):
                originalPixel = oldimage.getPixel(col,row)    
                newPixel = incExPixel(originalPixel)
                newim.setPixel(col,row,newPixel)     
        newim.draw(myimagewindow)
        newim.save("IncEx "+filename)
    changeImage(filename)
def decExposure(filename,factor):
    def decExPixel(oldPixel):             #process for decreasing exposure of a pixel
        red = oldPixel.getRed()/factor
        green = oldPixel.getGreen()/factor
        blue = oldPixel.getBlue()/factor
        newred=int(red)
        newblue=int(blue)
        newgreen=int(green)
        newPixel = Pixel(newred,newgreen,newblue)
        return newPixel
    def changeImage(imageFile):            #this function is pretty much the same in both RGBFunctions
        oldimage = FileImage(imageFile)     #except for the increase or decrease Pixel Ex. functions
        width = oldimage.getWidth()
        height = oldimage.getHeight()
        myimagewindow = ImageWin("Exposure Decrease",width,height)   
        newim = EmptyImage(width,height)       
        for row in range(height):
            for col in range(width):
                originalPixel = oldimage.getPixel(col,row)    
                newPixel = decExPixel(originalPixel)
                newim.setPixel(col,row,newPixel)     
        newim.draw(myimagewindow)
        newim.save("DecEx "+filename)
    changeImage(filename)
def whiteScreen(bodyfile,backgroundfile):      #challenge 1
    bodyimage=FileImage(bodyfile)
    backgroundimage=FileImage(backgroundfile)
    width=bodyimage.getWidth()   #the result photo will be the size of the body photo with the blank screen
    height=bodyimage.getHeight()
    bgwidth=backgroundimage.getWidth()
    bgheight=backgroundimage.getHeight()
    widthdiff=(bgwidth-width)//2
    heightdiff=bgheight-height
    combimage=EmptyImage(width,height)
    imageWin=ImageWin("White Screen", width, height)
    for col in range(width):
        for row in range(height):
            pixel=bodyimage.getPixel(col,row)
            if pixel.getRed()< 255:                                                    #R G and B values all have to fit the chromakey, in this case (255,255,255)
                if pixel.getGreen() < 255:
                    if pixel.getBlue() < 255:
                        combimage.setPixel(col,row,pixel)
                    else:
                        bgpixel=backgroundimage.getPixel(widthdiff+col,heightdiff+row) #such that the background image will be more centred 
                        combimage.setPixel(col,row,bgpixel)                            #and you can see the bottom of the picture
                else:
                    bgpixel=backgroundimage.getPixel(widthdiff+col,heightdiff+row)     #a limitation is that the background image has to be equal to or larger than the body image
                    combimage.setPixel(col,row,bgpixel)                                #in terms of size
            else:
                bgpixel=backgroundimage.getPixel(widthdiff+col,heightdiff+row)         #another problem is that the crappy gif quality causes reflections to be white too so they could turn out as part of the background
                combimage.setPixel(col,row,bgpixel)
    combimage.draw(imageWin)
    combimage.save("whiteScreen " + bodyfile)
def superImpose(bodyfile,blankfile,backgroundfile): #challenge 2 but it's very similar to the first
    bodyimage=FileImage(bodyfile)
    blankimage=FileImage(blankfile)
    backgroundimage=FileImage(backgroundfile)
    width=bodyimage.getWidth()
    height=bodyimage.getHeight()
    bgwidth=backgroundimage.getWidth()
    bgheight=backgroundimage.getHeight()
    widthdiff=(bgwidth-width)//2
    heightdiff=bgheight-height
    siimage=EmptyImage(width,height)
    completeimage=EmptyImage(width,height)
    imageWin=ImageWin("Superimpose", width, height)
    for col in range(width):
        for row in range(height):
            pixel=bodyimage.getPixel(col,row)
            blankpixel=blankimage.getPixel(col,row)
            bgpixel=backgroundimage.getPixel(widthdiff+col,heightdiff+row)
            if pixel.getRed()!= blankpixel.getRed():
                if pixel.getGreen() != blankpixel.getGreen():
                    if pixel.getBlue() != blankpixel.getBlue():
                       siimage.setPixel(col,row,pixel)
                    else:
                       siimage.setPixel(col,row,bgpixel)
                else:
                    siimage.setPixel(col,row,bgpixel)
            else:
                siimage.setPixel(col,row,bgpixel)
    siimage.draw(imageWin)
    siimage.save("Imposed "+ bodyfile)
def redEyecorrect(filename,noofredeyes):
    es=5                          #short for eye size. can be adjusted according to how big the eye is
    originalimage=FileImage(filename)
    width=originalimage.getWidth()
    height=originalimage.getHeight()
    newfilename="Corrected "+filename
    myWin=ImageWin(newfilename,width,height)
    def redEye():
        originalimage.draw(myWin)
        mouse=myWin.getMouse()
        for row in range(height):
            for col in range(width):
                if mouse[0] == col:
                    if mouse[1] == row:
                        for c in range(-es,es+1,1):
                            for r in range(-es,es+1,1):                 #such that only one click is needed
                                pixel=originalimage.getPixel(col+c,row+r)#draws a square aroung the eye
                                green=pixel.getGreen()
                                blue=pixel.getBlue()
                                red=pixel.getRed()
                                newred=(green+blue)//2
                                if red > newred:
                                    originalimage.setPixel(col+c,row+r,Pixel(newred,green,blue))
    for eye in range(1,noofredeyes+1):
        redEye()
    originalimage.save(newfilename)
def imageCut(filename):
    originalimage=FileImage(filename)
    width=originalimage.getWidth()
    height=originalimage.getHeight()
    newfilename="Cut?"+filename
    myWin=ImageWin(newfilename,width,height)
    originalimage.draw(myWin)
    point1=myWin.getMouse()                 #the two points are the top left and bottom right of the picture
    point2=myWin.getMouse()
    x1=point1[0]
    y1=point1[1]
    x2=point2[0]
    y2=point2[1]
    cutwidth=x2-x1+1
    cutheight=y2-y1+1
    newWin=ImageWin("Cut "+filename,cutwidth,cutheight)
    newimage=EmptyImage(cutwidth,cutheight)
    for col in range(x1,x2+1):
        for row in range(y1,y2+1):
            pixel=originalimage.getPixel(col,row)
            newimage.setPixel(col-x1,row-y1,pixel)
    newimage.draw(newWin)
    newimage.save("Cut "+filename)

smileyFace()
incExposure("baby.gif",3)
decExposure("Crying.gif",2.3)
rotateImage90CW("cuteanimal.gif")
whiteScreen("thumbs.gif","WeddingPhoto.gif")
superImpose("thumbs.gif","blank.gif","WeddingPhoto.gif")
redEyecorrect("red-eye.gif",4)
imageCut("Corrected red-eye.gif")

