# -*- coding:utf-8 -*-
import win32api
import win32con
 
name = 'test' # 要添加的项值名称
path = r'C:\Users\win10\Desktop\programming_works\hello_worldLinshi\ctOS2.0.exe' # 要添加的exe路径
# 注册表项名
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# 异常处理
try:
	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
	win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
	win32api.RegCloseKey(key)
except:
	print('添加失败。')
	input()

print('添加成功！')
input()