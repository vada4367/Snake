import pygame
from pygame import color
from pygame.constants import WINDOWHITTEST
from pygame import RESIZABLE
import random
import time
from pygame.time import Clock
pygame.init()
pygame.display.set_caption("Snake by Vadim")
FIOL = (150, 0, 255)
BROWN = (100, 50, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
LIME = (100, 255, 100)
PINK = (255, 0, 255)
ORANGE = (255, 150, 0)
GRAY = (17, 17, 17)
RED = (255, 0, 0)
GREEN = (40, 255, 40)
LIGHTGRAY = (80, 80, 80)
clock = pygame.time.Clock()
sc = pygame.display.set_mode((480, 480))
sc.fill(GRAY)
def printsnake(y, color):
            for f in range(0, 20):
                for h in range(0, 20):
                    if snake[f][h] == y:
                        dx = h * 24
                        dy = f * 24
                        pygame.draw.rect(sc, color, (dx, dy, 24, 24))
def printtul(color):
    bright = 255
    for i in range(1, len(snak)):
        db = 255 // len(snak)
        bright = bright - db
        if color == "DARKGREEN":
            fgh = (0, 255 - bright, 0)
        if color == "DARKBLUE":
                    fgh = (0, 0, 255 - bright)
        if color == "DARKFIOL":
                    fgh = (255 - bright - 18, 0, 255 - bright)
        if color == "DARKWHITE":
                    fgh = (255 - bright, 255 - bright, 255 - bright)
        if color == "DARKYELLOW":
                    fgh = (255 - bright, 255 - bright, 0)
        dy = snak[i][0] * 24
        dx = snak[i][1] * 24
        pygame.draw.rect(sc, fgh, (dx, dy, 24, 24))
def printtuldef(color):
    for i in range(1, len(snak)):
        dy = snak[i][0] * 24
        dx = snak[i][1] * 24
        bright = 200
        if color == "DARKGREEN":
            pygame.draw.rect(sc, (0, bright, 0), (dx, dy, 24, 24))
        if color == "DARKBLUE":
            pygame.draw.rect(sc, (0, 0, bright), (dx, dy, 24, 24))
        if color == "DARKFIOL":
            pygame.draw.rect(sc, (bright - 50, 0, bright), (dx, dy, 24, 24))
        if color == "DARKWHITE":
            pygame.draw.rect(sc, (bright, bright, bright), (dx, dy, 24, 24))
        if color == "DARKYELLOW":
            pygame.draw.rect(sc, (bright, bright, 0), (dx, dy, 24, 24))
def printtext(str, vis, x, y):
    fontObj = pygame.font.Font(None, vis)
    textSurfaceObj = fontObj.render(str, True, LIGHTGRAY, GRAY)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    sc.blit(textSurfaceObj, textRectObj)
printtext('Hello! This is my first game!', 50, 240, 20)
printtext('This is snake :D', 45, 240, 60)
printtext('How to game:', 45, 240, 120)
printtext('move: W A S D', 30, 240, 180)
printtext('change skin snake default/gradient: left shift', 27, 240, 210)
printtext('change your skin: number 1-5', 30, 240, 240)
printtext('change mod game default/easy: space', 30, 240, 270)
printtext('Start game: enter', 50, 240, 380)
pygame.display.update()
FPS = 7
start = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start = True
    while start:
        reload = False
        snake = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        for p in range(0, 20):
            for i in range(0, 20):
                snake[p].append("o")
        snake[9][9] = "x"
        dvizh = 0
        apple = True
        m = 1
        tall = 3
        snak = []
        died = False
        mode = "hard"
        cvet = "DARKGREEN"
        music = 1
        soundmove = 1
        snakeref = "default"
        golova = GREEN
        while True:
            sc.fill(GRAY)
            press = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and not dvizh == 3 and not press:
                        dvizh = 1
                        press = True
                    if event.key == pygame.K_d and not dvizh == 4 and not press:
                        dvizh = 2
                        press = True
                    if event.key == pygame.K_s and not dvizh == 1 and not press:
                        dvizh = 3
                        press = True
                    if event.key == pygame.K_a and not dvizh == 2 and not press:
                        dvizh = 4
                        press = True
                    if event.key == pygame.K_1:
                        cvet = "DARKGREEN"
                        golova = GREEN
                    if event.key == pygame.K_2:
                        cvet = "DARKBLUE"
                        golova = BLUE
                    if event.key == pygame.K_3:
                        cvet = "DARKFIOL"
                        golova = FIOL
                    if event.key == pygame.K_4:
                        cvet = "DARKYELLOW"
                        golova = YELLOW
                    if event.key == pygame.K_5:
                        cvet = "DARKWHITE"
                        golova = WHITE
                    if event.key == pygame.K_r:
                        reload = True
                    if event.key == pygame.K_LSHIFT:
                        if snakeref == "default":
                            snakeref = "gradient"
                        else:
                            snakeref = "default"
                    if event.key == pygame.K_SPACE:
                        if mode == "hard":
                            mode = "easy"
                        else:
                            mode = "hard"
            for i in range(len(snake)):
                for j in range(len(snake[i])):
                    if snake[i][j] == "x":
                        gk = i
                        gp = j
                        a = [gk, gp]
                        snak.append(a)
                        break;
            trueapple = False
            for i in range(len(snake)):
                for j in range(len(snake[i])):
                    if snake[i][j] == "a":
                        trueapple = True
            if not trueapple:
                apple = True
            if apple:
                e = random.randint(0, 19)
                ee = random.randint(0, 19)
                if snake[e][ee] == "o":
                    snake[e][ee] = "a"
                    apple = False
            if mode == "hard":
                if dvizh == 1:
                    if (gk - 1) == -1 or snake[gk - 1][gp] == "z":
                        died = True
                    if not died and snake[gk - 1][gp] == "a":
                        tall += 1
                        apple = True
                    if not died:
                        snake[gk - 1][gp] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 2:
                    if (gp + 1) == 20 or snake[gk][gp + 1] == "z":
                        died = True
                    if not died and snake[gk][gp + 1] == "a":
                        tall += 1
                        apple = True
                    if not died:
                        snake[gk][gp + 1] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 3:
                    if (gk + 1) == 20 or snake[gk + 1][gp] == "z":
                        died = True
                    if not died and snake[gk + 1][gp] == "a":
                        tall += 1
                        apple = True
                    if not died:
                        snake[gk + 1][gp] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 4:
                    if (gp - 1) == -1 or snake[gk][gp - 1] == "z":
                        died = True
                    if not died and snake[gk][gp - 1] == "a":
                        tall += 1
                        apple = True
                    if not died:
                        snake[gk][gp - 1] = "x"
                        snake[gk][gp] = "z"
            if mode == "easy":
                if dvizh == 1:
                    if snake[gk - 1][gp] == "z":
                        died = True
                    if not died and snake[gk - 1][gp] == "a":
                        tall += 1
                        apple = True
                    if (gk - 1) == -1:
                        if snake[19][gp] == "z":
                            died = True
                        snake[19][gp] = "x"
                        snake[gk][gp] = "z"
                    elif not died:
                        snake[gk - 1][gp] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 2:
                    if not (gp + 1) == 20 and snake[gk][gp + 1] == "z":
                        died = True
                    if not (gp + 1) == 20 and not died and snake[gk][gp + 1] == "a":
                        tall += 1
                        apple = True
                    if (gp + 1) == 20:
                        if snake[gk][0] == "z":
                            died = True
                        snake[gk][0] = "x"
                        snake[gk][gp] = "z"
                    elif not died:
                        snake[gk][gp + 1] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 3:
                    if not (gk + 1) == 20 and snake[gk + 1][gp] == "z":
                        died = True
                    if not (gk + 1) == 20 and not died and snake[gk + 1][gp] == "a":
                        tall += 1
                        apple = True
                    if (gk + 1) == 20:
                        if snake[0][gp] == "z":
                            died = True
                        snake[0][gp] = "x"
                        snake[gk][gp] = "z"
                    elif not died:
                        snake[gk + 1][gp] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 4:
                    if not (gp - 1) == -1 and snake[gk][gp - 1] == "z":
                        died = True
                    if not (gp - 1) == -1 and not died and snake[gk][gp - 1] == "a":
                        tall += 1
                        apple = True
                    if (gp - 1) == -1:
                        if snake[gk][19] == "z":
                            died = True
                        snake[gk][19] = "x"
                        snake[gk][gp] = "z"
                    elif not died:
                        snake[gk][gp - 1] = "x"
                        snake[gk][gp] = "z"
            if apple:
                pygame.mixer.music.load('apple.mp3')
                pygame.mixer.music.play(0)
                soundmove = 1
            if soundmove > 7:
                soundmove = 6
            if dvizh == 1 or dvizh == 2 or dvizh == 3 or dvizh == 4:
                if not died and not apple and soundmove == 7:
                    pygame.mixer.music.load('move.mp3')
                    pygame.mixer.music.play(0)
                    soundmove = 6
            soundmove += 1
            if len(snak) > tall:
                snak.remove(snak[0])
            if len(snak) == tall:
                snake[snak[0][0]][snak[0][1]] = "o"
            printsnake("x", golova)
            if snakeref == "gradient":
                printtul(cvet)
            if snakeref == "default":
                printtuldef(cvet)
            printsnake("a", RED)
            if died:
                if music == 1:
                    pygame.mixer.music.load('died.mp3')
                    pygame.mixer.music.play(0)
                    music = 2
                sc.fill(GRAY)
                fontObj = pygame.font.Font(None, 50)
                textSurfaceObj = fontObj.render('You score is: ' + str(tall), True, LIGHTGRAY, GRAY)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (240, 240)
                sc.blit(textSurfaceObj, textRectObj)
                printtext('Press R to reload', 24, 240, 280)
                if reload:
                    break;
            pygame.display.update()
            clock.tick(FPS)