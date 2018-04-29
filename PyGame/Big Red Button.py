import pygame
from random import randint
from PIL import ImageColor as IC

pygame.init()

width = 800
height = 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Do Not Press the Red Button.")
clock = pygame.time.Clock()

gameIcon = pygame.image.load('Button.png')
pygame.display.set_icon(gameIcon)

doge = pygame.image.load("doge.jpg")
dogewidth = doge.get_width()
dogeheight = doge.get_height()
#-20 from the row number to find the index
textfile = ["DO NOT PRESS",
            "*ahem*...DO NOT PRESS",
            "I repeat...don't press the button.",
            "...",
            "So you're not gonna listen?",
            "Well...okay then. Go ahead punk, press it.",
            "Yeah, do it again.",
            "Come on, one more time.",
            "Again.",
            "Do it.",
            "Okay, you've pressed it enough.",
            "Stop it.",
            "STOP IT!",
            "See, this is the problem between us.",
            "There's just no compromise at all.",
            "Just pure selfishness.",
            "Stop it.",     
            "You've had your fun. Just stop.",
            "Grr.",
            "S",
            "T",
            "O",
            "P",
            " ",
            "I",
            "T",
            ".", 
            "You seem to be immune to my mind control.",
            "Time for plan B. Press it. You know you want to.",    
            "BWAHAHAHA! Let's see you press it now, loser!",
            "Oh screw you.",   
            "Ha! I have replaced this button with a cute animal!",
            "Let's see how you press this!",
            "...you monster.",  
            "I really hate you. Did you know that?",
            '''In a "cut your nails off with a chainsaw" sort of way.''',   
            "Quick! What's behind you?!",
            "Which one is it?",
            "Not so smart now, are you?",
            "Congrats!", 
            "You beat a completely pointless minigame!",
            "Doing absolutely nothing productive.",
            "At all.", 
            "Okay, okay, you can press the button.",
            "I don't care.",
            "No really, I don't care anymore.",   
            "In fact, I lost interest quite a while ago.",
            "I'm just doing this to entertain you.",         
            "Don't you like doing anything else?",
            "Singing?",
            "Coding?",
            "Clicking a button for the rest of eternity?",    
            "Just kidding. You don't just like that last one.",
            "You LOVE it.",
            "How about colouring? That sounds like fun.", 
            "Pick a colour! This one's on me.",
            "Green? Fine.",
            "Pick the red one.",
            "Pick the green one.",
            "Pick the green one again.",
            "See, you can't trust me all the time.",
            "Or can you?",
            "You know, I'm glad we got to spend so much time together.", 
            "Doesn't it make you want to stop clicking big red buttons?",
            "No, seriously, look deep inside yourself.",  
            "Deeper.",
            "Deeper!",
            "DEEPER!!",
            "If the world was about to explode if you pressed the button,",
            "would you press it?", 
            "See, you've could have died right there.",
            "And there.",
            "You know, eventually I'm going to stop you.",       
            "The world is going to explode,",
            "But all you care about is pressing buttons.",
            "Okay, it's really gonna explode this time. I promise.",
            "BOOM! You're dead.",
            "That wasn't very smart, now was it?",   
            "Everyone's dead now. Even you.",
            "I'm not. I'm just text on a screen.",
            "But you. You're just dead.",         
            "Considering how much time you're wasting,",
            "you're probably already dead inside.",
            "Stop clicking.",
            "Stop.",
            "Now.", 
            "I'll start talking upside down if you click one more time.",
            "Ha! Can't read me now, can you?",
            "What? You never wanted to read me anyway?!",  
            "Well I'll show you...",
            " ",
            " ",
            " ",
            " ",
            " ",
            "You really are stubborn.",
            "Please stop clicking.",
            "Look, you've reduced me to begging.",
            "So please stop.",
            "PLEASE!!",
            "I'll give you ten cents.",
            "Twenty?",
            "Fifty?",
            "A dollar?",
            "Aww come on! Just stop!",    
            "That does it!",
            "Time to unleash my master plan!",
            "BEHOLD!",
            "The power of animation!",
            "H8!",
            "Let's get funky!",
            "I bet by now you're starting to wonder why you've",
            "been doing this for so long.",
            "Like geez, all you've been doing",
            "is clicking a red button.",
            "How lame is that?",
            "But there is a bonus to all this clicking.",
            "I can't tell you about it.",
            "It's a secret.",
            "Got you going, didn't I?",   
            "You should see the look on your face right now.",
            "HA!",
            "But seriously, there is a secret.",
            "There's been one this whole time.",  
            "You really wanna know?",
            "Well okay.",
            "While you were busy clicking away at this red button...",
            "...there's been a little white button",   
            "watching your every move this whole time!",
            "MWHAAHAAHAAHAHA!!",
            "HAHAHA!",
            "BWHAAH!",
            "MUAAHH!",
            "Haha!",
            "hehe",
            "lol",
            "rofl",
            "roflmao",
            "roflmaoqxz",
            "and so on and so forth.",
            "...","*whistles*",
            "Find it yet?",
            "Look harder!",
            "It's right under your nose.",
            "I know where it is,",
            "but I'll never tell...",
            "Or maybe I will...",
            "But ya gotta stop clicking first!",
            "Stop.",
            "Fine, I won't tell you.",
            "Go ahead, try to find it yourself.",
            "You'll never find it.",
            "Well, you might...",
            "But the odds are against you.",
            "...","What's your favourite letter?",
            "Mine is the dot!",
            "...",
            "Find it yet?",
            "No?","Then stop clicking and I'll tell you.",
            "You know what?",
            "POOF! It's gone!",
            "Has anyone ever slapped you?",
            "Because I will.",
            "Really, I will.",
            "It won't hurt though.",
            "Because you're dead.",
            "D-E-D",
            "Remember?",
            "You went and blew up the entire planet!",
            "Thought I'd forget about that, didn't you?",
            "But an elephant never forgets!",
            "...or something along those lines.",
            "You killed everyone.",
            "Sikko.",
            "What would your mother say?",
            "That's right...feel ashamed.",
            "The world is null and you're to blame.",
            "I'd recommend suicide, but you're dead already.",
            "There's only one thing left to do...",
            "Dude, you're dead.",
            "What are you gaining from this?",
            "Okay,everytime you click, you",
            "get sent to a lower layer of hell.",
            "Welcome to layer 1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "BOOM! You've exploded Hell.",
            "I hope you're happy.",
            "Heaven's gone too.",
            "That's how smooth you are.",
            "Now you're dead, and there's no Heaven or Hell.",
            "How does it feel?",
            "You've condemned the world to limbo.",
            "I once shot a man in limbo.",
            "Or was he doing the limbo?",
            "Meh, tomato tornado.",
            "This is getting boring, isn't it?",
            "No special effects or graphics to keep you interested.",
            "But you can't stop!",
            "You want to leave your computer and end this.",
            "But you can't!",
            "You need to see if there's a pot of gold",
            "at the end of the rainbow!",
            "But I've already told you how to find the pot of gold.",
            "Follow the white brick road.",
            "...erm, button.",
            "Remember the hidden button?",
            "Or are you so self-centred you forgot about that too?",
            "I could keep you here all day if I wanted.",
            "You're in my world now.",
            "No matter how much you hate it,",
            "you have to press the button.",
            "again",
            "and again...",
            "and again.",
            "You just keep hoping something good will come of this.",
            "Sure I could tell you if I wanted to,",
            "but I'm not gonna.",
            "You decided to keep clicking.",
            "So I'm gonna enjoy it.",
            "I mean, there's nothing else to enjoy.",
            "You blew everything up, remember?",
            "You're probably wondering who I am.",
            "Well, let me tell you a tale about myself.",
            "One day, I was walking home from work and",
            "I saw a little house.",
            "I knocked the door out of curiosity",
            "to see if anyone was home.",
            "The door opened.",
            "But no one was there.",
            "I went inside to check it out but found nothing.",
            "...nothing but a little metal box.",
            "So I opened it.",
            "Protecting the box's contents was a layer of foam.",
            "I removed the foam.",
            "And there it was...",
            "...",
            "... ...",
            "zzz",
            "ZZZzzzzz",
            "zzzZZZzzz",
            "ZZZzzzZZZ",
            "ZZZZZZZZZZ",
            "Huh?",
            "Oh right! The story!",
            "So there I was holding this little metal box in my hands.",
            "The top was open and sitting inside was this...",
            "A big red button.",
            "And do you know what it said?",
            "Oh, you wouldn't believe what it said!",
            "It said this:"]

smallbuttonlist = [29]
dogelist = [31]
tributtonlist = [37]
tricolbuttonlist = [57,58,59]
invertedtextlist = [87,88,89]
animatedbuttonlist = [107]
funkylist = [110]
funkydict = {(90,100):[(400,410)], (55,52):[(175,350),(625, 500),(675,275)],(35,30):[(440,250),(170,540),(550,305)], (25,20):[(510,590),(275,275),(250,455),(640,385),(365,555)]}
gonelist = [163]
multilist = [39,43,60,68,73,81,97,105,111,113,117,120,122,127,143,145,151,153,170,179,181,194,197,207,216,222,224,230,232,240]

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
    TextRect.center = (int((width/2)),int((height/x)))
    
    screen.blit(TextSurf, TextRect)

def circle_button(fontsize,x,y,r,ac,ic, msg = None):
    global text_no
    smallText = pygame.font.SysFont("FFFForward",fontsize)
    textSurf, textRect = text_objects(msg, smallText,ic)
    textRect.center = (x*1.0175,y*1.0244)
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.circle(screen, col(ic),(x,y),r)
    if pygame.draw.circle(screen, col(ic), (x,y), r).collidepoint(mouse[0]-1,mouse[1]-1) == True:
        pygame.draw.circle(screen, col(ac),(x,y),r)     
        screen.blit(textSurf, textRect)
    else:
        pygame.draw.circle(screen, col(ic),(x,y),r)
    

def quitgame():
    pygame.quit()
    quit()

def game_loop():
    global text_no
    game = True
    text_no = 0
    buttonx = 400
    buttony = 410
    buttonac = "red"
    buttonic = "maroon"
    left = 1
    x_change = 0 
    while game:
        buttonr = 90
        buttonfontsize = 100
        screen.fill(col("white"))
        message_display("DO NOT PRESS THE BUTTON", "ArcadeClassic", 60, "black", 7)
        
        if text_no in smallbuttonlist:
            buttonr = 5
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx,buttony,buttonr, buttonac, buttonic)
            
        elif text_no in dogelist:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            message_display(textfile[text_no + 1], "FFFForward", 20, "black", 2.6)
            screen.blit(doge, (buttonx - buttonr*1.1, buttony - buttonr*1.1))
            
        elif text_no in tributtonlist:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            message_display(textfile[text_no+1], "FFFForward", 20, "black", 2.6)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx,buttony,buttonr, buttonac, buttonic, "!")
            pygame.draw.circle(screen, col("darkgrey"), (buttonx-200, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx-200,buttony,buttonr, buttonac, buttonic, "!")
            pygame.draw.circle(screen, col("darkgrey"), (buttonx+200, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx+200,buttony,buttonr, buttonac, buttonic, "!")
            
        elif text_no in tricolbuttonlist:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx,buttony,buttonr, "blue", "navy", "!")
            pygame.draw.circle(screen, col("darkgrey"), (buttonx-200, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx-200,buttony,buttonr, buttonac, buttonic, "!")
            pygame.draw.circle(screen, col("darkgrey"), (buttonx+200, buttony), int(buttonr*1.1)) 
            circle_button(buttonfontsize, buttonx+200,buttony,buttonr, "lime", "green", "!")
            
        elif text_no in invertedtextlist:
            message_display(textfile[text_no],"FFFForward", 20, "black", 3, 180)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx, buttony), int(buttonr*1.1)) 
            circle_button(buttonfontsize, buttonx,buttony,buttonr, buttonac, buttonic, "!")
            
        elif text_no in animatedbuttonlist:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            message_display(textfile[text_no+1], "FFFForward", 20, "black", 2.6)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx+x_change, buttony), int(buttonr*1.1)) 
            circle_button(buttonfontsize, buttonx + x_change,buttony,buttonr, buttonac, buttonic, "!")
            if x_change > 210:
                left = 0
            if x_change < -210:
                left = 1
            if left == 1:
                x_change += 3
            elif left == 0:
                x_change -= 3
                
        elif text_no in funkylist:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3.5)
            for key in funkydict.keys():
                for xy in funkydict[key]:
                    pygame.draw.circle(screen, col("darkgrey"), (xy[0], xy[1]), int(key[0]*1.1))
                    if key[0] == 90:
                        circle_button( buttonfontsize, buttonx,buttony,buttonr, buttonac, buttonic, "!")
                    else:
                        circle_button(key[1], xy[0],xy[1],key[0],buttonac, buttonic)
                        
        elif text_no in gonelist:
            circle_button(buttonfontsize, 458,215,6, buttonac, buttonic)
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            
        elif text_no in multilist:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            message_display(textfile[text_no + 1], "FFFForward", 20, "black", 2.6)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx, buttony), int(buttonr*1.1)) 
            circle_button( buttonfontsize, buttonx,buttony,buttonr, buttonac, buttonic, "!")
        
        else:
            message_display(textfile[text_no], "FFFForward", 20, "black", 3)
            pygame.draw.circle(screen, col("darkgrey"), (buttonx, buttony), int(buttonr*1.1)) 
            circle_button(buttonfontsize, buttonx,buttony,buttonr, buttonac, buttonic, "!")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_no == len(textfile)-1:
                    text_no = 0
                elif text_no in gonelist:
                   if pygame.draw.circle(screen, col(buttonic) , (458,215),6).collidepoint(event.pos) == True:
                        text_no += 1 
                elif text_no in funkylist:
                    if pygame.draw.circle(screen, col(buttonic) , (275,275), 25).collidepoint(event.pos) == True:
                        text_no += 1
                elif text_no in animatedbuttonlist:
                    if pygame.draw.circle(screen, col(buttonic) , (buttonx+x_change,buttony), buttonr).collidepoint(event.pos) == True:
                        text_no += 2
                elif text_no == tricolbuttonlist[2]:
                    if pygame.draw.circle(screen, col("navy") , (buttonx ,buttony), buttonr).collidepoint(event.pos) == True:
                        text_no += 1
                elif text_no == tricolbuttonlist[1]:
                    if pygame.draw.circle(screen, col("green") , (buttonx + 200,buttony), buttonr).collidepoint(event.pos) == True:
                        text_no += 1
                elif text_no == tricolbuttonlist[0]:
                    if pygame.draw.circle(screen, col(buttonic) , (buttonx - 200,buttony), buttonr).collidepoint(event.pos) == True:
                        text_no += 1           
                elif text_no in tributtonlist:
                    if pygame.draw.circle(screen, col(buttonic) , (buttonx + 200,buttony), buttonr).collidepoint(event.pos) == True:
                        text_no += 2
                elif text_no in dogelist:
                    if event.pos[0]> buttonx - int(buttonr*1.1) and event.pos[0] < buttonx - int(buttonr*1.1) + dogewidth:
                        if event.pos[1]> buttony - int(buttonr*1.1) and event.pos[1] < buttony - int(buttonr*1.1) + dogeheight:
                            text_no += 2
                elif text_no in smallbuttonlist:
                    if pygame.draw.circle(screen, col(buttonic) , (buttonx,buttony), 6).collidepoint(event.pos) == True:
                        text_no += 1
                elif pygame.draw.circle(screen, col(buttonic) , (buttonx,buttony), buttonr).collidepoint(event.pos) == True:
                    if text_no in multilist:
                        text_no += 2
                    else:
                        text_no += 1
        pygame.display.update()
        clock.tick(60)

game_loop()
        
