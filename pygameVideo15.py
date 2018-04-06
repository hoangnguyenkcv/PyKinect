import pygame
import time 
import random


pygame.init()

display_width =800
display_height = 600
black = (0, 0 , 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0,200,0)
bright_red = (255, 0, 0)
bright_green = (0,255,0)

car_width = 30
block_color = (53, 115, 255)
# display windown

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()
carImg =  pygame.image.load('racecar.png')
carImg = pygame.transform.scale(carImg, (100, 100))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

# draw box things
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])
# display car    
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

# get text for messagee    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# display message box
def message_display(text):
    largeText = pygame.font.Font("",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
        
# show message text
def crash():
    message_display('You Crashed')
    
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    
#    print(mouse)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
#             if action == "play":
#                 game_loop()
#             elif action == "quit":
#                 pygame.quit()
#                 quit()
        
    
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)),(y +(h/2)))
    gameDisplay.blit(TextSurf, TextRect)
    
def quit_game():
    pygame.quit()
    quit()    
    
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit  Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)    
        
        button("Let Go!", 150, 450, 100, 50, green, bright_green, game_loop) 
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game) 
        
        pygame.display.update()
        clock.tick(15)
    
def game_loop():    
    # initial position of car
    x = (display_width *0.5)
    y = (display_height *0.8)
    x_change = 0

    # initial paramerter of things

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100
    dodged = 0 
    gameExit = False
    
    
    while not gameExit:
        # event  for  control position car
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 

        x += x_change           
        # display  background font
        gameDisplay.fill(white)    

        # get parameter of car
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        things_dodged(dodged)
        car(x,y)
        
        # boundary display windown
        if x > display_width - car_width or x <0 :
#             gameExit =True 
             crash()
        # created position of things  for each loop
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
        # 
        if y < thing_starty + thing_height: 
            print('y_crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width :
                print('x_crossover')
                crash()
        
        
        
        pygame.display.update()
        # frames per a second    
        clock.tick(60)

game_intro()        
game_loop()        
pygame.quit()
quit()
