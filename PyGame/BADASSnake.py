import pygame
import random
import time
from PIL import ImageColor as IC

pygame.init()

width = 900
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snakelist = []
odict = {"left":(20,0),"right":(-20,0),"up":(0,20),"down":(0,-20),"crashed":(0,0)}
oodict = {"left":"right","right":"left","up":"down","down":"up","crashed":"crashed"}

def col(colour):
    return IC.getrgb(colour)

def text_objects(text, font, colour, rotation = None):
    textSurface = font.render(text, True, col(colour))
    if rotation != None:
        textSurface = pygame.transform.rotate(textSurface, rotation)
    return textSurface, textSurface.get_rect()

def message_display(text, font, fontsize, colour, x, rotation = None):
    largeText = pygame.font.SysFont(font,fontsize)
    TextSurf, TextRect = text_objects(text, largeText, colour, rotation)
    TextRect.center = (int((width/2)),int(x))

    screen.blit(TextSurf, TextRect)

def button(msg,shape,x,y,w,h,ac,ic,font,fontsize,action=None):
    smallText = pygame.font.SysFont(font,fontsize)
    textSurf, textRect = text_objects(msg, smallText,ic)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if shape == "Rect":
        if pygame.draw.rect(screen, col(ic), (x,y,w,h)).collidepoint(mouse[0]-1,mouse[1]-1) == True:
            pygame.draw.rect(screen, col(ac),(x,y,w,h))
            if click[0] == 1 and action != None:
                time.sleep(0.1)
                action()
        else:
            pygame.draw.rect(screen, col(ic),(x,y,w,h))
            smallText = pygame.font.SysFont(font,fontsize)
            textSurf, textRect = text_objects(msg, smallText,ac)
            textRect.center = ((x+(w/2)), (y+(h/2)))

    if shape == "Circle":
        if pygame.draw.circle(screen, col(ic), (x,y), w).collidepoint(mouse[0]-1,mouse[1]-1) == True:
            pygame.draw.circle(screen, col(ac),(x,y), w)
            if click[0] == 1 and action != None:
                time.sleep(0.1)
                action()
        else:
            pygame.draw.circle(screen, col(ic),(x,y), w)
            smallText = pygame.font.SysFont(font,fontsize)
            textSurf, textRect = text_objects(msg, smallText,ac)
            textRect.center = ((x+(w/2)), (y+(h/2)))

    screen.blit(textSurf, textRect)

def snake_module(x,y,colour):
    pygame.draw.rect(screen,col(colour),(x,y,20,20))

def snake_food():
    random.seed()
    foodx = random.randrange(10,891,20)
    foody = random.randrange(110,691,20)
    if (foodx,foody) in snakelist:
        snake_food()
    else:
        return (foodx,foody)

def game_startscreen():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        screen.fill(col("white"))

        message_display("SNAKE","ArcadeClassic",150,"black",180)
        button("Play >","Rect",250,300,400,100,"lime","green","FFFForward",45,game_loop)
        button("Instructions","Rect",250,415,400,100,"darkgrey","grey","FFFForward",40,instructions)
        button("Quit  X","Rect",250,530,400,100,"red","maroon","FFFForward",45,game_quit)
        pygame.display.update()
        clock.tick(15)
def instructions():
    instruct = True
    while instruct:
        screen.fill(col("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()

        message_display("Instructions","FFFForward",60,"black",130)
        message_display("1. Use the arrow keys or the","FFFForward",30,"black",220)
        message_display("   WASD keys to move around.","FFFForward",30,"black",260)
        message_display("2. Collect the red food pellets to","FFFForward",30,"black",360)
        message_display("   grow longer and score points.","FFFForward",30,"black",400)
        message_display("3. Don't run into yourself or hit the","FFFForward",30,"black",500)
        message_display("   sides of the screen, or you'll die!","FFFForward",30,"black",540)

        button("< Back","Rect",0,0,250,80,"red","maroon","FFFForward",30,game_startscreen)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    game = True
    foodeaten = True
    startmeal = False
    inverse = False
    crash = False
    paused = False
    foodx = 0
    foody = 0
    x = 440
    y = 280
    snakelist = []
    start_pos = "crashed"
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
            if event.type == pygame.KEYDOWN:
                if paused == False:
                    if event.key == 8:
                        if inverse == False:
                            inverse = True
                        elif inverse == True:
                            inverse = False
                    if len(snakelist) > 1:
                        if event.key == pygame.K_LEFT or event.unicode == "a":
                            if start_pos != "right":
                                start_pos = "left"
                        if event.key == pygame.K_RIGHT or event.unicode == "d":
                            if start_pos != "left":
                                start_pos = "right"
                        if event.key == pygame.K_UP or event.unicode == "w":
                            if start_pos != "down":
                                start_pos = "up"
                        if event.key == pygame.K_DOWN or event.unicode == "s":
                            if start_pos != "up":
                                start_pos = "down"
                    else:
                        if event.key == pygame.K_LEFT or event.unicode == "a":
                            start_pos = "left"
                        if event.key == pygame.K_RIGHT or event.unicode == "d":
                            start_pos = "right"
                        if event.key == pygame.K_UP or event.unicode == "w":
                            start_pos = "up"
                        if event.key == pygame.K_DOWN or event.unicode == "s":
                            start_pos = "down"
                    if event.unicode == "p":
                        paused = True
                else:
                    if event.unicode == "p":
                        paused = False

        if paused == False:
            if inverse == False:
                screen.fill(col("white"))
                pygame.draw.rect(screen, col("grey"),(0,0,900,100))
                message_display("Score:"+ str(len(snakelist)-1),"FFFForward",50,"darkgrey",50)
            else:
                screen.fill(col("black"))
                pygame.draw.rect(screen, col("darkblue"),(0,0,900,100))
                message_display("Score:"+ str(len(snakelist)-1),"FFFForward",50,"blue",50)

            x += odict[oodict[start_pos]][0]
            y += odict[oodict[start_pos]][1]

            if foodeaten == True:
                foodxy = snake_food()
                foodx = foodxy[0]
                foody = foodxy[1]
                foodeaten = False
            if foodx - 10 == x and foody - 10 == y:
                foodeaten = True
                snakelist.insert(-1,(x+(odict[start_pos][0])*1,y+(odict[start_pos][1])*1))
                snakelist.insert(-1,(x+(odict[start_pos][0])*2,y+(odict[start_pos][1])*2))

            snakelist = snakelist[:-1]
            snakelist.insert(0, (x,y))

            if inverse == False:
                pygame.draw.circle(screen, col("red"),(foodx,foody),10)
                for module in snakelist:
                        snake_module(module[0],module[1],"black")
            else:
                pygame.draw.circle(screen, col("blue"),(foodx,foody),10)
                for module in snakelist:
                        snake_module(module[0],module[1],"white")

            if x < 0 or x >= 900 or y < 100 or y >= 700 or snakelist[0] in snakelist[1:]:
                inverse = False
                time.sleep(0.5)
                game_crash()
        else:
            message_display("PAUSED","ArcadeClassic",140,"black",300)


        pygame.display.update()
        clock.tick(12)

def game_crash():
    maxfont = 140
    font = 0
    while True:
        screen.fill(col("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        if font < maxfont:
            font += 2
        message_display("GAME OVER","ArcadeClassic",font,"black",150)
        button("Play Again >","Rect",250,300,400,100,"lime","green","FFFForward",35,game_loop)
        button("< Home","Rect",250,415,400,100, "darkgrey", "grey", "FFFForward",40, game_startscreen)
        button("Quit  X","Rect", 250,530,400,100,"red","maroon","FFFForward",40,game_quit)

        pygame.display.update()
        clock.tick(60)

def game_quit():
    pygame.quit()
    quit()

game_startscreen()
