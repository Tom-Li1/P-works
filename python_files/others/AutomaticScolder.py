import time, random, pyperclip
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class AutomaticScolder():
	def __init__(self):
		self.m = PyMouse()
		self.k = PyKeyboard()
		self.words = {
			'name':[],
			'location':["厕所里","宿舍里","房顶上","草坪上","树上","草丛里","操场上","教室里"],
			'verb':["吃","喝","玩","摸","拿","踢","举起","放下"],
			'noun':["屎","尿","鸡巴","屁眼","头","大屌","逼"]
			}

	def buildUpSentence(self):
		word_list = [] # Be used to temporary store words for one sentence.
		for v in self.words.values():
			word_list.append(random.choice(v)) # random choice a word from the words dic and append into word list.
		return "{0}在{1}{2}{3}".format(word_list[0], word_list[1], word_list[2], word_list[3]) # return the sentence be formated.

	def sendSentence(self):
		pyperclip.copy(self.buildUpSentence())
		self.k.press_key(self.k.control_key) 
		self.k.tap_key('V')
		time.sleep(0.1)
		self.k.release_key(self.k.control_key)
		time.sleep(0.1)
		self.k.tap_key(self.k.enter_key)
		
# Get name of the poor baby who will be scold.
def getName():
	print('Who are you going to scold?')
	while True:
		name = input('>>>')
		if name:
			return name

# Judge whether the string is a number.
def isDigits(digits):
	if digits == '':
		return False
	for i in digits:
		if i not in '1234567890':
			return False
	return True

# Get number of message sending.
def getScoldTime():
	print('How many message should I scold? (Must be an integer)')
	while True:
		msg_num = input('>>>')
		if msg_num == '' or isDigits(msg_num):
			return msg_num

def getIntervalTime():
	print('How long should be the interval between each message? (Must be an integer)')
	while True:
		interval_time = input('>>>')
		if isDigits(interval_time):
			return int(interval_time)

# Main part of all the project.
def main(auto_scolder):
	auto_scolder.words['name'] = [getName()]
	msg_num = getScoldTime()
	interval_time = getIntervalTime()

	print("Program will start to scoding in 5 seconds, click the chatting app's window now...")
	time.sleep(5)
	if msg_num == '':
		while True:
			auto_scolder.sendSentence()
			time.sleep(interval_time)
	else:
		for i in range(int(msg_num)):
			auto_scolder.sendSentence()
			time.sleep(interval_time)

	print('Scolding finished.\n')
	time.sleep(1)

auto_scolder = AutomaticScolder()
while True:
	main(auto_scolder)