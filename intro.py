#x and y are measured from topmost left screen
import pygame
import time
import random
from random import randint

pygame.init()
display_width = 900
display_height = 700
gameDisplay=pygame.display.set_mode((display_width,display_height))   #horizontal , vertical
pygame.display.set_caption('dOdger')

black = (0,0,0)
white = (255,255,255)
green=(0,190,0)
bright_green=(0,255,0)
red=(190,0,0)
bright_red=(255,0,0)
car_width=73
carImg = pygame.image.load('racecar.png')
clock=pygame.time.Clock()

	
def getRandomColor():
    return (randint(0,255),randint(0,255),randint(0,255))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def circle(color,x_cor,y_cor,rad):
     pygame.draw.circle(gameDisplay, color, (x_cor,y_cor), rad)


def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()
    
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def message_display(text,color):
    largeText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def crash():
    message_display('OOPS !! You Crashed',black)

def game_intro():
    intro=True
    while intro:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
              quit()
     gameDisplay.fill(white)
     largeText = pygame.font.Font('freesansbold.ttf',115)
     TextSurf, TextRect = text_objects("dOdger", largeText,black)
     TextRect.center = ((display_width/2),(display_height/2))
     gameDisplay.blit(TextSurf, TextRect)
     button("GO!",150,450,100,50,green,bright_green,game_loop)
     button("Quit",550,450,100,50,red,bright_red,quitgame)
     pygame.display.update()
     clock.tick(15)
    
def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change=0

    thing_startx = random.randint(0, display_width)
    rad= random.randint(50, 70)
    thing_starty = -600
    y_cor=-1000
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    count =0
    x_cor = random.randint(0, display_width)
    gameExit=False
	

    while not gameExit:#(alternatively..crashed):
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 gameExit=True
                 pygame.quit()
                 quit()
             if event.type == pygame.KEYDOWN:  #if keys are pressed
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:  #if keys are released
                    x_change = 7
             if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
         x+=x_change 
    ##         print(event)
         gameDisplay.fill(white)
         car(x,y)

         if(count==0):
          color=(0,255,0)
          col=(255,0,0)
          
         things(thing_startx, thing_starty, thing_width, thing_height,color )
         circle(col,x_cor,y_cor,rad)
         thing_starty += thing_speed
         y_cor+=thing_speed
         things_dodged(count)
         
         if x>display_width-car_width or x<0:
             crash()
             
         if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randint(0,display_width)
            count+=1
            if count%3 ==0 :
             thing_speed += 1
            thing_width += .5
            color=getRandomColor()

         if y_cor> display_height:
            y_cor = 0 - 300
            x_cor = random.randint(0,display_width)
            count+=1 
            if count%3 ==0:
             thing_speed += 1
            col=getRandomColor()
		
		

         if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
              crash()
         if y < y_cor-rad:
            if x > x_cor-rad and x < x_cor+rad or x+car_width > x_cor-rad and x + car_width < x_cor+rad:
              crash()


             
         pygame.display.update()
         clock.tick(100)   #frames per second.. for smooth display more no of frames
game_intro()
##game_loop()

