import tkinter as tk
import os
import time
import threading
from random import randint
from random import choice
import subprocess

# 一分种倒计时 多线程每秒修改变量并显示
def clock():
	while True:
		try:
			clock = open(os.path.abspath('..') + r"\UserSettings\TIR.txt", 'r').read()
		except:
			clock = ' '
		
		try:
			clock_1.place_forget()
		except:
			pass
		
		clock_1 = tk.Label(window, text= clock + 's', fg = 'DarkRed', font=('Arial', 18), width=12, height=1)
		clock_1.place(x=35,y=475)
		time.sleep(1)

sleepTime = []
timeValue = 0.1
for i in range(15):
	sleepTime.append(timeValue)
	timeValue += 0.1

# 生成浮点数列表 随机显示数字 表示时间
def randomClock():
	while True:
		try:
			clock_2.place_forget()
		except:
			pass
		clock_2 = tk.Label(window, text= str(randint(0, 59)) + ' : ' + str(randint(0, 59)) + ' : ' +str(randint(0, 59)), \
			fg = 'DarkRed', font=('Arial', 18), width=12, height=1)
		clock_2.place(x=35,y=290)
		time.sleep(choice(sleepTime))

def randomTime():
	while True:
		try:
			timeleft_1.place_forget()
		except:
			pass                
		timeleft_1 = tk.Label(window, text = str(randint(0, 59)) + ':' + str(randint(0, 59)) + ':' +str(randint(0, 59)) + \
			'  ' + choice('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()) + ' ' + str(randint(1, 31)) + \
			'  ' + str(randint(1900, 2100)), fg = 'DarkRed', font = ('Arial', 10), width=20, height=1)
		timeleft_1.place(x=50, y=220)
		time.sleep(choice(sleepTime))

# 创建窗口
window = tk.Tk()
window.title('Wana Fix')
window.geometry('1090x650')

# 将上方三个函数设为子线程并启动
mainUserUpdatet = threading.Thread(target = clock)
mainUserUpdatet.setDaemon(True)
mainUserUpdatet.start()
mainUserUpdatet = threading.Thread(target = randomClock)
mainUserUpdatet.setDaemon(True)
mainUserUpdatet.start()
mainUserUpdatet = threading.Thread(target = randomTime)
mainUserUpdatet.setDaemon(True)
mainUserUpdatet.start()

# 放置背景图
img_png = tk.PhotoImage(file = os.path.abspath('..') + r'\FavoriteIcons\image.png')
label_img = tk.Label(window, image = img_png)
label_img.place(x=0, y=0)

# 写入当前运行时间的下一分钟 用于显示发作时间
try:
	haveRunOrNot = open(os.path.abspath('..') + r'\UserSettings\UserLog.txt', 'r')
	runTime = haveRunOrNot.read()
except FileNotFoundError:
	haveRunOrNot = open(os.path.abspath('..') + r'\UserSettings\UserLog.txt', 'w')
	m = str(int(time.strftime("%M", time.localtime())) + 2)
	if m == '60':
		m = '00'
	if m == '59':
		m = '01'
	haveRunOrNot.write(time.strftime("%Y-%m-%d %H:" + m + ":%S", time.localtime()))
	haveRunOrNot.close()
	haveRunOrNot = open(os.path.abspath('..') + r'\UserSettings\UserLog.txt', 'r')
	runTime = haveRunOrNot.read()
	haveRunOrNot.close()

if not runTime:
	haveRunOrNot.close()
	haveRunOrNot = open(os.path.abspath('..') + r'\UserSettings\UserLog.txt', 'w')
	m = str(int(time.strftime("%M", time.localtime())) + 2)
	if m == '60':
		m = '00'
	if m == '59':
		m = '01'
	haveRunOrNot.write(time.strftime("%Y-%m-%d %H:" + m + ":%S", time.localtime()))
	haveRunOrNot.close()
	haveRunOrNot = open(os.path.abspath('..') + r'\UserSettings\UserLog.txt', 'r')
	runTime = haveRunOrNot.read()
	haveRunOrNot.close()

# 放置剩余时间显示模块
leftTime = tk.Label(window, text = runTime, fg = 'DarkRed', font = ('Arial', 10), width=20, height=1)
leftTime.place(x=50, y=410)

on_hit = True
# 放置三个按钮
def about_def():
	global on_hit
	#string = """mshta vbscript:msgbox("Happiness is a kind of special feeling when you have supper be cooked by dinner!",64,"What is happiness?")(window.close)"""
	#os.system(string)
	if on_hit == False:
		contant = ["Guide of blank staring","At this moment, you should relax and think nothing. The release will come soon......"] 
	else:
		contant = ["如何变得茫然","此时此刻，你应该放松自己，不要去想你未保存的文档了。大解放即将来临......"]
	contant = "mshta vbscript:msgbox(" + '"' + contant[1] + '",48,' + '"' + contant[0] + '")(window.close)'
	subprocess.run(contant, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
about = tk.Button(window, text="About 'stare blankly'", font=('Arial', 8), width=18, height=1, command=about_def)
about.place(x=70, y=540)

def how_def():
	global on_hit
	#string = """mshta vbscript:msgbox("Lesson one of life: Do NOT have any children!",48,"Father")(window.close)"""
	#os.system(string)
	if on_hit == False:
		contant = ["Stare blankly","Stare at your computer blankly is the best way to solve the ploblem, Show your face to yourself without feeling, understanding, or interest."] 
	else:
		contant = ["发呆","茫然地凝视着你的电脑是当下最好的解决办法，把你没有感觉与意识和理解能力的脸展示出来。"]
	contant = "mshta vbscript:msgbox(" + '"' + contant[1] + '",48,' + '"' + contant[0] + '")(window.close)'
	subprocess.run(contant, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
how = tk.Button(window, text='How to be blank', font=('Arial', 8), width=18, height=1, command=how_def)
how.place(x=70, y=570)

def con_def():
	global on_hit
	#string = """mshta vbscript:msgbox("You can talk to yourself when you have supper that cooked by dinner, I can here you when you do that!",64,"Author's words")(window.close)"""
	#os.system(string)
	if on_hit == False:
		contant = ["Contact us","Sorry, I shouldn't meet strangers, my mother said."]
	else:
		contant = ["联系我们","我在你后边看着你呢。"]
	contant = "mshta vbscript:msgbox(" + '"' + contant[1] + '",48,' + '"' + contant[0] + '")(window.close)'
	subprocess.run(contant, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
con = tk.Button(window, text='Contact Us', font=('Arial', 8), width=18, height=1, command=con_def)
con.place(x=70, y=600)

def fake_def():
	global on_hit
	#string = """mshta vbscript:msgbox("You can talk to yourself when you have supper that cooked by dinner, I can here you when you do that!",64,"Author's words")(window.close)"""
	#os.system(string)
	a = open(os.path.abspath('..') + r'\UserSettings\KsysN.txt', 'w')
	a.close()
	if on_hit == False:
		contant = ["I lied to you","So, why you pushed the butten? I have said I will definitely cheat you...lol"] 
	else:
		contant = ["我是绝对会骗你的","所以说，你点击了那个按钮还企图缓解状况？我说过我是绝对会骗你的:p"]
	contant = "mshta vbscript:msgbox(" + '"' + contant[1] + '",48,' + '"' + contant[0] + '")(window.close)'
	subprocess.run(contant, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
fake = tk.Button(window, text='Delay', font=('Arial', 10), width=38, height=1, command=fake_def)
fake.place(x=322, y=618)

def cut_def():
	global on_hit
	#string = """mshta vbscript:msgbox("You can talk to yourself when you have supper that cooked by dinner, I can here you when you do that!",64,"Author's words")(window.close)"""
	#os.system(string)
	if on_hit == False:
		contant = ["Guide of cuting","Pick up your tool and JUST DO IT! It's time to say goodbye to your little bro:("] 
	else:
		contant = ["切丁指南","拿起工具，干就完了！"]
	contant = "mshta vbscript:msgbox(" + '"' + contant[1] + '",48,' + '"' + contant[0] + '")(window.close)'
	subprocess.run(contant, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cut = tk.Button(window, text='Cut down your little bro', font=('Arial', 10), width=38, height=1, command=cut_def)
cut.place(x=731, y=618)

#放置主要信息显示部件 以及 切换语言按钮 44
artical_chi = '''不戒色有什么后果？
    沉迷色情会让一个人面容变丑，面相猥琐，面部轮廓凹陷扭曲变形，脱发白发，痤疮，痘痘，胆
小怕事懦弱，性格敏感多疑，社交恐惧，身行猥琐，气场全无，对视困难，双眼空洞无神，事业工作
家庭婚姻不顺，脑力严重下降。肾精需要化生元气气血骨髓的，请呵护你的肾精，婚前禁欲婚后节制，
有病先禁欲。
我该怎么做？
    我们提供两种方法：
    第一种是删除Windows，经过对您电脑使用的长期观测，第一种方法是删除掉Windows操作系统，
这样做是有原因的，我们发现您最近经常浏览不良网站，所以我们打算这样做。意在给您指出一条戒
撸的明路，帮助您更加专业的戒色，克服撸管恶习，回归阳光纯正，通过不使用电脑，您可以戒掉撸
管，找回原来那个健康向上的你！只需要等待即可达成目标！
    第二种是立刻躲屌，彻底戒色。点击下面右边的按钮，查看剁屌戒色的正确方式与注意事项。
    这和一般戒色方法有本质上的区别。您大可在网上找找戒撸戒色的方法，我敢保证，没有我们的
戒撸服务,就算老天来了你也还是那个样儿！
有没有其他的方法?
    当然有办法。但是接下来只能靠你了。我们以人格担保,能够提供安全有效的戒色服务。但这是要
付出代价的,也不能无限期的推迟。请点击下面左侧的按钮，就可以延长你的考虑时间。请您放心,我
绝对会骗你的。但想要放弃这次戒色的绝佳机会，需要您学会一项技能。天上会随便掉下一个馅饼，
然后给您吃吗？当然不是，不论如何都是需要付出的。 最好在一分钟之内学会所说的技能，时间到了
对你是绝对不利的。
您应该学会的技能：
我们觉得您总是担惊受怕，所及希望您能够学会如何放空自我，如何发呆。不懂发呆是什么的，请点
左下角的<About 'stare blankly'>查看信息。不会发呆的，请点击<'How to be blank'>查看发
呆的具体方法。
联系方式：
	如果需要我们的帮助，请点击<Contact us>试着找到我们。

	祝你好运！'''

artical_eng = '''What happened?
Actually nothing happened, you don't have to worry about it.
We want you to keep calm and then stare blankly. If you don't know what blank is.
If you don't know how to daze, please click to check the information in the lower 
left corner. There are also two buttons at the bottom that you can guess from
their names, Or click on them.

Time is running, good luck!'''

info = tk.StringVar()
info.set(artical_chi)
l = tk.Label(window, textvariable=info, bg='white', fg='black', font=('华文隶书', 10), width=84, height=28, justify = 'left', anchor = 'nw')
l.place(x = 322, y = 44)

def hit_me():
    global on_hit
    global artical_chi
    global artical_eng
    
    if on_hit == False:
        on_hit = True
        info.set(artical_chi)
    else:
        on_hit = False
        info.set(artical_eng)
 
b = tk.Button(window, text='Change language', font=('Arial', 8), width=15, height=1, command=hit_me)
b.place(x=950, y=10)

window.mainloop()