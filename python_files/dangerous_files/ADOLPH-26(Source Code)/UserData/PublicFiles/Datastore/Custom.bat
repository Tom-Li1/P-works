@echo off
reg add "hkcu\control panel\desktop" /v Wallpaper /d "%cd%\..\FavoriteIcons\wallpaper.png" /f
reg add "hkcu\control panel\desktop" /v WallpaperStyle /t REG_SZ /d 1 /f
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
exit