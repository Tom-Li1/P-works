import win32com.client
from time import sleep
import os
import subprocess
import tkinter as tk
def checkWanaFix():
	WMI = win32com.client.GetObject('winmgmts:')
	processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name like "%{}%"'.format('WanaFix.exe'))
	if len(processCodeCov) > 0:
		print('True')
	else:
		print('False')
		na = '"' + os.path.abspath('..') + r'\Datastore\WanaFix.exe' + '"'
		subprocess.run(na, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
	while True:
		checkWanaFix()
		sleep(1)
	
	window = tk.Tk()
	window.title('sss')
	window.geometry('100x100')
	window.mainloop()