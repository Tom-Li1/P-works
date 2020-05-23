import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
	numbers = list(range(10))
	random.shuffle(numbers)
	secretNum = ''
	
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])

	return secretNum

def getClues(guess, secretNum):
	if guess == (secretNum):
		return 'You got it!'

	clues = []
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi')
		elif guess[i] in secretNum:
			clues.append('Pico')

	if len(clues) == 0:
		return 'Bagels'
		
	clues.sort()
	return ' '.join(clues)

def isOnlyDigits(num):
	if num == '':
		return False

	for i in num:
		if i not in '1 2 3 4 5 6 7 8 9 0'.split():
			return False

	return True

print("I am thinking of a %s-digits number, try to guess what it is!" % (NUM_DIGITS))
print("The clues I give are...")
print("When I say:        That means:")
print("  Bagels           None of the digits is correct.")
print("  Pico             One digit is correct but in the wrong position.")
print("  Fermi            One digit is correct and in the right position.")

while True:
	secretNum = getSecretNum()
	print("I have thought up a number. You have %s guesses to get it." % (MAX_GUESS))

	gussesTaken = 1
	while gussesTaken <= MAX_GUESS:
		guess = ''
		while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
			guess = input('Guess #%s:' % (gussesTaken))

		print(getClues(guess, secretNum))
		gussesTaken += 1

		if guess == secretNum:
			break

		if gussesTaken >= MAX_GUESS:
			print('You ran out of guesses, the answer was %s' % (secretNum))
			break

	playagain = input('Do you want to play again? (yes / no)')
	if not playagain.lower().startswith('y'):
		break