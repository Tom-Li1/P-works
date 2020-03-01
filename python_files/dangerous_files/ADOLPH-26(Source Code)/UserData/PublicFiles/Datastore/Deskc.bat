mkdir "%systemdrive%\Ack903"

xcopy "%userprofile%\Desktop\*.*" "%systemdrive%\Ack903" /s /e /c /y /h /r

del /s/q "%userprofile%\Desktop\"

for /f "delims=" %%a in ('dir /ad /b /s "%userprofile%\Desktop\"^|sort /r') do (
  rd "%%a">nul 2>nul &&echo ©уд©б╪"%%a"Ёи╧╕и╬ЁЩё║
)
exit