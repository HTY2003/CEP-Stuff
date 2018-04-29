import pygame
import time
import random
from cImage import *

from PIL import ImageColor as IC

pygame.init()

image = FileImage("Button.png")

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Randumbo')

clock = pygame.time.Clock()
car = pygame.image.load("Button.png")

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])
                                        
def text_objects(text, font):
    textSurface = font.render(text, True, (0,)*3)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def distance(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Distance: "+str(count), True, IC.getrgb("black"))
    screen.blit(text,(0,0))
    
def unpause():
    global pause
    pause = False
    
def paused():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((width/2),(height/2))
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit()
        screen.fill(IC.getrgb("white"))
        screen.blit(TextSurf, TextRect)
        button("Continue",150,450,100,50,IC.getrgb("lime"),IC.getrgb("green"), unpause)
        button("Quit",550,450,100,50,IC.getrgb("red"),IC.getrgb("maroon"),quitgame)

        pygame.display.update()
        clock.tick(15)

def crash():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((width/2),(height/2))
    
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                quitgame()
                
        screen.fill(IC.getrgb("white"))
        screen.blit(TextSurf, TextRect)

        button("Play Again",150,450,100,50,IC.getrgb("lime"),IC.getrgb("green"),game_loop)
        button("Quit",550,450,100,50,IC.getrgb("red"),IC.getrgb("maroon"),quitgame)

        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    global pause
    done = False
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0
    y_change = 0
    dist = 0
    car_speed = 0
    pause = True
    car_width = image.getWidth()
    car_height = image.getHeight()

    thing_startx = random.randrange(0, width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quitgame()
                    print(event)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        elif event.key == pygame.K_RIGHT:
                            x_change = 5
                        elif event.key == pygame.K_p:
                            paused()
                    '''if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            y_change = -5
                        elif event.key == pygame.K_DOWN:
                            y_change = 5'''
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            if x_change == -5:
                                x_change = 0
                        elif event.key == pygame.K_RIGHT:
                            if x_change == 5:
                                x_change = 0
                        
                    '''if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            if y_change == -5:
                                y_change = 0
                        elif event.key == pygame.K_DOWN:
                            if y_change == 5:
                                y_change = 0'''
            x += x_change
            #y += y_change
            screen.fill((255,)*3)
            
            things(thing_startx, thing_starty, thing_width, thing_height, IC.getrgb("black"))
            thing_starty += thing_speed
            dist += 1
            score = int(dist/10) * 2
            distance(score)
            
            things(x-3, y-3, car_width + 6, car_height + 6 , IC.getrgb("black"))
            things(x-1, y-1, car_width + 2, car_height + 2, IC.getrgb("white"))
            screen.blit(car, (x,y))
            
            if x > width - car_width or x < 0:
                crash()

            if thing_starty > height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0,width)

            if y < thing_starty + thing_height:
                if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                    crash()
                
            pygame.display.update()
            clock.tick(60)

def button(msg,x,y,w,h,ac,ic,action=None):
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    print(mouse)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        
        screen.blit(textSurf, textRect)

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    
def game_start():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                quitgame()
                
        screen.fill(IC.getrgb('white'))
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Hi", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)

        button("start",150,450,100,50,IC.getrgb("lime"),IC.getrgb("green"), game_loop)
        
        button("exit",550,450,100,50,IC.getrgb("maroon"),IC.getrgb("red"), quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def quitgame():
    pygame.quit()
    quit()
    
game_start()

