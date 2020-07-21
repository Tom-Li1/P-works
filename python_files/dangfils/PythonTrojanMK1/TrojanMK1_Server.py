import socket
import os
import json
import traceback
import time
import uuid
import sys
import threading
# 占用资源：所在目录下创建UserData.json用于储存用户数据
# 端口使用： 5681-udp-心跳包收发

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

	def addUser(self, user_ID, t1me = ''):
		# 向内存中的数据结构添加用户 不写入文件
		try:
			if t1me == '':
				t1me = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			self.user_data[user_ID] = [t1me, 'None']
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
	global ctrl_user_ID
	global listening
	global ude

	print('[INFO] 心跳包接收线程初始化......')
	HOST_PORT = ('127.0.0.1', 5681)
	BUFSIZE = 1024
	hb_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	hb_sock.bind(HOST_PORT)
	print('[INFO] 心跳包接收线程初始化完毕 进入接收循环')

	while listening:
		data, addr = hb_sock.recvfrom(BUFSIZE)
		if data.decode('utf-8') == ctrl_user_ID:
			try:
				hb_sock.sendto('c'.encode('utf-8'), addr)
				print('[INFO] 已向ID为', ctrl_user_ID, '的用户发起控制请求')
				ctrl_user_ID = None
			except Exception as e:
				print('[ERRO] 发起控制请求失败', e)
		else:
			try:
				hb_sock.sendto('h'.encode('utf-8'), addr)
			except Exception as e:
				print('[ERRO] 回复心跳包失败', e)

		ude.addUser(user_ID = data.decode('utf-8'))
		ude.writeUserData()

	hb_sock.close()

listening = True
ctrl_user_ID = None
ude = UserDataEditor()
time.sleep(0.1)
heartBeatThread = threading.Thread(target=listen_heartbeat)
heartBeatThread.setDaemon(True)
heartBeatThread.start()
time.sleep(0.1)

'''
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
while True:
	cmd = input('>>>').split(' ')
	if len(cmd) == 1:
		if cmd[0] == 'qt':
			listening = False
			sys.exit()
		elif cmd[0] == 'lu':
			ude.showDataContent()
		elif cmd[0] == 'rd':
			ude.resetData()
		elif cmd[0] == 'ld':
			print('[INFO] 将文件内容读取至数据结构')
			ude.loadUserData()
		elif cmd[0] == 'wd':
			print('[INFO] 将用户数据结构写入文件')
			ude.writeUserData()
		elif cmd[0] == 'hp':
			print('''lu ---------------- 列出所有用户信息
ru [用户ID] ------- 移除指定ID的用户
cu [用户ID] ------- 请求控制指定ID的用户
sn [用户ID] [备注] - 为指定用户设置备注
rd ---------------- 重置用户数据库
ld ---------------- 手动读取用户数据文件
wd ---------------- 手动将用户数据写入文件
qt ---------------- 退出程序并结束所有子线程
hp ---------------- 显示说明''')
		else:
			print('[ERRO] 无效的本地操作指令')

	elif len(cmd) == 2:
		if cmd[1] not in ude.user_data:
				print('[ERRO] 此用户ID不存在')
		if cmd[0] == 'ru':
			print('[INFO] 将ID为', cmd[1], '的用户移出数据结构')
			ude.removeUser(cmd[1])
		elif cmd[0] == 'cu':
			print('[INFO] 将向ID为', cmd[1], '的用户发出控制请求')
			ctrl_user_ID = cmd[1]
		else:
			print('[ERRO] 无效的本地操作指令')

	elif len(cmd) == 3:
		if cmd[0] == 'sn':
			ude.setUserNickname(cmd[1], cmd[2])
		else:
			print('[ERRO] 无效的本地操作指令')

	else:
		print('[ERRO] 无效的本地操作指令')