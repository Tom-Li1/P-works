import random

guessTaken = 0
print('Hello, what is your name?')
myName = input('>>>')

print("Well, " + myName + '. I am thinking of number between 1 and 20.')

while True:
	number = random.randint(1,20)

	for i in range(6):
		print('Take a guess.')
		guess = input('>>>')
		guess = int(guess)

		if guess < number:
			print('Your guess is too low.')

		if guess > number:
			print('Your guess is too high.')

		if guess == number:
			break

	if guess == number:
		guessTaken = str(i)
		print("Good job, " + myName + '. You guessed my number in ' + guessTaken + ' guesses!')

	else:
		number = str(number)
		print("Nope, the number I was thinking of was " + number + ".")

	con = input("Play again?(y/n)\n>>>")
	if con.lower() == 'n':
		break
	
	else:
		continue