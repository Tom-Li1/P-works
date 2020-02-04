import random, sys, math, time

def getNewBoard():
    # 创建一个60x15的界面数据架构
    board = []
    for x in range(60): # 主列表是一个包含60个列表的列表.
        board.append([])
        for y in range(15): # 主列表中的每个列表都有15个单字符串。
            # 使用随机符号增加界面的可视性。
            if random.randint(0, 1) == 0:
                board[x].append('-')
            else:
                board[x].append('-')
    return board

def drawBoard(board):
    # 绘制界面数据
    tensDigitsLine = '    ' # 为界面左侧竖列数字预留空间
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # 打印横穿界面顶部的数字
    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))

    #逐次打印15横行
    for row in range(15):
        # 单个数字需要增加一个空格以对齐。
        if row < 10:
            extarSpace = ' '
        else:
            extarSpace = ''

        # 为界面上的此行创建字符串
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extarSpace, row, boardRow, row))

    # 打印横穿界面底部的数字。
    print('   ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    # 创建包含目标数据结构的列表 (一个包含xy坐标的列表)。

    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests: # 确保目标位置未被其他目标占用
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    # 如果xy坐标在界面范围内，返回True。相反， 返回False

    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    ''' 使用探测设备字符更改板数据结构。
        在找到地雷时，将其从列表中移除。
        如果是无效的移动，则返回False。
        相反，返回这次移动3的坐标。'''
    smallestDistance = 100 #任何目标的距离将会小于100
    
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy -y))

        if distance < smallestDistance:
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        # x y 直接在目标上
        chests.remove([x, y])
        return '你刚刚发现了一位地雷'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return '探测设备发现了一位距离它 %s 个距离单位的地雷' % (smallestDistance)
        else:
            board[x][y] = 'X'
            return '探测设备没有发现任何地雷 所有地雷都在它的探测范围之外'

def enterPlayerMove(previousMoves):
    # 让玩家输入放置探测设备的位置 返回一个两个元素的列表 以xy表示的整数坐标
    print('键入下一个探测设备的部署位置（0-59 0-14）或者键入 quit 退出')
    while True:
        move = input('>>>')
        
        if move.lower() == 'quit':
            print('感谢游玩')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('指定的坐标位置已被部署探测设备')
                continue
            return [int(move[0]), int(move[1])]

        print('键入一个0-59的数字 + 一个空格 + 一个0-14的数字来表示雷区内的坐标位置')

print('\n                                           Mine Clearance(中文低配版)')

print()

string_0 = "怎么玩呢？你说还能怎么玩！\n\
你要干的是使用探测设备去扫雷，一共有三个地雷，它们被埋在一片60x15的矩形雷区。\n\
你的探测设备很辣鸡，它不能告诉你地雷的具体位置，但是能告诉离它最近的那颗雷与它的直线距离。\n\
输入一个坐标来表示你的探测设备的部署位置，随后地图上会在探测设备的位置用阿拉伯数字显示离它最近的雷的距离，\n\
或者是在部署位置上显示一个'X'来表示它的探测范围内没有地雷。\n\
举个栗子：你在'6 2'位置上放下探测设备，地图上的'B'表示地雷的位置，\n\
地图上的'3'是你的探测设备，'3'表示有一个地雷埋于距离它三个单位的位置。"
string_1 ='''

				            1         2         3
				  012345678901234567890123456789012
				0 --------------------------------- 0
				1 --------------------------------- 1
				2 ---B--3------B------------------- 2
				3 --------------------------------- 3
				4 -------------B------------------- 4
				  012345678901234567890123456789012
				            1         2         3
			     (游戏中不会显示地雷位置，按回车'enter'键继续)'''

string_2 = "当你在地雷所在的坐标上放置声纳设备时，你就扫到一颗雷了，随后地雷会被移除，这时探测设备上的数字会改变，\n\
数字会变成其他地雷距离此探测设备的直线距离。你在放置探测设备于'6 2'后，又在'3 2'部署了另一个探测设备。\n\
在'3 2'上的探测设备显示'X'表示探测范围内没有地雷。"
string_3 = '''

				            1         2         3
				  012345678901234567890123456789012
				0 --------------------------------- 0
				1 --------------------------------- 1
				2 ---X--7------B------------------- 2
				3 --------------------------------- 3
				4 -------------B------------------- 4
				  012345678901234567890123456789012
				            1         2         3
				            '''

string_4 = "探测设备的最大探测范围是'10'。尝试在用完探测设备之前发现所有地雷！\n\
\n\
--------------------Good Luck Have Fun--------------------"

insOrNot =  input('想看看说明吗？键入yes/no\n>>>')
print()

if insOrNot.lower().startswith('y'):

	for i in range(len(string_0)):
		print(string_0[i], end = '')
		time.sleep(0.01)
		sys.stdout.flush()
	
	print(string_1)
	input()

	for i in range(len(string_2)):
		print(string_2[i], end = '')
		time.sleep(0.01)
		sys.stdout.flush()
	
	print(string_3)

	for i in range(len(string_4)):
		print(string_4[i], end = '')
		time.sleep(0.01)
		sys.stdout.flush()
	print()
	input("准备好了就按回车'enter'键！")

while True:
    print()
    #建立一局游戏
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        #展示探测设备与地雷的状态
        print('目前剩余探测设备 ：%s\n目前剩余地雷     ：%s' % (sonarDevices, len(theChests)))
        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x, y]) #追踪每次的放置位置以便更新

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue

        else:
            if moveResult == '你刚刚发现了一位地雷':
                # 更新所有地图上的探测设备
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('你已将所有地雷位置标记完毕 雷区探测工作完成')
            break

        sonarDevices -= 1

    if sonarDevices == 0:
        print('探测设备已用尽 仍有剩余地雷未被发现 扫雷失败\n剩余地雷坐标：')
        for x, y in theChests:
            print('(%s. %s)' % (x, y))
            #肏你妈哇塞

    print('再试一次？键入yes/no')
    if not input('>>>').lower().startswith('y'):
        sys.exit()