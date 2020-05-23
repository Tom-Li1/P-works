import socket
import sys
import time
'''
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
serversocket.bind((host, port))
serversocket.listen(5)

while True:
	clientsocket, addr = serversocket.accept()
	print('%s 已连接' % str(addr))
	clientsocket.send('A message comes from server.'.encode('utf-8'))
	msg = clientsocket.recv(1024)
	print(msg.decode('utf-8'))
	clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
serversocket.bind((host, port))
serversocket.listen(5)

while True:
	print('Waiting for Connection......')
	clientsocket, addr = serversocket.accept()
	print('Connected with %s' % str(addr))

	while True:
		msg = clientsocket.recv(1024).decode()

		if not msg:
			break

		print('Message received:' + msg)
		clientsocket.send((time.strftime("[%Y-%m-%d %H:%M:%S] ") + msg).encode())
		print('Message replyed:' + time.strftime("[%Y-%m-%d %H:%M:%S] ") + msg)

	clientsocket.close()

serversocket.close()
'''
# 导入模块
import socket
# 创建tcp服务端socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
tcp_server_socket.bind(("", 8080))
# 设置监听，把服务端socket由主动套接字改成被动套接字，只能接收客户端的连接请求
tcp_server_socket.listen(128)
while True:
	# 接收客户端信息
	client_socket, client_ip = tcp_server_socket.accept()
	print("客户端：", client_ip, "连接")
	# 接收下载信息
	file_name_data = client_socket.recv(1024)
	# 解码下载信息
	file_name = file_name_data.decode()
	try:
		# 数据传输
		with open(file_name, "rb") as file:
			while True:
				# 读取文件数据
				file_data = file.read(1024)
				# 数据长度不为0表示还有数据没有写入
				if file_data:
					client_socket.send(file_data)
				# 数据为0表示传输完成
				else:
					print(file_name, "传输成功")
					break
	except Exception as e:
		print("传输异常：", e)
  # 关闭客户端连接
client_socket.close()