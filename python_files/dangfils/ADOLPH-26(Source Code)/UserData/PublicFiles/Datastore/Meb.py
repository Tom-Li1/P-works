from random import randint
from random import shuffle
from time import sleep
from sys import exit
import tkinter as tk

msgboxInfo_1 = [
				['Microsoft Visual C++ Runtime Library', 'Runtime Error!\n\nProgram:C:\\WINDOWS\\system32\\cidaemon.exe\n\nR0901\n-pure virtual function call', '16'],
				['RE5DX9.exe - Application Error', 'Application normal initialization failed(0xc000005)\nClick OK to terminate the program.', '16'],
				['Brother MFL-Suite installer', 'DIFxDriverPackageInstall Error = 1610154566', '16'],
				['RUNDLL', 'Error while run C:\\PROGRA~1\\fovj\\pyft.dll\nThe specified module could not be found', '16'],
				['Explorer.EXE', 'The sepcified module could NOT be found.', '16'],
				['Windows internet firewall service', 'Firewall entry and exit rules fail.\nErrorCode-0129911xc00001', '16'],
				['C:\\Unknow path\\.', 'Can not run C:\\Windows\\addins\\FXSEXT.ecf\nFile is invalid.', '48'],
				['Windows internet firewall service', 'Unknow application tried to establish a TCP-Link.', '48'],
				['Windows update', 'Can not update windows.\n\nUnable to establish a secure connection between servers\n\nTry later.', '48'],
				['RUNDLL', 'Error while run C:\\^^^\\foj#\\%userprofile\nThe specified module could not be found', '16']
			]

msgboxInfo_2 = [
				['Windows 文件保护', "正常运行Windows所需的文件已被替换成无法识别的版本。要保持系统的稳定，Windows必须还原这些文件的原有版本\n\n无法使用应该从中复制文件的网络位置\nC:\\Windows\\System32\\drivers。", '48'],
				['没有磁盘', "请在驱动器 USB-Harddisk1 中插入磁盘。", '16'],
				['C:\\Windwos\\System32\\RDX09B.fsk', '向程序发送命令时出现问题。', '16'],
				['Windows Update', "Windows can't update important files and services.\n\nUnable to establish a secure connection to the server.", '48'],
				['资源管理器', '程序正在运行\n请勿同时打开多个进程','48'],
				['系统信息', 'Windows出现错误-系统冲突，请及时更新Windows。\n请确保此电脑链接网络，并按“是”运行自动更新服务。', '4'],
				['Windows script host', "脚本： C:\\Windows\\system32\\slmgr.vbs\n行： 1324 \n错误： 0xc004d30n2\n代码： C004D302\n源： (null)", '16'],
				['磁盘管理', '本操作将删除原C盘数据，确保已备份原数据并分区', '48'],
				['Fehler', 'Data\\FX\\post_mask_uni.fx\nD3DXCreaterEffectColpiler () schlug fehl\nmemory(111,23): error X3000: syntax error: unexpected and of flip', '16'],
				['0x0000000d1', 'STOP: 0xffff88001d30cd3', '16']
			]

msgboxInfo_3 = [
				['Missing File Error', 'Unable to find local data files, please reinstall.', '16'],
				['Users', "You don't have access to make the required system configuration modifications. \nProcess terminated", '48'],
				['应用程序错误', '应用程序发生异常 Unknow software exception (0xc0000417)\n位置为 0x004096d6\n\n要终止程序，请点击确定。', '16'],
				['添加打印机', 'Windows 无法连接到打印机\n操作失败，错误为 0x000003e3', '16'],
				['System Error', 'An error has occured. There is a possibility that your conputer is infected with virus.', '48'],
				['许可系统', '许可系统出现错误：此设备疑似存在安全性问题。如果此问题仍然存在，请与系统管理员联系。\n\n许可证状态[1.1.98]', '16'],
				['SAS Window: winlogon.exe - 应用程序错误', "'0xc00255f' 指令引用的 '0x023c6c20' 内存不能为 'written' 。\n点击确定已终止程序", '16'],
				['Error Applying Attributes', 'An error applying attribures to the file: C:\\Windows\\security\\database\\edb.chk\n\nThe requested operation delegation to be enabled on the machine.', '48'],
				['winlogon.exe - 应用程序错误', '应用程序出现异常，位置的软件异常 (0xc0000409)', '16'],
				['Windows - 注册表故障恢复', '检测到注册表被批量修改，恢复成功', '64']
			]

def main():
	names = [msgboxInfo_1, msgboxInfo_2, msgboxInfo_3]
	for i in names:
		shuffle(i)

	'''This computer has been Infected by ADOLPH-26 Virus. HOPE YOU ENJOY!'''



	for i in ['Msgm_3.bat', 'Msgm_2.bat', 'Msgm_1.bat']:
		batFile = open(i, 'w')
		for msg in names.pop():
			batFile.write('TIMEOUT /T ' + str(randint(2, 8)) + '\n\n')
			msg1 = msg[1].replace('\n', r'\n')
			batFile.write('set msg="' + msg1 + '"\n')
			batFile.write(r"""mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),""" + msg[2] + ',"' + msg[0] + '")' + "(window.close)\n")
		batFile.close()

if __name__=='__main__':
	main()
	exit()
	while True:
		sleep(1)

	window = tk.Tk()
	window.title('sss')
	window.geometry('100x100')
	window.mainloop()



'''
vbsFile = open('.vbs', 'w')
vbsFile.write("""createobject("wscript.shell").run "Msgm_1.bat",0""" + '\n')
vbsFile.write("""createobject("wscript.shell").run "Msgm_2.bat",0""" + '\n')
vbsFile.write("""createobject("wscript.shell").run "Msgm_3.bat",0""" + '\n')
vbsFile.close()


set msg="this is message.\n\nnew line"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"标题6")(window.close)
TIMEOUT /T 2

0 = vbOKOnly - 只显示确定按钮。
1 = vbOKCancel - 显示确定和取消按钮。
2 = vbAbortRetryIgnore - 显示放弃、重试和忽略按钮。
3 = vbYesNoCancel - 显示是、否和取消按钮。
4 = vbYesNo - 显示是和否按钮。
5 = vbRetryCancel - 显示重试和取消按钮。
16 = vbCritical - 显示临界信息图标。
32 = vbQuestion - 显示警告查询图标。
48 = vbExclamation - 显示警告消息图标。
64 = vbInformation - 显示信息消息图标。
0 = vbDefaultButton1 - 第一个按钮为默认按钮。
256 = vbDefaultButton2 - 第二个按钮为默认按钮。
512 = vbDefaultButton3 - 第三个按钮为默认按钮。
768 = vbDefaultButton4 - 第四个按钮为默认按钮。
0 = vbApplicationModal - 应用程序模式：用户必须响应消息框才能继续在当前应用程序中工作。
4096 = vbSystemModal - 系统模式：在用户响应消息框前，所有应用程序都被挂起。
'''