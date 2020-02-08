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
    printOneByOne("无聊的作者还原了WindowsXP上的扫雷，为了凸显创意他便将DOS当作游戏界面了。\n\
游戏的规则并没有改变，但是还有许多不同点，这就是说明的用处所在了：\n\
首先你不能通过鼠标点击来表示你下一步要检查哪个格子，你只能输入格子的坐标来表示他的位置。\n\
如果你想要标记雷点，呢么需要在坐标后面加上一个空格和'X'。先展示一下游戏界面方便举个例子：", 0.03)

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
    
    printOneByOne("如果你想要翻开'!'所在个格子，那你应该输入'3 2'，因为它上下所对的数字为3，左右所对的数字为2。\n\
如果你要将'?'所在的格子标记为地雷，那你应输入'14 1 X'，因为上下对的数字为14而左右为1，最后加X为表示表记地雷。\n\
最后加上'-'则表示你要取消标记。游戏规则没有改变，和普通的扫雷是一样的。你可以在游戏中途输入'quit'退出。\n\
当你翻开所有不是地雷的格子后，你就赢了这局游戏。当你翻开地雷所在的盖子时，你就输掉了。\n\
随后会展示所有地雷的位置，在界面上表示为'M'，你已经标记到到的地雷会表示为'√'。\n", 0.03)

    input("当你读完后按回车'enter'键继续......")

    printOneByOne("\n每当你输入完一个格子的坐标后按下回车，如果没有'X'或'-'则表示你要翻开这个格子。\n\
随后这个格子可能会变成一个数字，或者是一块区域变成空的，亦或你脸黑第一次就翻到地雷了......\n\
如果变成了一个数字，那它就表示围着这个数字的八个格子里雷的数量，比如：你翻开一个格子，\n\
随后它变成了'1'，则表示它周围八个格子里有一个地雷，变成'2'或者'3'等等数字都是以此类推。\n\
如果你翻完一个格子后它变成空白，或者它周围一片区域也变成空白了，就像下面的例子一样，\n\
那就代表这这个格子的周围一个地雷都没有，此时电脑会帮你翻开周围的八个格子，这就是为啥有时候空了一片。", 0.03)

    print('''
                                1         2         3
                      012345678901234567890123456789012
                    0 -------------------11------------ 0
                    1 ------1-----------1  1----------- 1
                    2 ------------------1   1---------- 2
                    3 ----3-------------21111---------- 3
                    4 --------------------------------- 4
                      012345678901234567890123456789012
                                1         2         3
                                                                   ''')
    input("教程到此结束，按下回车'enter'键开始游戏。\n")

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
printOneByOne('\n需要看一下说明吗？（如果这是你第一次尝试它，那作者认为你需要看一看）', 0.03)

while True:
    showOrNot = input('(yes/no)>>>')
    if showOrNot.lower().startswith('y'):
        showHowToPlay()
        system('cls')
        break
    elif showOrNot.lower().startswith('n'):
        printOneByOne('那你可真聪明')
        sleep(1)
        system('cls')
        break
    else:
        printOneByOne('啥意思？')
        continue

    
while True:
    printOneByOne('你要在1200个格子里埋多少颗雷？')
    while True:
        MN = input('>>>')
        if MN.isdigit() and int(MN) <= 1200:
            mines = setMines(int(MN))
            system('cls')
            break
        else:
            printOneByOne("你填写的内容并不符合要求，一共1200个格子......")

    theBoard = getNewBoard()
    drawBoard(theBoard)
    if showOrNot.lower().startswith('n'):
        printOneByOne('懵逼了吧')
    
    while True:
        if isGameWin(theBoard, mines):
            printOneByOne("你 赢 了!")
            printOneByOne("所有未部署地雷的盖子都被翻开 ")
            if input('再来一局吗(yes/no)？\n>>>').lower().startswith('y'):
                    showOrNot = 'yes'
                    system('cls')
                    break
            else:
                exit()

        moveList = getPlayerMove(theBoard)
        result = makeMove(moveList[0], moveList[1], mines, mark = moveList[2])
        if result:
            if '游戏结束' in result:
                system('cls')
                drawMinesBoard(theBoard, mines)
                printOneByOne(result)
                if input('再来一局吗(yes/no)？\n>>>').lower().startswith('y'):
                    showOrNot = 'yes'                    
                    system('cls')
                    break
                
                else:
                    exit()
        else:
            system('cls')
            drawBoard(theBoard)