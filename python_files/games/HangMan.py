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
	'.adj':'big small good bad happy beautiful'.split(),
	'.n':'cat dog'.split(),
	'.v':'eat run walk smellm look hear say'.split()
}

def getRandomWord(wordDict):
	wordKey = random.choice(list(wordDict.keys()))
	wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

	return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()

	print("Missed letters:", end = ' ')
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
		print('Guess a letter, please.')
		guess = input('>>>')
		guess = guess.lower()
		if len(guess) != 1:
			print('You only can enter ONE letter each time.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter, choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess

def playAgain():
	print("Do you want to play again?(yes or no)")
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

string_1 = '''This is a simple computer game. You are a person who will be hanged on the gallows.\n\
All you have to do is guess a random English word. You can only guess one letter at a time.\n\
If the letters are in this word, nothing will happen. You continue to guess the rest of the words.\n\
On the contrary, a part of your body will be hung on the gallows. When your whole body is hung, you die.\n\
When you guess all the letters correctly before you are hung, you win.\n----------GOOD LUCK HAVE FUN----------'''

print(string_0)

for i in range(len(string_1)):
	print(string_1[i], end = '')
	time.sleep(0.01)
	sys.stdout.flush()
print()
input("Press 'enter' if you are ready.")

difficulty = ' '
while difficulty not in 'EMH':
	difficulty = input("Enter difficulty: E - Eazy, M - Medium, H - Hard\n>>>").upper()
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
	print('The secret word is in the set:', secretSet)
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
			print("Yes, the secret word is '" + secretWord + "'! You have won!")
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess
		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\nAfter ' + 
				str(len(missedLetters)) + ' missed guesses and ' +
				str(len(correctLetters)) + ' correct guesses.\nThe word was ' +
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