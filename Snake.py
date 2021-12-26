#Импорт библиотек
import pygame
from pygame import color
from pygame.constants import WINDOWHITTEST
from pygame import RESIZABLE
import random
import time
from pygame.time import Clock
pygame.init()
pygame.display.set_caption("Snake by Vadim")
#Создаём цвета
FIOL = (200, 0, 255)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (17, 17, 17)
RED = (255, 0, 0)
GREEN = (40, 255, 40)
LIGHTGRAY = (80, 80, 80)
#FPS
clock = pygame.time.Clock()
#Создаём окно pygame
sc = pygame.display.set_mode((480, 480))
#Красим в серый. В будущем будем наносить змейку яблоко надписи и тд
sc.fill(GRAY)
#Функция для отображения головы
def printsnake(y, color):
            for f in range(0, 20):
                for h in range(0, 20):
                    if snake[f][h] == y:
                        dx = h * 24
                        dy = f * 24
                        pygame.draw.rect(sc, color, (dx, dy, 24, 24))
#Функция рисования туловища (gradient)
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
#Функция рисования туловища (default)
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
#Функция рисования надписей
def printtext(str, vis, x, y):
    fontObj = pygame.font.Font(None, vis)
    textSurfaceObj = fontObj.render(str, True, LIGHTGRAY, GRAY)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    sc.blit(textSurfaceObj, textRectObj)
#Рисуем надписи стартового меню
printtext('Hello! This is my first game!', 50, 240, 20)
printtext('This is snake :D', 45, 240, 60)
printtext('How to game:', 45, 240, 120)
printtext('move: W A S D or keys UP LEFT DOWN RIGHT', 30, 240, 180)
printtext('change skin snake default/gradient: left shift', 27, 240, 210)
printtext('change your skin: number 1-5', 30, 240, 240)
printtext('change mod game default/easy: space', 30, 240, 270)
printtext('press esc to pause game', 30, 240, 300)
printtext('Start game: enter', 50, 240, 380)
#И выводим их
pygame.display.update()
#FPS EASY MODE
FPSE = 8
#Переменная старт отвечает за старт игры при нажатии enter
start = False
while True:
    #Цикл что бы зафиксировать нажатия exit или enter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start = True
    #Стартуем игру
    while start:
        #reload отвчает за перезапуск игры
        reload = False
        #Это список поля. Здесь хранятся змейка пустоты яблоки и тд
        snake = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        #Этот цикл заполняет пустатой список snake
        for p in range(0, 20):
            for i in range(0, 20):
                snake[p].append("o")
        #Кидаем на поле голову змейки
        snake[9][9] = "x"
        gk = 9
        gp = 9
        #dvizh отвечает на вектор движения
        dvizh = 0
        #Эта переменная отвечает за спавн яблок
        apple = True
        #не помню
        m = 1
        #Длинна змейки
        tall = 3
        #Это список голов из прошлого, то есть это будущие хвосты. Я с помошю этого списка вывожу туловище и удаляю хвост 
        snak = []
        #Отвечает за смерть
        died = False
        #режим игры от которого зависит будем мы умирать от стен или нет
        mode = "hard"
        #Цвет туловища
        cvet = "DARKGREEN"
        #не помню
        music = 1
        #Если я ем яблоко, то мне нужно пропустить несколько раз проигрывание звука ходьбы. Эта переменная считает кадры
        soundmove = 1
        #отвечает за отображение змейки, градиент или дефолт
        snakeref = "default"
        #Цвет головы
        golova = GREEN
        #Отвечает за паузу
        stopgame = False
        #FPS
        FPS = 8
        #начало игры
        while True:
            #Заполняем экран серым
            sc.fill(GRAY)
            #Все кнопки и что они делают
            press = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if not snake[gk - 1][gp] == "z":
                            dvizh = 1
                            press = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if not snake[gk][gp + 1] == "z":
                            dvizh = 2
                            press = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if not snake[gk + 1][gp] == "z":
                            dvizh = 3
                            press = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if not snake[gk][gp - 1] == "z":
                            dvizh = 4
                            press = True
                    if event.key == pygame.K_ESCAPE:
                        if not dvizh == 0: 
                            dvizh = 0
                            stopgame = True
                        else:
                            stopgame = False
                            dvizh = dvizh
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
                            mode = "superhard"
                            FPS = 8
                        elif mode == "superhard":
                            mode = "easy"
                        elif mode == "easy":
                            mode = "hard"
                        
            #добавление голов в список голов разного времени
            for i in range(len(snake)):
                for j in range(len(snake[i])):
                    if snake[i][j] == "x" and not dvizh == 0:
                        gk = i
                        gp = j
                        a = [gk, gp]
                        snak.append(a)
                        break;
            #Для яблока (конкпретнее не помню)
            trueapple = False
            #Спавн яблока
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
                FPS += 0.5
                tall += 1
            if not mode == "easy":
                #Движение смерть и поедание яблок
                if dvizh == 1:
                    if (gk - 1) == -1 or snake[gk - 1][gp] == "z":
                        died = True
                    if not died and snake[gk - 1][gp] == "a":
                        apple = True
                    if not died:
                        snake[gk - 1][gp] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 2:
                    if (gp + 1) == 20 or snake[gk][gp + 1] == "z":
                        died = True
                    if not died and snake[gk][gp + 1] == "a":
                        apple = True
                    if not died:
                        snake[gk][gp + 1] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 3:
                    if (gk + 1) == 20 or snake[gk + 1][gp] == "z":
                        died = True
                    if not died and snake[gk + 1][gp] == "a":
                        apple = True
                    if not died:
                        snake[gk + 1][gp] = "x"
                        snake[gk][gp] = "z"
                if dvizh == 4:
                    if (gp - 1) == -1 or snake[gk][gp - 1] == "z":
                        died = True
                    if not died and snake[gk][gp - 1] == "a":
                        apple = True
                    if not died:
                        snake[gk][gp - 1] = "x"
                        snake[gk][gp] = "z"
            if mode == "easy":
                #тоже самое только с телепортирующими стенами 
                if dvizh == 1:
                    if snake[gk - 1][gp] == "z":
                        died = True
                    if not died and snake[gk - 1][gp] == "a":
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
                        apple = True
                    if (gp - 1) == -1:
                        if snake[gk][19] == "z":
                            died = True
                        snake[gk][19] = "x"
                        snake[gk][gp] = "z"
                    elif not died:
                        snake[gk][gp - 1] = "x"
                        snake[gk][gp] = "z"
            #Звуки
            if apple:
                pygame.mixer.music.load('apple.mp3')
                pygame.mixer.music.play(0)
                soundmove = 1
            if soundmove > 7:
                soundmove = 6
            if not dvizh == 0:
                if not died and not apple and soundmove == 7:
                    pygame.mixer.music.load('move.mp3')
                    pygame.mixer.music.play(0)
                    soundmove = 6
            soundmove += 1
            #Удаление слишком давних голов (то есть кончики хвоста)
            for i in range(0, len(snak)):
                if len(snak) > tall:
                    snak.remove(snak[0])
            if len(snak) == tall and not dvizh == 0:
                snake[snak[0][0]][snak[0][1]] = "o"
            for j in range(0, len(snake)):
                for h in range(0, len(snake)):
                    if snake[j][h] == "z":
                        z = 0
                        for i in range(0, len(snak)):
                            if not j == snak[i][0] and not h == snak[i][1]:
                                z += 1
                        if z == tall:
                            snake[j][h] = "o"
            
            #Вывод змейки и яблока
            printsnake("x", golova)
            if snakeref == "gradient":
                printtul(cvet)
            if snakeref == "default":
                printtuldef(cvet)
            printsnake("a", RED)
            #Меню паузы
            if stopgame:
                sc.fill(GRAY)
                printtext('Stop menu', 50, 240, 200)
                printtext('press esc to resume game', 20, 240, 235)
            #Меню и звук смерти
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
            #Отрисовка всего кадра который мы создали выше
            pygame.display.update()
            #Ждём пока наступит след кадр
            if mode == "superhard":
                clock.tick(FPS)
            else:
                clock.tick(FPSE)

