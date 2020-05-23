import random
import time
import sys

HANGMAN_PICS = ['''     
      +---+     
          |     
          |     
          |     
         ===''', '''        
      +---+     
      O   |     
          |     
          |     
         ===''', '''        
      +---+     
      O   |     
      |   |     
          |     
         ===''', '''        
      +---+     
      O   |     
     /|   |     
          |     
         ===''', '''        
      +---+     
      O   |     
     /|\  |     
          |     
         ===''', '''        
      +---+     
      O   |     
     /|\  |     
     /    |     
         ===''', '''        
      +---+     
      O   |     
     /|\  |     
     / \  |     
         ===''','''
      +---+     
     [O   |     
     /|\  |     
     / \  |     
         ===''','''
      +---+     
     [O]  |     
     /|\  |     
     / \  |     
         ===''']

words = {
	'形容词':'big small good bad happy beautiful'.split(),
	'名词':'cat dog'.split(),
	'动词':'eat run walk smellm look hear say'.split()
}

def getRandomWord(wordDict):
	wordKey = random.choice(list(wordDict.keys()))
	wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

	return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()

	print("错误字母:", end = ' ')
	for letter in missedLetters:
		print(letter, end = ' ')
	print()

	blanks = '_' * len(secretWord)

	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	for letter in blanks:
		print(letter, end=' ')

	print()

def getGuess(alreadyGuessed):
	while True:
		print('请猜')
		guess = input('>>>')
		guess = guess.lower()
		if len(guess) != 1:
			print('那个字母你早就猜过')
		elif guess in alreadyGuessed:
			print('')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('你确定这是字母？')
		else:
			return guess

def playAgain():
	print("还玩？(键入 yes/no)")
	return input(">>>").lower().startswith('y')

string_0 = '''
  o         o           o           o          o        o__ __o       o          o           o           o          o  
 <|>       <|>         <|>         <|\        <|>      /v     v\     <|\        /|>         <|>         <|\        <|> 
 < >       < >         / \         / \\o       / \     />       <\    / \\o    o/ / \         / \         / \\ o      / \ 
  |         |        o/   \o       \o/ v\     \o/   o/               \o/ v\  /v \o/       o/   \o       \o/ v\     \o/ 
  o__/_ _\__o       <|__ __|>       |   <\     |   <|       _\__o__   |   <\/>   |       <|__ __|>       |   <\     |  
  |         |       /       \      / \    \o  / \   \\           |    / \        / \      /       \      / \    \o  / \ 
 <o>       <o>    o/         \o    \o/     v\ \o/     \         /    \o/        \o/    o/         \o    \o/     v\ \o/ 
  |         |    /v           v\    |       <\ |       o       o      |          |    /v           v\    |       <\ |  
 / \       / \  />             <\  / \        < \      <\__ __/>     / \        / \  />             <\  / \        < \ 
'''

string_1 = '''简单电子游戏这是. 人将被吊起来.\n\
你应该干的是猜测一个随机英文单词的拼写. 每次猜测一个字母.\n\
如果字母在这个单词, 不发生什么. 你继续猜剩下的.\n\
如果不在, 人的身体的一部分将会被吊起. 当人之全体被吊, 它死你输了.\n\
当人全被挂起之前，你猜出了所有单词里的字母，你赢了就.\n----------好----------'''

print(string_0)

for i in range(len(string_1)):
	print(string_1[i], end = '')
	time.sleep(0.01)
	sys.stdout.flush()
print()
input("按一次回车键如果你是准备好的。")

difficulty = ' '
while difficulty not in 'EMH':
	difficulty = input("输入一个难度(每局猜测次数): E - 简单, M - 中等, H - 挺难\n>>>").upper()
	if difficulty == 'M':
		del HANGMAN_PICS[8]
		del HANGMAN_PICS[7]

	if difficulty == 'H':
		del HANGMAN_PICS[8]
		del HANGMAN_PICS[7]
		del HANGMAN_PICS[5]
		del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
	print('被选中的单词是一个：', secretSet)
	displayBoard(missedLetters, correctLetters, secretWord)
	guess = getGuess(missedLetters + correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters == True:
			print("对，这个单词就是 '" + secretWord + "'! 你胜。")
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess
		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('猜测机会被你用完!\n经过 ' + 
				str(len(missedLetters)) + ' 次错误猜测和 ' +
				str(len(correctLetters)) + ' 次正确猜测.\n实际上是 ' +
				 "'" + secretWord + "'.")
			gameIsDone = True

	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord, secretSet = getRandomWord(words)
		else:
			break