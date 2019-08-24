#!/usr/bin/env python3
"""
===========================================================================

    ***************************************************
    ***************** ACCIDENT ESCAPE *****************
    ***************************************************
    ***************************************************
    ***************** HamidReza Momeni ****************
    ***************************************************

    Game Name: Accident Escape        
    Game Author: HamidReza Momeni
    Game Version: 0.1
    Game Discription: Accident Escape is a simple and fun game with python
    Game Github: https://github.com/hamidrezaMomeni/AccidentEscape
    Author Github: https://github.com/hamidrezaMomeni
    Author Instagram: https://instagram.com/hamidreza_momeni_
    Author Telegram: https://t.me/hamidrezaPK7

============================================================================
"""
import pygame
import random
import time
# start pygame
pygame.init()
# set width and hieght for display window
width = 700
height = 600
# set colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
lightRed = (150,0,0)
orange = (255, 100, 0)
blue = (0, 83, 255)
yellow = (245, 219, 0)
green = (0,255,0)
lightGreen = (0,150,0)
purple = (148, 3, 252)
pink = (252, 3, 140)
gray = (240,240,240)
colorList = [green, pink, red, blue, purple, yellow, orange]
# create game display and caption for title window and clock
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("AccidentEscape Game")
clock = pygame.time.Clock()
# get and load car image
carImg1 = pygame.image.load("Bug.png")
carImg2 = pygame.image.load("Bug2.png")
carImg3 = pygame.image.load("Bug3.png")
carImg4 = pygame.image.load("Bug4.png")
carImg5 = pygame.image.load("Bug5.png")
carList = (carImg1,carImg2,carImg3,carImg4,carImg5)
car = random.choice(carList)
boyImg = pygame.image.load("boy.png")
# hovering button
def button(msg,x,y,w,h,ia,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ia,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()
            else: 
                quit()
    else:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf, TextRect = textObjects(msg, smallText)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)
    mouse = pygame.mouse.get_pos()
    
# this function drawing a rect object and insert into game display
# , stuffW, stuffH, color
def stuff(stuffX, stuffY,car):
    gameDisplay.blit(car, (stuffX,stuffY))
# set x,y position car for show to game display
def carPosition(x,y):
    gameDisplay.blit(boyImg, (x,y))
# get render and return text with your font selection
def textObjects(text,fonts):
    textSurface = fonts.render(text, True, black)
    return textSurface,textSurface.get_rect()
# stop game and show message and run game again
def messageDisplay(msg):
    # select font family and font size for show to user
    largText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = textObjects(msg, largText)
    textRect.center = ((width/2), (height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(4)
    gameIntro("are you want play again?")
# when user accidented stop game and show message
def crash():
    messageDisplay("you Crashed !!")
# show on top display user score
def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: {}".format(str(count)), True, black)
    gameDisplay.blit(text, (1,1))
# welcome screen to show user
def gameIntro(title):
    intro = True
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                
        gameDisplay.fill(gray)
        largText = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = textObjects(title, largText)
        textRect.center = ((width/2), (height/2))
        gameDisplay.blit(textSurf, textRect)
        # button for start or quit from game
        button("Play",100,450,100,50,green,lightGreen,"play")
        button("Exit",500,450,100,50,red,lightRed,"quit")
        #pygame.draw.rect(gameDisplay, red, (500,450,100,50))
        pygame.display.update()
# Game components loop
bestScore = 0
def gameLoop():
    # set y position and random x position for car and another information
    xPosRange = (0.25,0.45,0.65,0.85)
    xPosRand = random.choice(xPosRange)
    xPosition = (width * xPosRand) 
    yPosition = (height * 0.88)
    xChange = 0
    counter = 0
    carWidth = 64
    global bestScore
    # set some variable for generate stuff
    stuffStartX = random.randrange(0,width)
    stuffStartY = -600
    stuffSpeed = 4
    stuffWidth = 64
    stuffHeight = 64
    #stuffColor = random.choice(colorList)
    car = random.choice(carList)
    # set default state for user
    gameExit = False
    # An endless loop until the user loss
    while not gameExit:
        # A loop to capture all the events while playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                elif event.key == pygame.K_RIGHT:
                    xChange = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
        # apply x change for car
        xPosition += xChange
        # filling screen with white color
        gameDisplay.fill(gray)
        # show car in x,y Position 
        carPosition(xPosition, yPosition)
        # show user score in the top window
        score(counter)
        # generate stuff and scroll down from sky
        stuff(stuffStartX,stuffStartY,car)
        #########stuff(stuffStartX,stuffStartY,stuffWidth,stuffHeight,stuffColor)
        stuffStartY += stuffSpeed
        # when car accidented with left and right wall
        if xPosition > width - 32 or xPosition < 0:
            crash()
        # rain stuff from sky and calculate user score
        if stuffStartY > height:
            stuffStartY = 0 - stuffHeight
            stuffStartX = random.randrange(64,width - 64)
            #stuffColor = random.choice(colorList)
            car = random.choice(carList)
            counter += 1
            # if score 5 level upgraded speed stuff up to +1
            if counter % 5 == 0:
                stuffSpeed += 1
        # when accident stuff with car
        
        font = pygame.font.SysFont(None, 30)
        text = font.render("Best Score: {}".format(str(bestScore)), True, lightGreen)
        gameDisplay.blit(text, (550,1))
        pygame.display.update()
        
        
        if yPosition < stuffStartY + stuffHeight:
            if xPosition > stuffStartX and xPosition < stuffStartX + stuffWidth or xPosition + carWidth > stuffStartX and xPosition + carWidth < stuffStartX + stuffWidth:
                if counter > bestScore:
                    bestScore = counter
                crash()
        # game display updating
        
        pygame.display.update()
        # run game with 80 frame/second
        clock.tick(80)
# running game form the first time
gameIntro("Game Starting, You Ready?")
gameLoop()
# quit from pygame library and python file
pygame.quit()
quit()


