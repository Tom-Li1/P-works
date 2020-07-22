import socket
import os
import json
import traceback
import time
import uuid
import sys
import threading
# 占用资源：所在目录下创建UUID.json用于储存此用户的ID码
# 端口使用：5681-UDP-心跳包收发 5682-TCP-远程控制通讯 5683-TCP-文件传输
# 命名规则：函数-xxxXxx 类-XxxXxx 局部变量-xxx_xxx 全局变量-XXXXXX

def isUuidOK(file_name, file_path): # 判断UUID储存文件是否存在且完整 返回True或False
	if os.path.exists(file_path + file_name) == False: # 先用exists()核实文件是否存在
		print('[ERRO] UUID储存文件不存在')
		return False
	else:
		try:
			with open(file_path + file_name, mode = 'r') as uuid_file:
				content = json.load(uuid_file)
				uuid_file.close()
				if 'uuid' not in content or 'complete' not in content or content['complete'] != '0x00012c':
					print('[ERRO] UUID储存文件不完整') # 内容缺一不可
					return False
				else:
					print('[INFO] UUID文件存在并完整')
					return True
		except:
			print('[ERRO] 验证文件可用性时出错')
			traceback.print_exc()
			return False

def UUID(): # 用于操作储存UUID文件的函数 内部调用isUuidOK()
	file_path = os.path.dirname(__file__) # 默认存储目录为此文件所在目录
	file_name = r'\UUID.json'

	if isUuidOK(file_name, file_path) == False:
		print('[INFO] 正在重设UUID储存文件......') # UUID文件不存则或不完整则新建/覆盖 同时获取新的UUID
		with open(file_path + file_name, mode = 'w') as uuid_file:
			json.dump({'uuid':str(uuid.uuid4()), 'complete':'0x00012c'}, uuid_file)
			uuid_file.close()
		print('[INFO] UUID文件重设完成')

	with open(file_path + file_name, mode = 'r') as uuid_file: # 打开UUID文件并读取 用于向服务器提供身份
			content = json.load(uuid_file)
			uuid_file.close()
			print('[INFO] UUID文件读取完成')
			return content['uuid']

class HeartBeatController(): # 用于接收/回复/辨别来自服务端心跳包的类
	def __init__(self, user_ID):
		print('[INFO] 心跳包收发类初始化......')
		self.user_ID = user_ID
		self.host_port = ('127.0.0.1', 5681)
		self.bufsize = 1024
		self.hb_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.hb_sock.settimeout(10)
		print('[INFO] 心跳包收发类初始化完成')

	def sendHb(self, ctrl_reply = False): # 发送心跳包 指定默认值的参数若为True则发送接入控制许可
		try:
			if ctrl_reply == False:
				self.hb_sock.sendto(self.user_ID.encode("utf-8"), self.host_port)
				print('[INFO] 已向服务器发送心跳包')
			else:
				self.hb_sock.sendto((self.user_ID + 'R').encode("utf-8"), self.host_port) # 在UUID末尾加 R 便是许可
		except Exception as e:
			print('[ERRO] 心跳包发送失败', e)


	def recvHb(self): # 接收并分析心跳包返回布尔值 收到 c 代表服务器的接入请求 其他为来自服务器的普通响应
		try:
			serv_msg, _ = self.hb_sock.recvfrom(self.bufsize)
			print('[INFO] 收到服务器响应')
			if serv_msg.decode('utf-8') == "c":
				print('[INFO] 收到服务器控制请求')
				return True
			else:
				return False
		except Exception as e:
			print('[ERRO] 服务器未响应', e)
			return False


	def shutDown(self): # 关闭心跳包收发套接字
		self.hb_sock.close()
		print('[INFO] 心跳包发送套接字已关闭')

def remoteCtrl(HeartBeatController): # 与服务器建立TCP链接 接收处理命令 发送返回值 唯一参数用于完全退出此程序
	global HBC

	rc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	rc_sock.settimeout(5) # 五秒内无法链接服务器则关闭套接字
	try:
		rc_sock.connect(('127.0.0.1', 5682))
		rc_sock.sendall((socket.gethostname() + ' Ready.').encode('utf-8')) # 发送招呼信息代表一切就绪
		print('[INFO] 进入远控命令收发循环')
		rc_sock.settimeout(300)
		while True:
			sevr_data = rc_sock.recv(10240).decode('utf-8')
			print('[RECV]', sevr_data)
			if sevr_data == 'q':
				rc_sock.close() # 收到 q 为手动关闭链接
				print('[INFO] TCP远控连接已关闭')
				return None
			rc_sock.sendall((sevr_data + ' reply').encode('utf-8'))
	except:
		print('[ERRO] 远控TCP链接发生异常 已关闭')
		traceback.print_exc()
		rc_sock.close()


HBC = HeartBeatController(UUID())
while True:
	HBC.sendHb()
	if HBC.recvHb() == True:
		time.sleep(0.5)
		HBC.sendHb(ctrl_reply = True)
		print('[INFO] 已应答服务器的控制请求')
		time.sleep(0.5)
		remoteCtrl(HBC)
	time.sleep(5)