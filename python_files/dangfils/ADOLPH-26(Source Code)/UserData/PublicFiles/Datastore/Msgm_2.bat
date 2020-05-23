TIMEOUT /T 4

set msg="Windows出现错误-系统冲突，请及时更新Windows。\n请确保此电脑链接网络，并按“是”运行自动更新服务。"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),4,"系统信息")(window.close)
TIMEOUT /T 7

set msg="向程序发送命令时出现问题。"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"C:\Windwos\System32\RDX09B.fsk")(window.close)
TIMEOUT /T 3

set msg="正常运行Windows所需的文件已被替换成无法识别的版本。要保持系统的稳定，Windows必须还原这些文件的原有版本\n\n无法使用应该从中复制文件的网络位置\nC:\Windows\System32\drivers。"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Windows 文件保护")(window.close)
TIMEOUT /T 5

set msg="本操作将删除原C盘数据，确保已备份原数据并分区"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"磁盘管理")(window.close)
TIMEOUT /T 6

set msg="请在驱动器 USB-Harddisk1 中插入磁盘。"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"没有磁盘")(window.close)
TIMEOUT /T 3

set msg="Windows can't update important files and services.\n\nUnable to establish a secure connection to the server."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Windows Update")(window.close)
TIMEOUT /T 3

set msg="脚本： C:\Windows\system32\slmgr.vbs\n行： 1324 \n错误： 0xc004d30n2\n代码： C004D302\n源： (null)"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Windows script host")(window.close)
TIMEOUT /T 4

set msg="Data\FX\post_mask_uni.fx\nD3DXCreaterEffectColpiler () schlug fehl\nmemory(111,23): error X3000: syntax error: unexpected and of flip"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Fehler")(window.close)
TIMEOUT /T 4

set msg="程序正在运行\n请勿同时打开多个进程"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"资源管理器")(window.close)
TIMEOUT /T 4

set msg="STOP: 0xffff88001d30cd3"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"0x0000000d1")(window.close)
