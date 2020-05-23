#导入所需模块
import time
import random
import requests
import sys
import os

#写文件模块
def text_create(name, msg):
	desktop_path = "C:\\Users\\Ethan Li\\Desktop\\"  # 新创建的txt文件的存放路径
	full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
	file = open(full_path, 'w')
	file.write(msg)   
    # file.close()

#定义网络监测函数 True=联网 False=断网

def internet_or_not():
	try:
		html = requests.get("http://www.baidu.com",timeout=2)
	
	except:
		return False
	
	return True

#连接转发攻击服务器 随机时间后执行下一步进程
print("......Searching a Server......")
time.sleep(random.randint(2,5))

#判定是否联网 联网=继续攻击 断网=Retry五次
#有一次成功，显示提示消息后，进行下一步 都不成功弹出WARNING后自杀
active = 0
while active != 20:
	if internet_or_not() == True: 
		print("Connect Server Successfully (ADDR:{}.{}.{}.{})".format\
			(int(random.randint(1,999)),int(random.randint(1,999)),\
				int(random.randint(1,999)),int(random.randint(1,999))))
		print("\n")
		active = 20

	elif internet_or_not() == False:
		print("WARNING: Retrying get connection. Retry 1 miunte \nconnect = None \nstatus  = Offline \nAfter connection broken by 'NewConnectionError('<server._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x03E41490>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')"\
			 + "\n")
		active = active + 1
	time.sleep(3)

#最终检测网络连接状态，若一分钟内未连接，则退出
#有网络连接则安装
if internet_or_not() == False:
	print("ErrorType:Net work error (connect timeout)" + \
		"\n          deleting user info and quit.....")
	time.sleep(random.randint(2,5))
	print("\nFatal out of net work error. Process terminated\nQuit after 3 seconds.")
	time.sleep(3)
	exit()


#安装进度条显示
print("Getting a little present for your computer from Server...")
d=0
for data in range(1,11):
    time.sleep(random.randint(0,2))
    d += 1
    done = int(50* d / 10)
    sys.stdout.write("\r[%s%s] %d%%" % ('>' * done, ' ' * (50 - done),10*d))
    sys.stdout.flush()
print("\nInstall successfully.")
time.sleep(3)
input()