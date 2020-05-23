TIMEOUT /T 7

set msg="An error has occured. There is a possibility that your conputer is infected with virus."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"System Error")(window.close)
TIMEOUT /T 3

set msg="You don't have access to make the required system configuration modifications. \nProcess terminated"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Users")(window.close)
TIMEOUT /T 7

set msg="许可系统出现错误：此设备疑似存在安全性问题。如果此问题仍然存在，请与系统管理员联系。\n\n许可证状态[1.1.98]"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"许可系统")(window.close)
TIMEOUT /T 4

set msg="Unable to find local data files, please reinstall."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Missing File Error")(window.close)
TIMEOUT /T 8

set msg="'0xc00255f' 指令引用的 '0x023c6c20' 内存不能为 'written' 。\n点击确定已终止程序"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"SAS Window: winlogon.exe - 应用程序错误")(window.close)
TIMEOUT /T 4

set msg="Windows 无法连接到打印机\n操作失败，错误为 0x000003e3"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"添加打印机")(window.close)
TIMEOUT /T 3

set msg="应用程序发生异常 Unknow software exception (0xc0000417)\n位置为 0x004096d6\n\n要终止程序，请点击确定。"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"应用程序错误")(window.close)
TIMEOUT /T 8

set msg="An error applying attribures to the file: C:\Windows\security\database\edb.chk\n\nThe requested operation delegation to be enabled on the machine."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Error Applying Attributes")(window.close)
TIMEOUT /T 3

set msg="检测到注册表被批量修改，恢复成功"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),64,"Windows - 注册表故障恢复")(window.close)
TIMEOUT /T 4

set msg="应用程序出现异常，位置的软件异常 (0xc0000409)"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"winlogon.exe - 应用程序错误")(window.close)
