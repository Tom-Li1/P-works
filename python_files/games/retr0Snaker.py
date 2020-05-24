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
    print('{:=^120}'.format('Score:' + str(len(snake))), end = '')
    
    for row in range(28):
        boardRow = ''
        for column in range(120):
            boardRow += board[column][row]
        print(boardRow, end = '')

    print('=' * 120, end = '')


def listenKeyboard():
    global direction
    global gameIsDone
    global time
    global escGame

    while True:
        if gameIsDone != False:
            exit()
            
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

        elif ch == b' ':
            if time == 0.05:
                time = 0.01
            else:
                time = 0.05

        elif ch == b'\x1b':
            escGame = True


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
    global escGame

    if direction == 'up':
        snake.insert(0, [snake[0][0], snake[0][1] - 1, choice(bodyAndFood)])
    elif direction == 'down':
        snake.insert(0, [snake[0][0], snake[0][1] + 1, choice(bodyAndFood)])
    elif direction == 'left':
        snake.insert(0, [snake[0][0] - 1, snake[0][1], choice(bodyAndFood)])
    elif direction == 'right':
        snake.insert(0, [snake[0][0] + 1, snake[0][1], choice(bodyAndFood)])
    
    if snake[0][0] < 0 or snake[0][0] > 119 or snake[0][1] < 0 or snake[0][1] > 27:
        return 'Game Over'
    else:
        for s in snake[1:]:
            if [snake[0][0], snake[0][1]] == [s[0], s[1]]:
                return 'Game Over'
    if escGame:
        return 'Game Over'
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

def drawGameOverBoard(numberOfInfo):
    global gameIsDone
    info = [
    'Play Again',
    'Quit the Game',
    '->         Play Again           ',
    '->       Quit the Game          ',
    'PLAY ',
    'Quit the Game',
    '->           PLAY               ',
    '->       Quit the Game          ']
    
    if gameIsDone == True:
        if numberOfInfo == 'pa':
            info_1 = info[2]
            info_2 = info[1]

        elif numberOfInfo == 'q':
            info_1 = info[0]
            info_2 = info[3]

        else:
            info_1 = info[0]
            info_2 = info[1]

        print(r'''

                                 _____   ___  ___  ___ _____   _____  _   _ ___________ 
                                |  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \
                                | |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /
                                | | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / 
                                | |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ 
                                 \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|''')

    elif gameIsDone == 'Start':
        if numberOfInfo == 'p':
            info_1 = info[6]
            info_2 = info[5]

        elif numberOfInfo == 'q':
            info_1 = info[4]
            info_2 = info[7]

        else:
            info_1 = info[4]
            info_2 = info[5]

        print(r'''

   $$$$$$$\              $$\                                $$$$$$\                      $$\                           
   $$  __$$\             $$ |                              $$  __$$\                     $$ |                          
   $$ |  $$ | $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\        $$ /  \__|$$$$$$$\   $$$$$$\  $$ |  $$\  $$$$$$\   $$$$$$\  
   $$$$$$$  |$$  __$$\ \_$$  _|  $$  __$$\ $$  __$$\       \$$$$$$\  $$  __$$\  \____$$\ $$ | $$  |$$  __$$\ $$  __$$\ 
   $$  __$$< $$$$$$$$ |  $$ |    $$ |  \__|$$ /  $$ |       \____$$\ $$ |  $$ | $$$$$$$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
   $$ |  $$ |$$   ____|  $$ |$$\ $$ |      $$ |  $$ |      $$\   $$ |$$ |  $$ |$$  __$$ |$$  _$$<  $$   ____|$$ |      
   $$ |  $$ |\$$$$$$$\   \$$$$  |$$ |      \$$$$$$  |      \$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ | \$$\ \$$$$$$$\ $$ |      
   \__|  \__| \_______|   \____/ \__|       \______/        \______/ \__|  \__| \_______|\__|  \__| \_______|\__|''')

    

    for i in range(4):
        print()

    print(' ' * int(((120-len(info_1)) / 2)) + info_1)

    print("\n\n\n\n\n\n")

    print(' ' * int(((120-len(info_2)) / 2)) + info_2)

    print('\n\n')

    print(r'''                                Select what you want to do with 'W', 'S' and 'Enter' keys
        W
      A S D --- Change the direction of movement | Space --- Increase movement speed | Esc --- Quit while playing''')

gameIsDone = 'Start'
direction = choice(['left', 'right'])

drawGameOverBoard('w')
sel = 'w'
while True:
    ch = getch()
    system('cls')
    if ch == b'w':
        drawGameOverBoard('p')
        sel = 'p'
    elif ch == b's':
        drawGameOverBoard('q')
        sel = 'q'
    elif ch == b'\r':
        if sel == 'p':
            system('cls')
            break
        elif sel == 'q':
            exit()
        else:
            drawGameOverBoard('w')
    else:
        drawGameOverBoard('w')

while True:
    gameIsDone = False
    mainUserUpdatet = threading.Thread(target = listenKeyboard)
    mainUserUpdatet.setDaemon(True)
    mainUserUpdatet.start()

    bodyAndFood = choice(['O', '0', '@', '#', '$', 'S N A K E'.split(), 'P Y T H O N'.split()])
    escGame = False
    direction = choice(['left', 'right'])
    theBoard = setEmptyCoordinate()
    allOfSnake = getNewSnake(direction, bodyAndFood)
    for snakePart in allOfSnake:
        theBoard[snakePart[0]][snakePart[1]] = snakePart[2]
    drawBoard(theBoard, allOfSnake)
    foodLocation = setFood(theBoard, bodyAndFood)
    haveEaten = False
    restart = False
    time = 0.05

    while True:
        stdout.flush()
        sleep(time)
        system('cls')

        result = makeMove(theBoard, allOfSnake, bodyAndFood, foodLocation, direction)
        if result == 'Game Over':
            gameIsDone = True
            for i in range(3):
                drawBoard(setEmptyCoordinate(), allOfSnake)
                stdout.flush()
                sleep(0.2)
                system('cls')
                drawBoard(theBoard, allOfSnake)
                stdout.flush()
                sleep(0.2)
                system('cls')
                
                drawGameOverBoard('w')
                sel = 'w'
            
            while True:
                ch = getch()
                system('cls')

                if ch == b'w':
                    drawGameOverBoard('pa')
                    sel = 'pa'

                elif ch == b's':
                    drawGameOverBoard('q')
                    sel = 'q'

                elif ch == b'\r':
                    if sel == 'pa':
                        restart = True
                        break

                    elif sel == 'q':
                        exit()

                    else:
                        drawGameOverBoard('w')

                else:
                    drawGameOverBoard('s')
                    system('cls')
        if restart:
            break
        
        drawBoard(theBoard, allOfSnake)
        
        if haveEaten == True:
            foodLocation = setFood(theBoard, bodyAndFood)
            haveEaten = False