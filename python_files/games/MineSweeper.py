from sys import stdout, exit
from time import sleep
from random import randint
from os import system

def getNewBoard():
    # 创建坐标阵的数据结构
    theBoard = []
    
    for x in range(60):
        theBoard.append([])
        for y in range(20):
            theBoard[x].append('-')

    return theBoard

def drawBoard(theBoard):
    # 将坐标阵可视化
    tenDigitsLine = '    '
    OneToTenDigitsLine = '   '
    for i in range(1, 6):
        tenDigitsLine += (' ' * 9 + str(i))
    
    for i in range(6):
        OneToTenDigitsLine += '0123456789'

    print(tenDigitsLine)
    print(OneToTenDigitsLine)
    print('  ' + (len(OneToTenDigitsLine)-1) * '=')

    for y in range(20):
        if y < 10:
            space = ' '
        else:
            space = ''
        
        row = ''
        for x in range(60):
            row += theBoard[x][y]
        print('%s%s|%s|%s' % (space, y, row, y))
    
    print('  ' + (len(OneToTenDigitsLine)-1) * '=')
    print(OneToTenDigitsLine)
    print(tenDigitsLine)
    
def printOneByOne(data,wait_time=0.06,second_line=True):
 #用于进行单个字符打印的函数
	for i in range(len(data)):
		print(data[i], end = "")
		stdout.flush()
		sleep(wait_time)
	if second_line == True:
		print()

def setMines(MineNumber):
    mines = []
    while len(mines) < MineNumber:
        mine = [randint(0, 59), randint(0, 19)]
        if mine not in mines:
            mines.append(mine)
    return mines

def isOnBoard(x, y):
    if int(x) >= 0 and int(x) <= 59 and int(y) >= 0 and int(y) <= 19:
        return True
    return False

def getPlayerMove(theBoard):
    while True:
        moveList = input('>>>').split()
        if moveList[0].lower() == 'quit':
            exit()
        if len(moveList) == 2 or len(moveList) == 3:
            if moveList[0].isdigit() and moveList[1].isdigit():
                if isOnBoard(moveList[0], moveList[1]):
                    if len(moveList) == 2:
                        if theBoard[int(moveList[0])][int(moveList[1])] != 'X':
                            if theBoard[int(moveList[0])][int(moveList[1])] == '-':
                                moveList.append('')
                                return moveList
                            else:
                                system('cls')
                                drawBoard(theBoard)
                                printOneByOne('这个位置的盖子已经被翻开')
                        else:
                            system('cls')
                            drawBoard(theBoard)
                            printOneByOne('确定要翻开已经被标记地雷的盖子？若要翻开请先取消标记')
                    elif len(moveList) == 3:
                        if moveList[2] == '-':
                            if theBoard[int(moveList[0])][int(moveList[1])] == 'X':
                                return moveList
                            else:
                                system('cls')
                                drawBoard(theBoard)
                                printOneByOne('要取消标记的位置已被翻开或未曾被标记')
                        elif not moveList[2].isdigit() and moveList[2].upper() == 'X':
                            if theBoard[int(moveList[0])][int(moveList[1])] == '-':
                                moveList[2] = 'X'
                                return moveList
                            else:
                                system('cls')
                                drawBoard(theBoard)
                                printOneByOne('要标记的位置已经被翻开')
                        else:
                            system('cls')
                            drawBoard(theBoard)
                            printOneByOne("若要标记地雷 请将第三个参数输入为'X' 在标记过的位置取消标记则输入为'-'")
                else:
                    system('cls')
                    drawBoard(theBoard)
                    printOneByOne("坐标位置超出游戏范围了")
            else:
                system('cls')
                drawBoard(theBoard)
                printOneByOne("前两个参数为你要检查的盖子的'坐标' 确保它们都是'数字'")
        else:
            system('cls')
            drawBoard(theBoard)
            printOneByOne("翻开需提供'2'个参数 标记盖子需提供'3'个参数并将第3个参数填为'X'")

def computerMoveNoneMineBlock(mines, waitingCheckList):
    # 用与帮助玩家翻开周围八格都没有地雷的空格子及其周边格子 此函数由其他函数调用
    # 遍历待翻列表 检测其中的每一项
    # 如果为数字格子 则翻开后不动 如果为空 则翻开后将周边的添加至待翻列表中
    # 完成一次循环 回到首部
    global theBoard
    haveAlreadyChacked = []
    while waitingCheckList != []:
        for i in waitingCheckList:        
            if i not in haveAlreadyChacked:
                mineNumber = 0
                arounds = [
                    [i[0], i[1] + 1],
                    [i[0], i[1] - 1],
                    [i[0] - 1, i[1]],
                    [i[0] + 1, i[1]],
                    [i[0] - 1, i[1] + 1],
                    [i[0] - 1, i[1] - 1],
                    [i[0] + 1, i[1] + 1],
                    [i[0] + 1, i[1] - 1]
                    ]
                
                for around in arounds:
                    if isOnBoard(around[0], around[1]) and around in mines:
                        mineNumber += 1
                
                if mineNumber != 0:
                    theBoard[i[0]][i[1]] = str(mineNumber)
    
                else:
                    theBoard[i[0]][i[1]] = ' '
                    for around in arounds:
                        if isOnBoard(around[0], around[1]) and \
                            around not in haveAlreadyChacked and \
                                around not in waitingCheckList:
                            waitingCheckList.append(around)
                
                haveAlreadyChacked.append(i)
                waitingCheckList.remove(i)

def makeMove(x, y, mines, mark = ''):
    global theBoard
    x = int(x)
    y = int(y)
    
    if mark == '':
        if [x, y] in mines:
            return '你翻开的(' + str(x) + ',' + str(y) + ')为地雷 游戏结束'
            theBoard[x][y] == '!'
        else:
            numberOfMine = 0
            arounds = [
                [x, y + 1],
                [x, y - 1],
                [x - 1, y],
                [x + 1, y],
                [x - 1, y + 1],
                [x - 1, y - 1],
                [x + 1, y + 1],
                [x + 1, y - 1]
                ]
            
            for around in arounds:
                if isOnBoard(around[0], around[1]) == False or theBoard[around[0]][around[1]] == 'X' \
                    or theBoard[around[0]][around[1]] == ' ':
                    pass
                else:
                    if [around[0], around[1]] in mines:
                        numberOfMine += 1
            
            if numberOfMine != 0:
                theBoard[x][y] = str(numberOfMine)
            
            else:
                computerMoveNoneMineBlock(mines, waitingCheckList = [[x, y]])

    elif mark.upper() == 'X':
        theBoard[x][y] = 'X'
    
    elif mark == '-':
        theBoard[x][y] = '-'

    else:
        return "如果要标记地雷 请将第三个参数输入为'X' 取消标记则输入为'-'"

def drawMinesBoard(theBoard, mines):
    # 在玩家失败后列出所有地雷
    tenDigitsLine = '    '
    OneToTenDigitsLine = '   '
    for i in range(1, 6):
        tenDigitsLine += (' ' * 9 + str(i))
    
    for i in range(6):
        OneToTenDigitsLine += '0123456789'

    print(tenDigitsLine)
    print(OneToTenDigitsLine)
    print('  ' + (len(OneToTenDigitsLine)-1) * '=')

    for y in range(20):
        if y < 10:
            space = ' '
        else:
            space = ''
        
        row = ''
        for x in range(60):
            if theBoard[x][y] == 'X' and [x, y] in mines:
                row += '√'
            elif [x, y] in mines:
                row += 'M'
            else:
                row += theBoard[x][y]
        print('%s%s|%s|%s' % (space, y, row, y))
    
    print('  ' + (len(OneToTenDigitsLine)-1) * '=')
    print(OneToTenDigitsLine)
    print(tenDigitsLine)

def isGameWin(theBoard, mines):
    for y in range(20):
        for x in range(60):
            if [x, y] not in mines and theBoard[x][y] in 'X-':
                return False
    return True

def showHowToPlay():
    printOneByOne("输入坐标来表示格子的位置，坐标加X表示标记格子。\n", 0.03)

    print('''
                                1         2         3
                      012345678901234567890123456789012
                    0 --------------------------------- 0
                    1 --------------?------------------ 1
                    2 ---!----------------------------- 2
                    3 --------------------------------- 3
                    4 --------------------------------- 4
                      012345678901234567890123456789012
                                1         2         3
                                                                   ''')
    
    printOneByOne("输入'3 2'可翻开！所在位置。输入'14 1 X'可将？所在位置标记地雷\n\
最后加'-'可删除标记。输入'quit'退出。\n\
游戏结束后，'M'表示未被发现的地雷，'√'则代表已被发现的。\n", 0.03)

    input("按'enter'键开始\n")

sleep(0.8)
print(r'''
                             __  __ _                                                
                            |  \/  (_)_ __   ___
                            | |\/| | | '_ \ / _ \
                            | |  | | | | | |  __/
                            |_|  |_|_|_| |_|\___|''')
sleep(1)
system('cls')
print(r'''
                             __  __ _              ____                                   
                            |  \/  (_)_ __   ___  / ___|_      _____  ___ _ __   ___ _ __ 
                            | |\/| | | '_ \ / _ \ \___ \ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|
                            | |  | | | | | |  __/  ___) \ V  V /  __/  __/ |_) |  __/ |   
                            |_|  |_|_|_| |_|\___| |____/ \_/\_/ \___|\___| .__/ \___|_|
                                                                         |_| ''', end = '')
sleep(1)
printOneByOne('in the DOS! v1.0.1', 0.03)
sleep(0.8)
printOneByOne('\n展示说明？（y/n）', 0.03)

while True:
    showOrNot = input('(yes/no)>>>')
    if showOrNot.lower().startswith('y'):
        showHowToPlay()
        system('cls')
        break
    elif showOrNot.lower().startswith('n'):
        printOneByOne('NB')
        sleep(1)
        system('cls')
        break
    else:
        printOneByOne('？？？')
        continue

    
while True:
    printOneByOne('提供地雷数量')
    while True:
        MN = input('>>>')
        if MN.isdigit() and int(MN) <= 1200:
            mines = setMines(int(MN))
            system('cls')
            break
        else:
            printOneByOne("数值范围：0-1200的整数")

    theBoard = getNewBoard()
    drawBoard(theBoard)
    if showOrNot.lower().startswith('n'):
        printOneByOne('SB')
    
    while True:
        if isGameWin(theBoard, mines):
            printOneByOne("你赢")
            printOneByOne("NB ")
            if input('重新开始(yes/no)？\n>>>').lower().startswith('y'):
                    showOrNot = 'yes'
                    system('cls')
                    break
            else:
                exit()

        moveList = getPlayerMove(theBoard)
        result = makeMove(moveList[0], moveList[1], mines, mark = moveList[2])
        if result:
            if 'GAME OVER' in result:
                system('cls')
                drawMinesBoard(theBoard, mines)
                printOneByOne(result)
                if input('重来(yes/no)？\n>>>').lower().startswith('y'):
                    showOrNot = 'yes'                    
                    system('cls')
                    break
                
                else:
                    exit()
        else:
            system('cls')
            drawBoard(theBoard)