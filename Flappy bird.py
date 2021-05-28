import pygame
import random
import json
WIDTH, HEIGHT = 640,500
FPS = 60
clock = pygame.time.Clock()
pygame.font.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Definitely Not Flappy Bird")
LIGHTBLUE = (173, 216, 230)
YELLOW = (255,255,0)
GREEN = (0,255,0)
SIZE = 20
WHITE = (255,255,255)
BLACK = (0,0,0)
with open("Flappybirdhighscore.txt") as loadhighscore:  
    highscoreSave = json.load(loadhighscore)
loadhighscore.close()
highscoreSave = {int(k):str(v) for k,v in highscoreSave.items()}
score = 0
scoreFont = pygame.font.Font("freesansbold.ttf",20)
usernameFont = pygame.font.Font("freesansbold.ttf",40)
scoreNumber = scoreFont.render(str(score),True,WHITE)
scoreText = scoreFont.render("Score:",True,WHITE)
highscorer = sorted(highscoreSave,reverse = True)
highscorerNumber = highscorer[0]
highscoreText = scoreFont.render("Highscore:",True,WHITE)
highscoreNumber = scoreFont.render(str(highscorerNumber),True,WHITE)
def draw(bird,upperPillar,lowerPillar,upperPillar2,lowerPillar2,upperPillar3,lowerPillar3,upperPillar4,lowerPillar4):
    global score
    global scoreNumber
    global highscorerNumber
    highscoreNumber = scoreFont.render(str(highscorerNumber),True,WHITE)
    WIN.fill(LIGHTBLUE)
    pygame.draw.rect(WIN,YELLOW,(bird.x,bird.y,bird.width,bird.height))
    pygame.draw.rect(WIN,GREEN,(upperPillar.x,upperPillar.y,upperPillar.width,upperPillar.height))
    pygame.draw.rect(WIN,GREEN,(lowerPillar.x,lowerPillar.y,lowerPillar.width,lowerPillar.height))
    pygame.draw.rect(WIN,GREEN,(upperPillar2.x,upperPillar2.y,upperPillar2.width,upperPillar2.height))
    pygame.draw.rect(WIN,GREEN,(lowerPillar2.x,lowerPillar2.y,lowerPillar2.width,lowerPillar2.height))
    pygame.draw.rect(WIN,GREEN,(upperPillar3.x,upperPillar3.y,upperPillar3.width,upperPillar3.height))
    pygame.draw.rect(WIN,GREEN,(lowerPillar3.x,lowerPillar3.y,lowerPillar3.width,lowerPillar3.height))
    pygame.draw.rect(WIN,GREEN,(upperPillar4.x,upperPillar4.y,upperPillar4.width,upperPillar4.height))
    pygame.draw.rect(WIN,GREEN,(lowerPillar4.x,lowerPillar4.y,lowerPillar4.width,lowerPillar4.height))
    pygame.Surface.blit(WIN,highscoreText,(50,0))
    pygame.Surface.blit(WIN,highscoreNumber,(155,0))
    pygame.Surface.blit(WIN,scoreText,(50,20))
    pygame.Surface.blit(WIN,scoreNumber,(115,20))
    pygame.display.update()
def main():
    global score
    global scoreNumber
    global highscorerNumber
    speedup = 1
    score = 0
    fallspeed = 0
    bird = pygame.Rect(240,270,SIZE,SIZE)
    upperPillar = pygame.Rect(640,0,SIZE*2,200)
    lowerPillar = pygame.Rect(640,350,SIZE*2,400)
    upperPillar2 = pygame.Rect(800,0,SIZE*2,200)
    lowerPillar2 = pygame.Rect(800,350,SIZE*2,400)
    upperPillar3 = pygame.Rect(960,0,SIZE*2,200)
    lowerPillar3 = pygame.Rect(960,350,SIZE*2,400)
    upperPillar4 = pygame.Rect(1120,0,SIZE*2,200)
    lowerPillar4 = pygame.Rect(1120,350,SIZE*2,400)
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.y -= 40
                    fallspeed = 0
                if event.key == pygame.K_m:
                    run = False
                    menu()
        if score == 20:
            speedup = 2
        elif score == 40:
            speedup = 3
        elif score == 60:
            speedup = 4
        bird.y += 2+fallspeed
        fallspeed += 0.04
        lowerPillar.x -= 2 * speedup
        upperPillar.x -= 2 * speedup
        upperPillar2.x -= 2 * speedup
        lowerPillar2.x -= 2 * speedup
        lowerPillar3.x -= 2 * speedup
        upperPillar3.x -= 2 * speedup
        upperPillar4.x -= 2 * speedup
        lowerPillar4.x -= 2 * speedup
#Make it so the whole between the pillars can be a lot higher or lower
#Right now the whole is more or less only in the middle
        if lowerPillar.x <= 0:
            lowerPillar.x = 640
            upperPillar.x = 640
            lowerPillar.y = round(random.randint(150,450)/25)*25
            upperPillar.height = round(random.randint(50,lowerPillar.y-100)/25)*25
        if lowerPillar2.x <= 0:
            lowerPillar2.x = 640
            upperPillar2.x = 640
            lowerPillar2.y = round(random.randint(150,450)/25)*25
            upperPillar2.height = round(random.randint(50,lowerPillar2.y-100)/25)*25
        if lowerPillar3.x <= 0:
            lowerPillar3.x = 640
            upperPillar3.x = 640
            lowerPillar3.y = round(random.randint(150,450)/25)*25
            upperPillar3.height = round(random.randint(50,lowerPillar3.y-100)/25)*25
        if lowerPillar4.x <= 0:
            lowerPillar4.x = 640
            upperPillar4.x = 640
            lowerPillar4.y = round(random.randint(150,450)/25)*25
            upperPillar4.height = round(random.randint(50,lowerPillar4.y-100)/25)*25
        if lowerPillar.x == bird.x or lowerPillar2.x == bird.x or lowerPillar3.x == bird.x or lowerPillar4.x == bird.x:
            score += 1
            if score > highscorerNumber:
                highscorerNumber = score
        pillars = [upperPillar,lowerPillar,upperPillar2,lowerPillar2,upperPillar3,lowerPillar3,upperPillar4,lowerPillar4]
        if len(bird.collidelistall(pillars)) > 0 or bird.y == 0 or bird.y > 640:
            savegame()
            main()
            run = False
        scoreNumber = scoreFont.render(str(score),True,WHITE)
        draw(bird,upperPillar,lowerPillar,upperPillar2,lowerPillar2,upperPillar3,lowerPillar3,upperPillar4,lowerPillar4)
def menu():
    menurun = True
    playrect = pygame.Rect((150,80,340,50))
    highscorerect = pygame.Rect((150,240,340,50))
    exitrect = pygame.Rect((150,400,340,50))
    playText = scoreFont.render("Play",True,BLACK)
    highscoreText = scoreFont.render("Highscores",True,BLACK)
    exitText = scoreFont.render("Exit",True,BLACK)
    while menurun:
        clock.tick(FPS)
        WIN.fill(LIGHTBLUE)
        pygame.draw.rect(WIN,GREEN,(playrect.x,playrect.y,340,50))
        pygame.draw.rect(WIN,GREEN,(highscorerect.x,highscorerect.y,340,50))
        pygame.draw.rect(WIN,GREEN,(exitrect.x,exitrect.y,340,50))
        pygame.Surface.blit(WIN,playText,(300,100))
        pygame.Surface.blit(WIN,highscoreText,(300,260))
        pygame.Surface.blit(WIN,exitText,(300,420))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menurun = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseposition = pygame.mouse.get_pos()
                if playrect.collidepoint(mouseposition) == True:
                    menurun = False
                    usernameInput()
                elif highscorerect.collidepoint(mouseposition) == True:
                    menurun = False
                    highscoreMenu()
                elif exitrect.collidepoint(mouseposition) == True:
                    menurun = False
def usernameInput():
    usernamerun = True
    global text
    text = ""
    usernameInstructions = scoreFont.render("Type a username and press tab",True,BLACK)
    while usernamerun:
        clock.tick(FPS)
        WIN.fill(LIGHTBLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                usernamerun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_TAB:
                    usernamerun = False
                    main()
                else:
                    text += event.unicode
        usernameText = scoreFont.render(text,True,BLACK)
        pygame.draw.rect(WIN,WHITE,(150,200,340,60))
        pygame.Surface.blit(WIN,usernameInstructions,(150,160))
        pygame.Surface.blit(WIN,usernameText,(150,220))
        pygame.display.update()
def highscoreMenu():
    highscoreMenuRun = True
    exitButton = pygame.Rect(0,480,40,40)
    while highscoreMenuRun:
        clock.tick(FPS)
        WIN.fill(LIGHTBLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                highscoreMenuRun = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseposition = pygame.mouse.get_pos()
                if exitButton.collidepoint(mouseposition) == True:
                    highscoreMenuRun = False
                    menu()
        for i in range(5):
            pygame.draw.rect(WIN,GREEN,(120,20+100*i,400,50))
        xnumber = 480
        xname = 130
        yhighscore = 40
        for i in sorted(highscoreSave,reverse = True):
            usernameTextscore = scoreFont.render(highscoreSave[i],True,BLACK)
            scoreText = scoreFont.render(str(i),True,BLACK)
            pygame.Surface.blit(WIN,usernameTextscore,(xname,yhighscore))
            pygame.Surface.blit(WIN,scoreText,(xnumber,yhighscore))
            yhighscore += 100
        pygame.draw.rect(WIN,GREEN,(0,480,40,40))
        exitscoremenu = scoreFont.render("Exit",True,BLACK)
        pygame.Surface.blit(WIN,exitscoremenu,(0,480))
        pygame.display.update()
def savegame():
    global score
    global text
    highscoreSave[int(score)] = text
    if len(highscoreSave) > 5:
        removeSmallestScore = sorted(highscoreSave)
        highscoreSave.pop(removeSmallestScore[0])
    with open("Flappybirdhighscore.txt","w") as saveHighescore:
        json.dump(highscoreSave,saveHighescore)
    saveHighescore.close()
menu()