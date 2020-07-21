import pygame
import time
import random
import decimal
pygame.init()

length = 1300
height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
grey = (211,211,211)

bright_red = (255,0,0)
bright_green = (0,255,0)
light_grey = (200,200,200)

pause = False



gameDisplay = pygame.display.set_mode((length,height))
pygame.display.set_caption("A Curling Game")
clock = pygame.time.Clock()

rockimg = pygame.image.load("curling rock.png")
rockimg = pygame.transform.scale(rockimg,(50,30))

def rock(x,y):
    gameDisplay.blit(rockimg,(x,y))

curlingicon = pygame.image.load("curlingicon.png")

pygame.display.set_icon(curlingicon)

thefeels = pygame.image.load("thefeels.png")
thefeels = pygame.transform.scale(thefeels,(300,300))

def the_feels(x3,y3):
    gameDisplay.blit(thefeels,(x3,y3))
    
rock_displayimg = pygame.image.load("rock.png")
rock_displayimg = pygame.transform.scale(rock_displayimg,(400,300))

def rock_display(x1,y1):
    gameDisplay.blit(rock_displayimg,(x1,y1))

feelsgoodman = pygame.image.load("Feelsgoodman.png")
feelsgoodman = pygame.transform.scale(feelsgoodman,(1000,550))

def feels_goodman(x2,y2):
    gameDisplay.blit(feelsgoodman, (x2,y2))
    
sheetimg = pygame.image.load("CurlingSheet.jpg")
sheetimg = pygame.transform.scale(sheetimg,(1150,300))

def sheet(o,p):
    gameDisplay.blit(sheetimg,(o,p))
    

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def thing_speed():
    l = 0
def message_display(text):
    largeText = pygame.font.SysFont("berlinsanafb",90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2), (height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()
    
def button(msg,x,y,w,h,ic,ac,action=None):
    global m
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "go":
                choose_point()
                
            if action == "curl":
                game_loop1()
                
            if action == "curly":
                game_loop2()
                
            if action == "ready":
                game_intro()
            
            if action == "quit":
                quit()
                
            if action == "info":
                game_info()
                

            if action == "ten":
                m = 10
                player_1()
            if action == "twenty":
                m = 20
                player_1()
            if action == "thirty":
                m = 30
                player_1()

            if action == "forty":
                m = 40
                player_1()

            if action == "fifty":
                m = 50
                player_1()

            if action == "sixty":
                m = 60
                player_1()

            if action == "dinfo":
                dinfo()

            if action == "tready":
                paused()

            if action == "unpause":
                unpause()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))                              

    smallText = pygame.font.SysFont("berlinsanafb",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), y+(h/2))
    gameDisplay.blit(textSurf, textRect)


def rock_movement(thingx, thingy):
    rock(x,y)

broomimg = pygame.image.load("broom.png")

def broom(x,y):
    gameDisplay.blit(broomimg,(x,y))
    
medal = pygame.image.load("1stmedal.png")

def medal_1st(x4,y4):
    gameDisplay.blit(medal,(x4,y4))

def crash():
    message_display("You Lost")

def unpause():
    global pause
    pause = False
    
def curl():
    game_loop()

def choose_point():

    choose_matchpoint = True

    while choose_matchpoint:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        
        mediumText = pygame.font.SysFont("berlinsanafb",50)
        TextSurf, TextRect = text_objects("Choose the match point!", mediumText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("10",100,450,100,50,red,bright_red,"ten")
        button("20",300.5,450,100,50,red,bright_red,"twenty")
        button("30",500,450,100,50,red,bright_red,"thirty")
        button("40",700,450,100,50,red,bright_red,"forty")
        button("50",900,450,100,50,red,bright_red,"fifty")
        button("60",1100,450,100,50,red,bright_red,"sixty")
        
        pygame.display.update()
        
        clock.tick(30)
            
def restart():
    global t
    global v
    restart = True

    while restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        mediumText = pygame.font.SysFont("berlinsanafb",50)
        TextSurf, TextRect = text_objects("Would you like to play another game?", mediumText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Play",350,450,100,50,green,bright_green,"go")
        button("Home",612.5,450,100,50,light_grey,grey,"info")
        button("Quit",875,450,100,50,red,bright_red,"quit")
        pygame.display.update()

        t = 0
        v = 0
        
        clock.tick(30)


def player_1():

    player = True

    while player:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        mediumText = pygame.font.SysFont("berlinsanafb",50)
        TextSurf, TextRect = text_objects("Player 1 are you ready?", mediumText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Lets Curl!",600, 450,100,50,green,bright_green,"curl")
        pygame.display.update()
        
        clock.tick(30)
        
def player_2():
    player = True

    while player:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    

        gameDisplay.fill(white)

        mediumText = pygame.font.SysFont("berlinsanafb",50)
        TextSurf, TextRect = text_objects("Player 2 are you ready?", mediumText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Lets Curl!",600, 450,100,50,green,bright_green,"curly")
        pygame.display.update()
        
        clock.tick(30)

        
def paused():
    
    global pause
    
    while pause:
        pause = True
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        rock_display(x1,y1)
        largeText = pygame.font.SysFont("berlinsanafb",90)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",350,450,100,50,green,bright_green,"unpause")
        # wip button("Info",612.5,450,100,50,light_grey,grey,"dinfo")
        button("Quit",875,450,100,50,red,bright_red,"quit")
        pygame.display.update()
        clock.tick(30)
        

def game_intro():
    gameDisplay.fill(white)
    intro = True

    while intro:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        rock_display(x1,y1)
        largeText = pygame.font.SysFont("berlinsanafb",90)
        TextSurf, TextRect = text_objects("A Curling Game", largeText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start",350,350,100,50,green,bright_green,"go")
        button("Info",612.5,350,100,50,light_grey,grey,"info")
        button("Quit",875,350,100,50,red,bright_red,"quit")
        pygame.display.update()

        clock.tick(30)
        


x1 = (length * 0.35)
y1 = (height * 0.25)
x = (length * 0.45)
y = (height * 0.8)
o = (length * 0.06)
p = (height * 0.4)
x_change = 0
car_speed = 0
t = 0
k = 0
v = 0
gameExit = False
def game_info():    
    info = True
    
    while info:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

            
      
            
        mediumText = pygame.font.SysFont("berlinsanafb",23)
        TextSurf, TextRect = text_objects("Press space to sweep. Sweeping increases the distance the rock will travel. Try to get the rock as close to the center of the target as possible! Press P to pause the game.", mediumText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)
        mediumText = pygame.font.SysFont("berlinsanafb",23)
        TextSurf, TextRect = text_objects("You will get 1 point for blue, 2 points for white, 3 points for red and 5 points if you get it in the center.", mediumText)
        TextRect.center = ((length/2), (325))
        gameDisplay.blit(TextSurf, TextRect)
        mediumText = pygame.font.SysFont("berlinsanafb",23)
        TextSurf, TextRect = text_objects("Good Luck!", mediumText)
        TextRect.center = ((length/2), (350))
        gameDisplay.blit(TextSurf, TextRect)
        mediumText = pygame.font.SysFont("berlinsanafb",20)
        TextSurf, TextRect = text_objects("Created by: Tiger Ye, 01/24/18, Mary MacKenzie, ICS201-01, Computer Programming", mediumText)
        TextRect.center = ((length/2), (400))
        gameDisplay.blit(TextSurf, TextRect)
        button("OK",600, 450,100,50,green,bright_green,"ready")
        pygame.display.update()
            
        clock.tick(60)

def dinfo():    
    dinfo = True
    
    while dinfo:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

                 
        mediumText = pygame.font.SysFont("berlinsanafb",15)
        TextSurf, TextRect = text_objects("Press space to sweep. Sweeping increases the distance the rock will travel. Try to get the rock as close to the center of the target as possible! Press P to pause the game.", mediumText)
        TextRect.center = ((length/2), (height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Ready",600, 350,100,50,green,bright_green,"tready")
        pygame.display.update()
            
        clock.tick(60)

        
def game_loop2():
    global k
    global t
    global m
    global v
    global pause
    broomx = 100 
    broomy = 110
    thing_startx = 1182
    thing_starty = 375
    thing_speed = float(decimal.Decimal(random.randrange(36,42))/10)
    x1 = (length * 0.35)
    y1 = (height * 0.25)
    x = (length * 0.45)
    x2 = (400)
    x3 = (500)
    x4 = (400)
    y = (height * 0.8)
    y2 = (200)
    y3 = (200)
    y4 = (150)
    o = (length * 0.06)
    p = (height * 0.4)
    x_change = 0
    car_speed = 0
    gameDisplay.fill(white)
    while not gameExit:
                gameDisplay.fill(white)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_SPACE:
                            broomy = broomy - 20
                            broomx = broomx - 20
                            broom(broomx,broomy)
                            thing_speed = thing_speed * 1.01
                            
                         if event.key == pygame.K_p:
                            pause = True
                            paused()
                    if event.type == pygame.KEYUP:
                
                        if event.key == pygame.K_SPACE:
                            broomx = broomx+20
                            broomy = broomy+20
                            broom(broomx,broomy)
                
                            

                gameDisplay.fill(white)

                sheet(o,p)
                if thing_startx > -100:
                        thing_startx = thing_startx - (thing_speed)
                        if thing_speed > 0.005:
                            thing_speed = thing_speed - 0.01
                        else:
                            thing_speed = 0
                            if thing_startx > 303.5 and thing_startx < 343.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("1 POINT", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                t = t + 1
                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                            if thing_startx > 264.5 and thing_startx <= 303.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("2 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                t = t + 2 

                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                            if thing_startx > 234.5 and thing_startx <= 264.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("3 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                t = t + 3
                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                            if thing_startx > 215.5 and thing_startx <= 234.5:
                                gameDisplay.fill(white)
                                feels_goodman(x2,y2)
                                mediumText = pygame.font.SysFont("berlinsanafb",60)
                                TextSurf, TextRect = text_objects("BULLSEYE 5 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(3)
                                t = t + 5
                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                            if thing_startx > 185.5 and thing_startx <= 215.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("3 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                t = t + 3
                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    medal_1st(x4,y4)
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                            if thing_startx > 147.5 and thing_startx <= 185.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("2 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                t = t+2
                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                    
                            if thing_startx > 107.5 and thing_startx < 147.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("1 POINT", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                t = t +1
                                if t < m and v < m:
                                    player_1()
                                if t >= m and t > v:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 2!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                if v == t:
                                    gameDisplay.fill(white)
                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("Tied Bonus Round!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    pygame.display.update()
                                    time.sleep(2)
                                    player_1()
                                if v > t:
                                    gameDisplay.fill(white)
                                    medal_1st(x4,y4)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                            else:
                                gameDisplay.fill(white)
                                the_feels(x3,y3)
                                if v > t and v >= m:
                                    gameDisplay.fill(white)

                                    mediumText = pygame.font.SysFont("berlinsanafb",60)
                                    TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                    TextRect.center = ((length/2), (height/2))
                                    gameDisplay.blit(TextSurf, TextRect)
                                    medal_1st(x4,y4)
                                    pygame.display.update()
                                    time.sleep(6)
                                    restart()
                                pygame.display.update()
                                time.sleep(6)
                                player_1()

                mediumText = pygame.font.SysFont("berlinsanafb",50)
                TextSurf, TextRect = text_objects("Player 2 Total Points: " + str(t), mediumText)
                TextRect.center = ((1070), (50))
                gameDisplay.blit(TextSurf, TextRect)
                

                mediumText = pygame.font.SysFont("berlinsanafb",50)
                TextSurf, TextRect = text_objects("Player 1 Total Points: "+str(v), mediumText)
                TextRect.center = ((200), (50))
                gameDisplay.blit(TextSurf, TextRect)
                
                rock(thing_startx,thing_starty)
                broom(broomx,broomy)
                broomx = thing_startx -50
                pygame.display.update()

                clock.tick(60)
    else:
        pygame.quit()
        quit()

def game_loop1():
    global v
    global t
    global m
    global pause
    broomx = 100 
    broomy = 110
    thing_startx = 1182
    thing_starty = 375
    thing_speed = float(decimal.Decimal(random.randrange(36,42))/10)
    x1 = (length * 0.35)
    y1 = (height * 0.25)
    x = (length * 0.45)
    x2 = (400)
    x3 = (400)
    x4 = (400)
    y = (height * 0.8)
    y2 = (200)
    y3 = (100)
    y4 = (150)
    o = (length * 0.06)
    p = (height * 0.4)
    x_change = 0
    car_speed = 0
    gameDisplay.fill(white)
    while not gameExit:
                gameDisplay.fill(white)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_SPACE:
                            broomy = broomy - 20
                            broomx = broomx - 20
                            broom(broomx,broomy)
                            thing_speed = thing_speed * 1.01
                            
                         if event.key == pygame.K_p:
                            pause = True
                            paused()
                    if event.type == pygame.KEYUP:
                
                        if event.key == pygame.K_SPACE:
                            broomx = broomx+20
                            broomy = broomy+20
                            broom(broomx,broomy)
                
                            

                gameDisplay.fill(white)

                sheet(o,p)
                if thing_startx > -100:
                        thing_startx = thing_startx - (thing_speed)
                        if thing_speed > 0.005:
                            thing_speed = thing_speed - 0.01
                        else:
                            thing_speed = 0
                            if thing_startx > 303.5 and thing_startx < 343.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("1 POINT", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                v = v + 1
                                if v < m:
                                    player_2()
                                if v >= m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    if v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()

                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()

                                    if v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                            if thing_startx > 264.5 and thing_startx <= 303.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("2 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                v = v + 2 
                                if v < m:
                                    player_2()
                                if v >= m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    if v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()

                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                            if thing_startx > 234.5 and thing_startx <= 264.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("3 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                v = v + 3
                                if v < m:
                                    player_2()
                                if v >= m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    if v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                            if thing_startx > 215.5 and thing_startx <= 234.5:
                                gameDisplay.fill(white)
                                feels_goodman(x2,y2)
                                mediumText = pygame.font.SysFont("berlinsanafb",60)
                                TextSurf, TextRect = text_objects("BULLSEYE 5 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(3)
                                v = v + 5
                                if v < m:
                                    player_2()
                                if v >= m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    if v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                            if thing_startx > 185.5 and thing_startx <= 215.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("3 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                v = v + 3
                                if v < m:
                                    player_2()
                                if v >= m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    if v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                            if thing_startx > 147.5 and thing_startx <= 185.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("2 POINTS", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                v = v+2
                                if v < m:
                                    player_2()
                                if v >=m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    if v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()

                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    if v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                            if thing_startx > 107.5 and thing_startx < 147.5:
                                mediumText = pygame.font.SysFont("berlinsanafb",50)
                                TextSurf, TextRect = text_objects("1 POINT", mediumText)
                                TextRect.center = ((length/2), (height/2))
                                gameDisplay.blit(TextSurf, TextRect)
                                pygame.display.update()
                                time.sleep(1)
                                v = v +1
                                if v < m:
                                    player_2()
                                if v >= m:
                                    if v > (t + 5):
                                        gameDisplay.fill(white)
                                        medal_1st(x4,y4)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("WINNER PLAYER 1!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        
                                        pygame.display.update()
                                        time.sleep(6)
                                        restart()
                                    elif v <= (t+2):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",60)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a " + str((v - t)+1) + " to win!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()

                                    if v <= (t+4):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to win the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                                        
                                    elif v == (t+5):
                                        gameDisplay.fill(white)

                                        mediumText = pygame.font.SysFont("berlinsanafb",40)
                                        TextSurf, TextRect = text_objects("Match Point! Can Player 2 score a bullseye to tie the game!", mediumText)
                                        TextRect.center = ((length/2), (height/2))
                                        gameDisplay.blit(TextSurf, TextRect)
                                        pygame.display.update()
                                        time.sleep(3)

                                        player_2()
                            else:
                                gameDisplay.fill(white)
                                the_feels(x3,y3)
                                pygame.display.update()
                                time.sleep(6)
                                player_2()
                mediumText = pygame.font.SysFont("berlinsanafb",50)
                TextSurf, TextRect = text_objects("Player 1 Total Points: "+str(v), mediumText)
                TextRect.center = ((200), (50))
                gameDisplay.blit(TextSurf, TextRect)
                
                    
                mediumText = pygame.font.SysFont("berlinsanafb",50)
                TextSurf, TextRect = text_objects("Player 2 Total Points: " + str(t), mediumText)
                TextRect.center = ((1070), (50))
                gameDisplay.blit(TextSurf, TextRect)
                        
                rock(thing_startx,thing_starty)
                broom(broomx,broomy)
                broomx = thing_startx -50
                pygame.display.update()

                clock.tick(60)
    else:
        pygame.quit()
        quit()
game_intro()

game_loop()
pygame.quit()
quit()
