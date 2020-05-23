'''
import win32gui
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)
 
for h,t in hwnd_title.items():
    if t != "":
        print(h, t)

input()


import os
def popen(cmd):
	try:
		popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		popen.wait()
		lines = popen.stdout.readlines()
		return [line.decode('gbk') for line in lines]
	except BaseException as e:
		return -1

print(popen(r'C:\WINDOWS\system32\cmd.exe'))
input()
'''
import os
message = os.popen(r"C:\Users\Ethan Li\Desktop\peter's mission\dist\A.exe").readlines()
print(message)
input()


