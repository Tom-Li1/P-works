import socket
import os
import json
import traceback
import time
import uuid
import sys
import threading
import shutil
# 占用资源：所在目录下创建UUID.json用于储存此用户的ID码
# 端口使用：5681-UDP-心跳包收发 5682-TCP-远程控制通讯 5683-TCP-文件传输
# 命名规则：函数-xxxXxx 类-XxxXxx 局部变量-xxx_xxx 全局变量-XXXXXX

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
			print('[ERROR] 心跳包发送失败', e)

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
			print('[WARNING] 接收心跳包反馈时', e)
			return False
		except socket.timeout:
			print('[WARNING] 服务器未及时响应心跳包')


	def shutDown(self): # 关闭心跳包收发套接字
		self.hb_sock.close()
		print('[INFO] 心跳包发送套接字已关闭')

def isUuidOK(file_name, file_path): # 判断UUID储存文件是否存在且完整 返回True或False
	if os.path.exists(file_path + file_name) == False: # 先用exists()核实文件是否存在
		print('[WARNING] UUID储存文件不存在')
		return False
	else:
		try:
			with open(file_path + file_name, mode = 'r') as uuid_file:
				content = json.load(uuid_file)
				uuid_file.close()
				if 'uuid' not in content or 'complete' not in content or content['complete'] != '0x00012c':
					print('[WARNING] UUID储存文件不完整') # 内容缺一不可
					return False
				else:
					print('[INFO] UUID文件存在并完整')
					return True
		except:
			print('[WARNING] 验证文件可用性时出错 信息如下')
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

def remoteCtrl(HeartBeatController): # 与服务器建立TCP链接 接收处理命令 发送返回值 接收HBC类参数用于完全退出此程序
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
			print('[INFO] 接收服务器请求：', sevr_data)
			if sevr_data == 'q':
				rc_sock.close() # 收到 q 为手动关闭链接
				print('[INFO] TCP远控连接已关闭')
				return None
			rc_sock.sendall((sevr_data + ' reply').encode('utf-8'))
	except:
		print('[CRITICAL] 远控TCP链接发生异常 已关闭')
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



# 用于储存对用户设备进行控制的功能的类
# 错误反馈格式: ERROR_CODE 错误代码 需要发送至服务器的信息
# 例如: ERROR_CODE 05 None       
# ERROR_CODE用于使程序辨认为错误反馈 
# 错误代码发送至服务器用于辨别错误类型 
# 最后的信息为无法归类为错误类型时的附加内容 为None代表空
class RemoteCtrlFunctions():
	def __init__(self):
		# wk_dir用于储存游走与目录时的当前目录 默认为用户设备桌面路径
		self.wk_path = os.path.join(os.path.expanduser("~"), 'Desktop\\')

	def createNewFile(self, new_file):
		# 新建空文件 强制使用绝对路径 new_file为即将新建文件的绝对路径加文件名
		ph, nm = os.path.split(new_file)
		if os.path.exists(ph) == False:
			# 路径不存在 错误代码01
			return ['ERROR_CODE', '01', None]
		elif os.path.exists(new_file) == True:
			# 文件已存在 错误代码02
			return ['ERROR_CODE', '02', None]
		else:
			try:
				n_f = open(new_file, mode = 'w')
				del n_f
			except: # 发生无法捕捉确定的错误 错误代码03 附加反馈
				return ['ERROR_CODE', '03', traceback.format_exc()]

	def editFile(self, file, open_mode, operate_mode, ecding = 'utf-8', content):
		# 用于编辑文件 file为文件绝对路径加文件名 open_mode为打开文件的模式 
		# operate_mode为操作模式('read'和'write') content为对文件进行写入操作的内容
		# ecding为文件读取时的解码方式
		if os.path.split(file)[1] == '':
			# 无法对目录进行写入操作 错误代码04
			return ['ERROR_CODE', '04', None]
		elif os.path.exists(file) == False:
			# 要写入的文件不存在 错误代码05
			return ['ERROR_CODE', '05', None]
		else:
			try:
				f = open(file, mode = open_mode, encoding = ecding)
				if operate_mode == 'write':
					f.write(content)
					f.close()
				elif operate_mode == 'read':
					data = f.read()
					f.close()
					return ['INFO', data]
				else:
					# 无效的文件操作模式 错误代码06
					return ['ERROR_CODE', '06', None]
			except:
				# 意料之外的错误 错误代码07 附加反馈
				return ['ERROR_CODE', '07', traceback.format_exc()]

	def moveOrCopyFileOrDir(self, src_file_or_path, dst_file_or_path, operate_mode):
		# 若第二个参数为文件，复制source_file内容至此文件
		# 若为文件夹，复制source_file的内容至文件夹内的同名文件
		# 此方法强制使用绝对路径
		if os.path.exists(src_file_or_path) == False:
			# 源文件或目录不存在 错误代码08
			return ['ERROR_CODE', '08', None]

		if operate_mode == 'copy':
			# 复制文件或目录
			try:
				# 对不同类型的源采取针对性函数
				if os.path.isfile(src_file_or_path):
					shutil.copy(src_file_or_path, dst_file_or_path)
				elif os.path.isdir(src_file_or_path):
					shutil.copytree(src_file_or_path, dst_file_or_path)
			except Exception as e:
				# 复制文件或目录时发生的错误 错误代码09
				return ['ERROR_CODE', '09', str(e.__class__.__name__) + ' ' + str(e)]

		elif operate_mode == 'move':
			# 剪切文件或目录
			try:
				# move函数不讲究源的类型
				shutil.move(src_file_or_path, dst_file_or_path)
			except Exception as e:
				# 剪切文件或目录的错误 错误代码10
				return ['ERROR_CODE', '10', str(e.__class__.__name__) + ' ' + str(e)]