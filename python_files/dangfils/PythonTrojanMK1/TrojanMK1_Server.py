import socket
import os
import json
import traceback
import time
import uuid
import sys

# 用于编辑和管理用户数据库文件的类
class UserData(): # 参数包含文件名与路径 可自定义 默认当前所在路径
	def __init__(self, file_path = os.path.dirname(__file__), file_name = r'\UserData.json'):
		print('[INFO] 服务器端用户数据库管理类初始化......')
		self.user_data = {} # {'UUID':['Time', 'Nick name'], '5d8b66df-abc31b':['2020-07-21 13:11:24', 'Peter Duan']}
		self.file_path = file_path
		self.file_name = file_name
		# 若文件不存在则新建
		if os.path.exists(self.file_path + self.file_name) == False:
			print('[ERRO] 用户数据文件不存在 即将新建文件')
			file = open(self.file_path + self.file_name, mode = 'w')
			file.close()
		print('[INFO] 数据库管理类初始化完毕')

	def loadUserData(self): # 打开文件 将储存数据的文件内容读取至内存 关闭文件
		try:
			with open(self.file_path + self.file_name, mode = 'r') as data_file:
				self.user_data = json.load(data_file)
				data_file.close()
			print('[INFO] 用户数据读取成功')
		except:
			print('[ERRO] 用户数据读取失败 反馈如下')
			traceback.print_exc()


	def addUser(self, user_ID, t1me = ''):
		# 向内存中的数据结构添加用户 不写入文件
		try:
			if t1me == '':
				t1me = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			self.user_data[user_ID] = [t1me, 'None']
			print('[INFO] 已将ID为', user_ID, '的用户添加至内存中的用户数据结构')
		except:
			print('[ERRO] 添加用户至数据结构失败 反馈如下')
			traceback.print_exc()

	def removeUser(self, user_ID): # 从内存中的数据结构移除用户 不写入文件
		try:
			if user_ID not in self.user_data:
				print('[ERRO] 删除用户失败 数据结构中无此ID的用户')
			else:
				del self.user_data[user_ID]
				print('[INFO] 已将ID为', user_ID, '的用户移出数据结构')
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
			print('[INFO] 用户数据结构已写入文件')
		except:
			print('[ERRO] 写入用户数据至文件失败 反馈如下')
			traceback.print_exc()

	def showDataContent(self): # 格式化输出内存中用户数据结构的内容至命令行 不读取文件
		print('{:=^74}'.format('用户信息表单'))
		if self.user_data == {}:
			print('\n{:^65}\n'.format('数据结构中未储存任何用户信息'))
		else:
			print('{0:^40}{1:^25}{2:^15}'.format("User's UUID", 'Last Online Time', 'Nickname'))
			for uuid, data in self.user_data.items():
				print('{0:^40}{1:^25}{2:^15}'.format(uuid, data[0], data[1]))
		print('{:=^80}'.format(''))

	def setUserNickname(self, user_ID, nickname):
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

while True:
	exec(input('>>>'))