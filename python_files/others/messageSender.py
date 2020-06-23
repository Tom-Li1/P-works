import time
import random
import pyperclip
import argparse 
import sys
import os
from progressbar import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# define a main class to structure data and functions
class MessageSender():
	def __init__(self, document_path, sending_rate):
		self.sending_rate = sending_rate
		self.kbr = PyKeyboard()
		self.mus = PyMouse()
		self.sentences, self.lenth = self.prepSentence(document_path)

	def prepSentence(self, path):
		# read a TXT file and store every lines in a list
		sentences = []
		for line in open(path, encoding = 'UTF-8'):
			sentences.append(line)
		return (sentences, len(sentences))

	def sendMessage(self, index):
		# 'copy' a sentence to clipboard
		pyperclip.copy(self.sentences[index])

		# press 'control + v' then press 'enter' to send
		self.kbr.press_key(self.kbr.control_key)
		time.sleep(0.1)
		self.kbr.tap_key('V')
		self.kbr.release_key(self.kbr.control_key)
		self.kbr.tap_key(self.kbr.enter_key)

		# sleep random seconds(depend on the --time argument) before send next sentence
		time.sleep(random.randint(int(self.sending_rate[0]), int(self.sending_rate[1])))

# collect errors and give reasons for idiots
def argsTroubleShooting(args):
	error = 0

	# deal with the file path
	if args['file'] == None:
		print('[File ERROR] The argument -f/--file is required.')
		error = 1
	elif os.path.exists(args['file']) == False:
		print('[File ERROR] The file specified does not exist.')
		error = 1
	elif os.path.splitext(args['file'])[1] != '.txt':
		print('[File ERROR] Only TXT files are supported.')
		error = 1

	# this is about interval time
	if '-' not in args['time']:
		print('[Time ERROR] Time argument form should be: "positive integet - pisitive integet". Such as 1-3, 2-5, 5-6.')
		error = 1

	elif len(args['time'].split('-')) != 2:
		print('[Time Error] Invalid form of time argument you provided.')

	if error == 1:
		print("Try --help or -h for more help")
		sys.exit()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(
	description = 'This program is used to automatically send messages to others in chat apps.\n\
	Make sure a message will be sent when press enter key',
	epilog = 'If you still have no idea what just happened, try the following page:\n\nhttps://www.pornhub.com')
ap.add_argument('-f', '--file',
	type = str,
	default = None,
	help = "A TXT file's path, the file should include all sentences u r going to send.",)
ap.add_argument('-t', '--time',
	type = str,
	default = '1-1',
	help = 'The interval time of sending a message. This arg should be looks like 3-4 or 2-8.\n\
	Such 2-8, it means random pause 2 to 8 seconds. Default value is 1-1.')
args = vars(ap.parse_args())
argsTroubleShooting(args)

# The main part
def main():
	# create and initialize message-sender and progress-bar object
	msg_sder = MessageSender(document_path = args['file'], sending_rate = args['time'].split('-'))
	pro_bar = ProgressBar()

	# give user 5 seconds to get ready for start
	for i in list(range(5))[::-1]:
		print('\r[INFO] The program will start in %s seconds...' % (str(i+1)), end = '', flush = True)
		time.sleep(1)

	# go through the message list and send one each time, quit when finished
	for i in pro_bar(range(msg_sder.lenth)):
		msg_sder.sendMessage(i)
	sys.exit()

if __name__ == '__main__':
	main()