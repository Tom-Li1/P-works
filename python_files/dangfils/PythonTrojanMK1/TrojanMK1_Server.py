import socket
import os
import json
import traceback
import time
import uuid
import sys
import threading
# 占用资源：所在目录下创建UserData.json用于储存用户数据
# 端口使用：5681-UDP-心跳包收发 5682-TCP-远程控制通讯 5683-TCP-文件传输
# 命名规则：函数-xxxXxx 类-XxxXxx 局部变量-xxx_xxx 全局变量-XXXXXX
''' 本地指令
lu ---------------- 列出所有用户信息
ru [用户ID] ------- 移除指定ID的用户
cu [用户ID] ------- 请求控制指定ID的用户
sn [用户ID] [备注] - 为指定用户设置备注
rd ---------------- 重置用户数据库
ld ---------------- 手动读取用户数据文件
wd ---------------- 手动将用户数据写入文件
qt ---------------- 退出程序并结束所有子线程
hp ---------------- 显示说明
''' 

# 用于编辑和管理用户数据库文件的类
class UserDataEditor(): # 参数包含文件名与路径 可自定义 默认当前所在路径
	def __init__(self, file_path = os.path.dirname(__file__), file_name = r'\UserData.json'):
		print('[INFO] 服务器端用户数据库管理类初始化......')
		self.user_data = {} # {'UUID':['Time', 'Nick name'], '5d8b66df-abc31b':['2020-07-21 13:11:24', 'Peter Duan']}
		self.file_path = file_path
		self.file_name = file_name
		# 若文件不存在则新建
		if os.path.exists(self.file_path + self.file_name) == False:
			print('[ERRO] 用户数据文件不存在 即将新建文件')
			file = open(self.file_path + self.file_name, mode = 'w')
			json.dump({}, file)
			file.close()
		self.loadUserData()
		print('[INFO] 数据库管理类初始化完毕')

	def loadUserData(self): # 打开文件 将储存数据的文件内容读取至内存 关闭文件
		try:
			with open(self.file_path + self.file_name, mode = 'r') as data_file:
				self.user_data = json.load(data_file)
				data_file.close()
			print('[INFO] 用户数据读取成功')
		except Exception as e:
			print('[ERRO] 用户数据读取失败', e)

	def addUser(self, user_ID):
		# 向内存中的数据结构添加用户 不写入文件
		try:
			t1me = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			if user_ID not in self.user_data:
				self.user_data[user_ID] = [t1me, 'None']
			else:
				self.user_data[user_ID][0] = t1me
		except:
			print('[ERRO] 添加用户至数据结构失败 反馈如下')
			traceback.print_exc()

	def removeUser(self, user_ID): # 从内存中的数据结构移除用户 不写入文件
		try:
			if user_ID not in self.user_data:
				print('[ERRO] 删除用户失败 数据结构中无此ID的用户')
			else:
				del self.user_data[user_ID]
		except:
			print('[ERRO] 移除用户失败 反馈如下')
			traceback.print_exc()

	def resetData(self): # 打开文件 清空用户数据 关闭文件
		try:
			with open(self.file_path + self.file_name, 'w') as data_file:
				json.dump({}, data_file)
				data_file.close()
				self.user_data = {}
			print('[INFO] 用户数据库文件与内存数据结构已清空')
		except:
			print('[ERRO] 清空用户数据失败 反馈如下')
			traceback.print_exc()

	def writeUserData(self): # 打开文件 将当前内存中的数据结构写入文件 关闭文件
		try:
			with open(self.file_path + self.file_name, 'w') as data_file:
				json.dump(self.user_data, data_file)
				data_file.close()
		except:
			print('[ERRO] 写入用户数据至文件失败 反馈如下')
			traceback.print_exc()

	def showDataContent(self): # 格式化输出内存中用户数据结构的内容至命令行 不读取文件
		print('{:=^84}'.format('用户信息表单'))
		if self.user_data == {}:
			print('\n{:^75}\n'.format('数据结构中未储存任何用户信息'))
		else:
			print('{0:^40}{1:^25}{2:^10}{3:^15}'.format("User's UUID", 'Last Online Time', 'State', 'Nickname'))
			for uuid, data in self.user_data.items():
				if data[0][14:16] == time.strftime('%M',time.localtime(time.time())):
					state = 'ACTIVE'
				else:
					state = 'INACTIVE'
				print('{0:^40}{1:^25}{2:^10}{3:^15}'.format(uuid, data[0], state, data[1]))
		print('{:=^90}'.format(''))

	def setUserNickname(self, user_ID, nickname): # 为用户指定备注
		try:
			if user_ID not in self.user_data:
				print('[ERRO] 设置备注失败 数据结构中无此ID的用户')
			elif len(nickname) > 15 or len(nickname) == 0:
				print('[ERRO] 设置备注失败 用户备注需要1-15个字符')
			else:
				self.user_data[user_ID][1] = nickname
				print('[INFO] 已将ID为', user_ID, '的用户备注设置为', nickname)
		except:
			print('[ERRO] 设置备注失败 反馈如下')
			traceback.print_exc()

def listen_heartbeat(): # 子线程 心跳包接收以及接入控制用户函数
	global CTRL_USER_ID # 临时存储请求控制用户的ID
	global UDE # UserDataEditor对象
	global LISTENING # 控制心跳包收发线程开关的布尔值变量

	print('[INFO] 心跳包接收线程初始化......')
	host_port = ('127.0.0.1', 5681)
	bufsize = 1024
	hb_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	hb_sock.bind(host_port)
	hb_sock.settimeout(3)
	print('[INFO] 心跳包接收线程初始化完毕 进入接收循环')

	while LISTENING:
		try:
			data, addr = hb_sock.recvfrom(bufsize)
		except:
			continue
		if data.decode('utf-8') == CTRL_USER_ID:
			try:
				hb_sock.sendto('c'.encode('utf-8'), addr)
				print('[INFO] 已向ID为', CTRL_USER_ID, '的用户发起控制请求')
				CTRL_USER_ID = None
			except Exception as e:
				print('[ERRO] 发起控制请求失败', e)
		elif data.decode('utf-8')[-1] == 'R':
			print('[INFO] 收到ID为', data.decode('utf-8')[:-1], '的控制请求许可')
		else:
			try:
				hb_sock.sendto('h'.encode('utf-8'), addr)
			except Exception as e:
				print('[ERRO] 回复心跳包失败', e)

		UDE.addUser(user_ID = data.decode('utf-8'))
		UDE.writeUserData()

	hb_sock.close()
	print('[INFO] 心跳包收发线程已结束')

def printHelp():
	local_help = {
	'lu ':' 列出所有用户信息',
	'ru [UserID] ':' 移除指定ID的用户',
	'cu [UserID] ':' 请求控制指定ID的用户',
	'sn [UserID] [Nickname] ':' 为指定用户设置备注',
	'rd ':' 重置用户数据库',
	'ld ':' 手动读取用户数据文件',
	'wd ':' 手动将用户数据写入文件',
	'qt ':' 退出程序并结束所有子线程',
	'hp ':' 显示说明'
	}

	remote_help = {
	'吃屎':'你可以吃掉一个屎',
	'喝尿':'你可以喝掉一个尿'
	}

	print('{:=^60}'.format('本地'))
	for k, v in local_help.items():
		print('{0:-<30}{1:<30}'.format(k, v))

	print('{:=^60}'.format('远控'))
	for k, v in remote_help.items():
		print('{0:-<30}{1:<30}'.format(k, v))
	print('{:=^62}'.format(''))

	del local_help
	del remote_help

def remoteCtrl():
	host_port = ('127.0.0.1', 5682)
	rc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	rc_sock.settimeout(5)
	rc_sock.bind(host_port)
	rc_sock.listen(1)
	try:
		user, _ = rc_sock.accept()
		print(user.recv(1024).decode('utf-8'))
		while True:
			serv_msg = input('User> ')
			if serv_msg == 'q':
				user.sendall('q')
				rc_sock.close()
				break
			user.send(serv_msg.encode('utf-8'))
			user_msg = user.recv(20480).decode('utf-8')
			print(user_msg)
	except Exception as e:
		print('[ERRO] 链接发生异常', repr(e))
		rc_sock.close()

def localCommand(cmd):
	global CTRL_USER_ID
	global LISTENING
	global UDE

	cmd_list = cmd.split(' ')
	if len(cmd_list) == 1:
		if cmd_list[0] == 'qt':
			LISTENING = False
			print("[INFO] 正在结束所有子线程并退出")
			sys.exit()
		elif cmd_list[0] == 'lu':
			UDE.showDataContent()
		elif cmd_list[0] == 'rd':
			UDE.resetData()
		elif cmd_list[0] == 'ld':
			print('[INFO] 将文件内容读取至数据结构')
			UDE.loadUserData()
		elif cmd_list[0] == 'wd':
			print('[INFO] 将用户数据结构写入文件')
			UDE.writeUserData()
		elif cmd_list[0] == 'hp':
			printHelp()
		else:
			print('[ERRO] 无效的本地操作指令')

	elif len(cmd_list) == 2:
		if cmd_list[1] not in UDE.user_data:
				print('[ERRO] 此用户ID不存在')
		elif cmd_list[0] == 'ru':
			print('[INFO] 将ID为', cmd_list[1], '的用户移出数据结构')
			UDE.removeUser(cmd_list[1])
		elif cmd_list[0] == 'cu':
			print('[INFO] 将向ID为', cmd_list[1], '的用户发出控制请求')
			CTRL_USER_ID = cmd_list[1]
			remoteCtrl()
		else:
			print('[ERRO] 无效的本地操作指令')

	elif len(cmd_list) == 3:
		if cmd_list[0] == 'sn':
			UDE.setUserNickname(cmd_list[1], cmd_list[2])
		else:
			print('[ERRO] 无效的本地操作指令')

	else:
		print('[ERRO] 无效的本地操作指令')


# 创建本地用户信息编辑类对象
UDE = UserDataEditor()
time.sleep(0.1)
# 设定必要变量并创建心跳包收发子线程
LISTENING = True
CTRL_USER_ID = None
heartBeatThread = threading.Thread(target=listen_heartbeat)
heartBeatThread.setDaemon(False)
heartBeatThread.start()
time.sleep(0.1)

while True:
	cmd = input('Local> ')
	localCommand(cmd)