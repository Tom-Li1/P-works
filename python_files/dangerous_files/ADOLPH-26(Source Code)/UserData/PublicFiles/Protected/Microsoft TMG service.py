import win32com.client
from time import sleep
import os
import tkinter as tk
from sys import exit
running = True

def checkTaskmgr():
	global running
	WMI = win32com.client.GetObject('winmgmts:')
	processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name like "%{}%"'.format('Taskmgr.exe'))
	if len(processCodeCov) > 0:
		print('True')
		f = open(os.path.abspath('..') + r'\UserSettings\KsysN.txt', 'w')
		f.close
		running = False
	else:
		print('False')
	sleep(1)

if __name__ == '__main__':
	while running:
		checkTaskmgr()
		sleep(1)
	if running == False:
		exit()
	while True:
		sleep(1)
	window = tk.Tk()
	window.title('sss')
	window.geometry('100x100')
	window.mainloop()