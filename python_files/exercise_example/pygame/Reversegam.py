# Reversegam: A clone of Othello/Reversegam

import random
import sys

WIDTH = 8
HEIGHT = 8

def drawBoard(board):
	print('  12345678')
	print(' +--------+')
	for y in range(HEIGHT):
		print('%s|' % (y + 1), end = '')
		for x in range(WIDTH):
			print(board[x][y], end = '')
		print('|%s' % (y + 1))
	print(' +--------+')
	print('  12345678')

def getNewBoard():
	board = []
	for i in range(WIDTH):
		board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
	return board

def isValidMove(board, tile, xstart, ystart):
	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False

	if tile == 'X':
		otherTile = 'O'
	else:
		otherTile = 'X'

	tilesToFlip = []
	for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		x, y = xstart, ystart
		x += xdirection
		y += ydirection
		while isOnBoard(x, y) and board[x][y] == otherTile:
			x += xdirection
			y += ydirection
			if isOnBoard(x, y) and board[x][y] == tile:
				while True:
					x -= xdirection
					y -= ydirection
					if x == xstart and y == ystart:
						break
					tilesToFlip.append([x, y])

	if len(tilesToFlip) == 0:
		return False

	return tilesToFlip

def isOnBoard(x, y):
	return x >= 0 and x <= WIDTH -1 and y >= 0 and y <= HEIGHT -1

def getBoardWithValidMoves(board, tile):
	boardCopy = getBoardCopy(board)
	for x, y in getValidMoves(boardCopy, tile):
		boardCopy[x][y] = '.'
	return boardCopy

def getValidMoves(board, tile):
	validMoves = []
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if isValidMove(board, tile, x, y) != False:
				validMoves.append([x, y])
	return validMoves

def getScoreOfBoard(board):
	xscore = 0
	oscore = 0
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if board[x][y] == 'X':
				xscore += 1
			if board[x][y] == 'O':
				oscore += 1

	return {'X':xscore,'O':oscore}

def enterPlayerTile():
	tile = ''
	while not (tile == 'X' or tile == 'O'):
		print('你希望使用 X 还是 O 作为你的棋子？')
		tile = input('>>>').upper()

	if tile == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def makeMove(board, tile, xstart, ystart):
	tilesToFlip = isValidMove(board, tile, xstart, ystart)

	if tilesToFlip == False:
		return False

	board[xstart][ystart] = tile
	for x, y in tilesToFlip:
		board[x][y] = tile

	return True

def getBoardCopy(board):
	boardCopy = getNewBoard()

	for x in range(WIDTH):
		for y in range(HEIGHT):
			boardCopy[x][y] = board[x][y]

	return boardCopy

def isOnCorner(x, y):
	return (x == 0 or x == WIDTH -1) and (y == 0 or y == HEIGHT -1)

def getPlayerMove(board, playerTile):
	DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split(' ')
	while True:
		print('输入你要放置棋子的位置，输入"quit"退出或输入"hints"来显示可以下棋的位置')
		move = input('>>>').lower()
		if move == 'hints' or move == 'quit':
			return move

		if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
			x = int(move[0]) - 1
			y = int(move[1]) - 1
			if isValidMove(board, playerTile, x, y) == False:
				continue
			else:
				break

		else:
			print('此位置不能下棋，输入横坐标（1-8）和纵坐标（1-8）')
			print('比如输入“81”将会在右上角下棋')

	return [x, y]

def getComputerMove(board, computerTile):
	possibleMoves = getValidMoves(board, computerTile)
	random.shuffle(possibleMoves)

	for x, y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]

	bestScore = -1
	for x, y in possibleMoves:
		boardCopy = getBoardCopy(board)
		makeMove(boardCopy, computerTile, x, y)
		score = getScoreOfBoard(boardCopy)[computerTile]
		if score > bestScore:
			bestMove = [x, y]
			bestScore = score

	return bestMove

def printScore(board, playerTile, computerTile):
	scores = getScoreOfBoard(board)
	print('你： %s 分。 AI: %s 分。' % (scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):
	showHints = False
	turn = whoGoesFirst()
	print('本局%s先走第一步。' % (turn))
	board = getNewBoard()

	board[3][3] = 'X'
	board[4][4] = 'X'
	board[3][4] = 'O'
	board[4][3] = 'O'

	while True:
		playerValidMoves = getValidMoves(board, playerTile)
		computerValidMoves = getValidMoves(board, computerTile)

		if playerValidMoves == [] and computerValidMoves == []:
			return board

		elif turn == 'player':
			if playerValidMoves != []:
				if showHints:
					validMovesBoard = getBoardWithValidMoves(board, playerTile)
					drawBoard(validMovesBoard)
				else:
					drawBoard(board)
				printScore(board, playerTile, computerTile)

				move = getPlayerMove(board, playerTile)
				if move == 'quit':
					print('感谢游玩。')
					sys.exit()
				elif move == 'hints':
					showHints = not showHints
					continue
				else:
					makeMove(board, playerTile, move[0], move[1])
			turn = 'computer'

		elif turn == 'computer':
			if computerValidMoves != []:
				drawBoard(board)
				printScore(board, playerTile, computerTile)

				input('按下回车键使AI下棋。')
				move = getComputerMove(board, computerTile)
				makeMove(board, computerTile, move[0], move[1])
			turn = 'player'

print('Reversegam! v0.0.1 游侠汉化组汉化')

playerTile, computerTile = enterPlayerTile()
while True:
	finalBoard = playGame(playerTile, computerTile)
	drawBoard(finalBoard)
	scores = getScoreOfBoard(finalBoard)
	print('X得分%s分，O得分%s分。' % (scores['X'], scores['O']))
	if scores[playerTile] > scores[computerTile]:
		print('你以%s分的战绩战胜了AI，牛逼者！' % (scores[playerTile] - scores[computerTile]))

	elif scores[playerTile] < scores[computerTile]:
		print('AI以%s的战绩打败了你......' % (scores[computerTile] - scores[playerTile]))

	else:
		print('好像平局了。')

	print('再来一局么？(yes/no)')
	if not input('>>>').lower().startswith('y'):
		print('感谢游玩。')
		break
