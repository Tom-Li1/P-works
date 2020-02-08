# -- coding:utf-8--
from random import randint, choice
from sys import exit
from sys import stdout
from msvcrt import getch
from time import sleep
from os import system
import threading

def setEmptyCoordinate():
    # 创建一个60x15的界面数据架构
    board = []
    for x in range(120): # 主列表是一个包含60个列表的列表.
        board.append([])
        for y in range(28): # 主列表中的每个列表都有15个单字符串。
            board[x].append(' ')
    return board


def drawBoard(board, snake):
    print('=' * 120, end = '')

    for row in range(28):
        boardRow = ''
        for column in range(120):
            boardRow += board[column][row]
        print(boardRow, end = '')

    print('Score:' + str(len(snake)) + '=' * (120 -len('Score:' + str(len(snake)))), end = '')


def listenKeyboard():
    global direction
    while True:
        ch = getch()
        if ch == b'w':
            if direction != 'down':
                direction = 'up'
        
        elif ch == b's':
            if direction != 'up':
                direction = 'down'
        
        elif ch == b'a':
            if direction != 'right':
                direction = 'left'
        
        elif ch == b'd':
            if direction != 'left':
                direction = 'right'

def setFood(theBoard, bodyAndFood):
    while True:
        x = randint(0, 119)
        y = randint(0, 27)
        
        if theBoard[x][y] == ' ':
            theBoard[x][y] = choice(bodyAndFood)
            return [x, y]

def getNewSnake(direction, bodyAndFood):
    middle = [randint(59, 60), randint(13, 14), choice(bodyAndFood)]
    if direction == 'left':
        head = [middle[0] - 1, middle[1], choice(bodyAndFood)]
        tail = [middle[0] + 1, middle[1], choice(bodyAndFood)]

    elif direction == 'right':
        head = [middle[0] + 1, middle[1], choice(bodyAndFood)]
        tail = [middle[0] - 1, middle[1], choice(bodyAndFood)]
    
    return [head, middle, tail]

def makeMove(theBoard, snake, bodyAndFood, foodLocation, direction):
    # 根据移动方向添加一个头部，原来的头部变为身体的一部分
    if direction == 'up':
        snake.insert(0, [snake[0][0], snake[0][1] - 1, choice(bodyAndFood)])
    elif direction == 'down':
        snake.insert(0, [snake[0][0], snake[0][1] + 1, choice(bodyAndFood)])
    elif direction == 'left':
        snake.insert(0, [snake[0][0] - 1, snake[0][1], choice(bodyAndFood)])
    elif direction == 'right':
        snake.insert(0, [snake[0][0] + 1, snake[0][1], choice(bodyAndFood)])
    
    if snake[0][0] < 0 or snake[0][0] > 119 or snake[0][1] < 0 or snake[0][1] > 27:
        return 'Game Over A'
    else:
        for s in snake[1:]:
            if [snake[0][0], snake[0][1]] == [s[0], s[1]]:
                return 'Game Over B'
    # 判定头部坐标是否等于食物位置，不等于则删掉最后一节 反之，在增加头部后不减尾部则达到增长效果
    if [snake[0][0], snake[0][1]] != foodLocation:
        theBoard[snake[-1][0]][snake[-1][1]] = ' '
        del snake[-1]
    
    # 吃到就将食物坐标设置为False 来让setfood()重新设定食物
    else:
        global haveEaten
        haveEaten = True

    # 遍历蛇列表 根据坐标位置在游戏板上将空格修改为蛇身体
    for OnePartOfSnake in snake:
        theBoard[OnePartOfSnake[0]][OnePartOfSnake[1]] = OnePartOfSnake[2]

bodyAndFoodStr = "~!@#$%^&*()_+=-`1234567890[]';/.,{}:?><|\\qwertyuiopasdfghjklzxcvbnm\
QWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()_+=-`1234567890[]';/.,{}:?><|"
bodyAndFood = []
for part in bodyAndFoodStr:
    bodyAndFood.append(part)

direction = choice(['left', 'right'])
theBoard = setEmptyCoordinate()
allOfSnake = getNewSnake(direction, bodyAndFood)
for snakePart in allOfSnake:
    theBoard[snakePart[0]][snakePart[1]] = snakePart[2]
drawBoard(theBoard, allOfSnake)
foodLocation = setFood(theBoard, bodyAndFood)

mainUserUpdatet = threading.Thread(target = listenKeyboard)
mainUserUpdatet.setDaemon(True)
mainUserUpdatet.start()

haveEaten = False
while True:
    stdout.flush()
    sleep(0.03)
    system('cls')

    result = makeMove(theBoard, allOfSnake, bodyAndFood, foodLocation, direction)
    if result == 'Game Over A':
        drawBoard(theBoard, allOfSnake)
        input('Game Over, the wall is hader than your teeth!')
        break
    elif result == 'Game Over B':
        drawBoard(theBoard, allOfSnake)
        input('Game Over, your pioson your self!')
    
    drawBoard(theBoard, allOfSnake)
    
    if haveEaten == True:
        foodLocation = setFood(theBoard, bodyAndFood)
        haveEaten = False
    