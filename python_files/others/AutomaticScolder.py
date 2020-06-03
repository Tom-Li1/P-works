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
		word_list = []
		for words_key in self.words.keys():	
			word_list.append(random.choice(self.words[words_key]))
		return "{0}在{1}{2}{3}".format(word_list[0], word_list[1], word_list[2], word_list[3])

	def sendSentence(self):
		pyperclip.copy(self.buildUpSentence())
		self.k.press_key(self.k.control_key) 
		self.k.tap_key('V')
		self.k.release_key(self.k.control_key)
		self.k.tap_key(self.k.enter_key)

auto_scolder = AutomaticScolder()

print('Who are you going to scold?')
while True:
	name = input('>>>')
	if name:
		auto_scolder.words['name'].append(name)
		break
		
print("Program scolding, click chat app's window to start...")
while True:
	auto_scolder.sendSentence()
	time.sleep(1)