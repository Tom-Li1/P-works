import socket
import os
import json
import traceback
import time
import uuid
import sys
import threading
# 占用资源：所在目录下创建UUID.json用于储存此用户的ID码
# 端口使用：5681-udp-心跳包收发

def isUuidOK(file_name, file_path): # 判断UUID储存文件是否存在且完整 返回True或False
	if os.path.exists(file_path + file_name) == False:
		print('[ERRO] UUID储存文件不存在')
		return False
	else:
		try:
			with open(file_path + file_name, mode = 'r') as uuid_file:
				content = json.load(uuid_file)
				uuid_file.close()
				if 'uuid' not in content or 'complete' not in content or content['complete'] != '0x00012c':
					print('[ERRO] UUID储存文件不完整')
					return False
				else:
					print('[INFO] UUID文件存在并完整')
					return True
		except:
			print('[ERRO] 验证文件可用性时出错')
			traceback.print_exc()
			return False

def UUID(): # 用于操作储存UUID文件的函数 内部调用isUuidOK()
	file_path = os.path.dirname(__file__)
	file_name = r'\UUID.json'

	if isUuidOK(file_name, file_path) == False:
		print('[INFO] 正在重设UUID储存文件......')
		with open(file_path + file_name, mode = 'w') as uuid_file:
			json.dump({'uuid':str(uuid.uuid4()), 'complete':'0x00012c'}, uuid_file)
			uuid_file.close()
		print('[INFO] UUID文件重设完成')

	with open(file_path + file_name, mode = 'r') as uuid_file:
			content = json.load(uuid_file)
			uuid_file.close()
			print('[INFO] UUID文件读取完成')
			return content['uuid']

class HeartBeatController(): # 用于接收/回复/辨别来自服务端心跳包的类
	def __init__(self, user_ID):
		print('[INFO] 心跳包收发类初始化......')
		self.user_ID = user_ID
		self.HOST_PORT = ('127.0.0.1', 5681)
		self.BUFSIZE = 1024
		self.hb_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.hb_sock.settimeout(10)
		print('[INFO] 心跳包收发类初始化完成')

	def sendHb(self):
		try:
			self.hb_sock.sendto(self.user_ID.encode("utf-8"), self.HOST_PORT)
			print('[INFO] 心跳包发送')
		except:
			print('[ERRO] 心跳包发送失败 反馈如下')
			traceback.print_exc()

	def recvHb(self):
		try:
			serv_msg, _ = self.hb_sock.recvfrom(self.BUFSIZE)
			print('[INFO] 心跳包接收')
			if serv_msg.decode('utf-8') == "c":
				print('[INFO] 收到服务器接受请求')
				return True
			else:
				return False
		except ConnectionResetError:
			print('[ERRO] 心跳包发送失败 服务器已关闭')

		except  as e:
			print('[ERRO] 心跳包发送失败', e)


	def shutDown(self):
		self.hb_sock.close()
		print('[INFO] 心跳包发送套接字已关闭')

hbc = HeartBeatController(UUID())
while True:
	hbc.sendHb()
	if hbc.recvHb() == True:
		print('[INFO] 已转入控制模式')
		while True:
			if input('>>>') == 'q':
				print('[INFO] 已退出控制模式')
				break
	time.sleep(6)