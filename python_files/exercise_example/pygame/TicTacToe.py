import random, time, sys

#==============导入适用模块，进入函数区域===============
def drawBoard(board):
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
	letter = ''
	
	while letter != 'O' or letter != 'X':
		print('Do you want to be X or O?')
		letter = input('>>>').upper()

		if letter == 'X':
			return ['X', 'O']

		else:
			return ['O', 'X']

def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'player'

	else:
		return 'computer'

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or
		(bo[4] == le and bo[5] == le and bo[6] == le) or
		(bo[1] == le and bo[2] == le and bo[3] == le) or
		(bo[7] == le and bo[4] == le and bo[1] == le) or
		(bo[5] == le and bo[8] == le and bo[2] == le) or
		(bo[3] == le and bo[6] == le and bo[9] == le) or
		(bo[7] == le and bo[5] == le and bo[3] == le) or
		(bo[1] == le and bo[5] == le and bo[9] == le))

def getBoardCopy(board):
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

def isSpaceFree(board, move):
	return board[move] == ' '

def getPlayerMove(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print("What is your next move? (1-9)")
		move = input('>>>')
	return int(move)

def chooseRandomMoveFormList(board, moveList):
	possibleMoves = []
	for i in moveList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	for i in range (1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, computerLetter, i)
			if isWinner(boardCopy, computerLetter):
				return i

	for i in range (1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, playerLetter, i)
			if isWinner(boardCopy, playerLetter):
				return i

	move = chooseRandomMoveFormList(board, [1, 3, 7, 9])
	if move != None:
		return move

	if isSpaceFree(board, 5):
		return 5

	return chooseRandomMoveFormList(board, [2, 4, 6, 8])

def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	
	return True

#==================函数区域结束，进入游戏主循环======================
print('''
  _______ _____ _____ _______       _____ _______ ____  ______ 
 |__   __|_   _/ ____|__   __|/\   / ____|__   __/ __ \|  ____|
    | |    | || |       | |  /  \ | |       | | | |  | | |__   
    | |    | || |       | | / /\ \| |       | | | |  | |  __|  
    | |   _| || |____   | |/ ____ \ |____   | | | |__| | |____ 
    |_|  |_____\_____|  |_/_/    \_\_____|  |_|  \____/|______|
                                                               ''')

string_1 = "Have you ever played a simple game that called the name showed above?\nNow you can play with a computer.\n\
Choose your letter and try to put them in the game board look like '#'.\nWhen three same letter in a same line, the letter's user will win.\n\
The side that go first will be chose randomly.\n\n====================GOOD LUCK HAVE FUN===================="

for i in range(len(string_1)):
	print(string_1[i], end = '')
	time.sleep(0.01)
	sys.stdout.flush()
print()

while True:
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	
	print('The ' + turn + ' will go first.')

	gameIsPlaying = True
	while gameIsPlaying:
		if turn == 'player':
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print("Hooray! U have won the game!")
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("This game is a tie.")
					break
				else:
					turn = 'computer'

		else:
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('Computer has won the game! You are sillier than a computer.')
				gameIsPlaying = False

			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("This game is a tie.")
					break
				else:
					turn = 'player'

	print('Would u want to play again?(Yes / No)')
	if not input('>>>').lower().startswith('y'):
		break
