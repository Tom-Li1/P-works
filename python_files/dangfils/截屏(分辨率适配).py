import time
import win32ui
from win32 import win32api, win32gui, win32print
from win32.lib import win32con
import cv2

def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h



def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()

    w,h = get_real_resolution()#注意这个是获取真实的屏幕分辨率

    # 为bitmap开辟空间win32api.GetSystemMetrics(2880)
    saveBitMap.CreateCompatibleBitmap(mfcDC,w,h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)



window_capture("haha.jpg")
img = cv2.imread('haha.jpg',1)
#对于jpg文件的压缩，第三个参数是压缩质量
cv2.imwrite('haha1.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,20])


input()