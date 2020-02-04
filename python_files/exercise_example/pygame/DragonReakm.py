import random
import time

def desplayIntro():
	print('''Do you think you are an asshole?''')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		cave = input("1=yes  2=no（1 或 2）")
	return cave

def checkCave(chosenCave):
	print("I think you are......")
	time.sleep(2)
	print("As far as I know......")
	time.sleep(2)
	print("You are certainly a......")
	print()
	time.sleep(2)

	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print("Asshole!")

	else:
		print("In fact, you are very good")
		time.sleep(2)
		print("but...")
		time.sleep(2)
		print("You are an asshole!")
		time.sleep(2)

playAgain = 'yes'
while playAgain == 'yes' or  playAgain == 'y':
	desplayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print("Do you believe my words? (y or n)")
	time.sleep(2)
	print("No matter you believe them or not...")
	time.sleep(2)
	print("You are an asshole, fuck you!")
	playAgain = input('>>>')