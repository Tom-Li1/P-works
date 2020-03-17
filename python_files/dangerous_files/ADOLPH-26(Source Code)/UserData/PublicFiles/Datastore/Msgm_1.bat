TIMEOUT /T 2

set msg="The sepcified module could NOT be found."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Explorer.EXE")(window.close)
TIMEOUT /T 2

set msg="Firewall entry and exit rules fail.\nErrorCode-0129911xc00001"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Windows internet firewall service")(window.close)
TIMEOUT /T 7

set msg="Can not update windows.\n\nUnable to establish a secure connection between servers\n\nTry later."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Windows update")(window.close)
TIMEOUT /T 6

set msg="Application normal initialization failed(0xc000005)\nClick OK to terminate the program."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"RE5DX9.exe - Application Error")(window.close)
TIMEOUT /T 4

set msg="Error while run C:\PROGRA~1\fovj\pyft.dll\nThe specified module could not be found"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"RUNDLL")(window.close)
TIMEOUT /T 4

set msg="DIFxDriverPackageInstall Error = 1610154566"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Brother MFL-Suite installer")(window.close)
TIMEOUT /T 7

set msg="Runtime Error!\n\nProgram:C:\WINDOWS\system32\cidaemon.exe\n\nR0901\n-pure virtual function call"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Microsoft Visual C++ Runtime Library")(window.close)
TIMEOUT /T 3

set msg="Unknow application tried to establish a TCP-Link."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Windows internet firewall service")(window.close)
TIMEOUT /T 3

set msg="Can not run C:\Windows\addins\FXSEXT.ecf\nFile is invalid."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"C:\Unknow path\.")(window.close)
TIMEOUT /T 5

set msg="Error while run C:\^^^\foj#\%userprofile\nThe specified module could not be found"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"RUNDLL")(window.close)
