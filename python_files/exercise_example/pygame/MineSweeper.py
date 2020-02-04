import sys
import time
import random

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
    tenDigitsLine = '   '
    OneToTenDigitsLine = '  '
    for i in range(1, 6):
        tenDigitsLine += (' ' * 9 + str(i))
    
    for i in range(6):
        OneToTenDigitsLine += '0123456789'

    print(tenDigitsLine)
    print(OneToTenDigitsLine)

    for y in range(20):
        if y < 10:
            space = ' '
        else:
            space = ''
        
        row = ''
        for x in range(60):
            row += theBoard[x][y]
        print('%s%s%s%s' % (space, y, row, y))

    print(OneToTenDigitsLine)
    print(tenDigitsLine)
    
def printOneByOne(data,wait_time=0.06,second_line=True):
 #用于进行单个字符打印的函数
	for i in range(len(data)):
		print(data[i], end = "")
		sys.stdout.flush()
		time.sleep(wait_time)
	if second_line == True:
		print()

def setMines(MineNumber):
    mines = []
    while len(mines) < MineNumber:
        mine = [random.randint(0, 59), random.randint(0, 19)]
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
        if len(moveList) == 2 or len(moveList) == 3:
            if moveList[0].isdigit() and moveList[1].isdigit():
                if isOnBoard(moveList[0], moveList[1]):
                    if len(moveList) == 2:
                        if theBoard[int(moveList[0])][int(moveList[1])] != 'X':
                            if theBoard[int(moveList[0])][int(moveList[1])] == '-':
                                moveList.append('')
                                return moveList
                            else:
                                printOneByOne('这个位置的盖子已经被翻开')
                        else:
                            printOneByOne('确定要翻开已经被标记地雷的盖子？若要翻开请先取消标记')
                    elif len(moveList) == 3:
                        if moveList[2] == '-':
                            if theBoard[int(moveList[0])][int(moveList[1])] == 'X':
                                return moveList
                            else:
                                printOneByOne('要取消标记的位置已被翻开或未曾被标记')
                        elif not moveList[2].isdigit() and moveList[2].upper() == 'X':
                            if theBoard[int(moveList[0])][int(moveList[1])] == '-':
                                moveList[2] = 'X'
                                return moveList
                            else:
                                printOneByOne('要标记的位置已经被翻开')
                        else:
                            printOneByOne("若要标记地雷 请将第三个参数输入为'X' 在标记过的位置取消标记则输入为'-'")
                else:
                    printOneByOne("坐标位置超出游戏范围了")
            else:
                printOneByOne("前两个参数为你要检查的盖子的'坐标' 确保它们都是'数字'")
        else:
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
                    drawBoard(theBoard)
                    print(len(waitingCheckList))
                else:
                    theBoard[i[0]][i[1]] = ' '
                    drawBoard(theBoard)
                    print(len(waitingCheckList))

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
    tenDigitsLine = '   '
    OneToTenDigitsLine = '  '
    for i in range(1, 6):
        tenDigitsLine += (' ' * 9 + str(i))
    
    for i in range(6):
        OneToTenDigitsLine += '0123456789'

    print(tenDigitsLine)
    print(OneToTenDigitsLine)

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
        print('%s%s%s%s' % (space, y, row, y))

    print(OneToTenDigitsLine)
    print(tenDigitsLine)

def isGameWin(theBoard, mines):
    for y in range(20):
        for x in range(60):
            if [x, y] not in mines and theBoard[x][y] in 'X-':
                return False
    return True

while True:
    theBoard = getNewBoard()
    drawBoard(theBoard)
    mines = setMines(10)

    while True:
        if isGameWin(theBoard, mines):
            printOneByOne("你 赢 了!")
            printOneByOne("所有未部署地雷的盖子都被翻开 ")
            if input('再来一局吗(yes/no)？\n>>>').lower().startswith('y'):
                    break
            else:
                sys.exit()

        moveList = getPlayerMove(theBoard)
        result = makeMove(moveList[0], moveList[1], mines, mark = moveList[2])
        if result:
            print(result)
            if '游戏结束' in result:
                drawMinesBoard(theBoard, mines)
                printOneByOne(result)
                if input('再来一局吗(yes/no)？\n>>>').lower().startswith('y'):
                    break
                
                else:
                    sys.exit()
        else:
            drawBoard(theBoard)