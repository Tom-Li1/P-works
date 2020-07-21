import socket
import os
import json
import traceback
import time
import uuid
import sys
import threading

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

def UUID(): # 用于操作储存UUID文件的函数
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

print(UUID())