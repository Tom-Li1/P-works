from os import system
from random import randint
from time import sleep
from sys import stdout
from sys import exit

def printOneByOne(data,wait_time=0.05,second_line=True):
 #用于进行单个字符打印的函数
	for i in range(len(data)):
		print(data[i], end = "")
		stdout.flush()
		sleep(wait_time)
	if second_line == True:
		print()

print(r'''
      ___           ___           ___           ___           ___     
     /\  \         /\__\         /\  \         /\__\         /\  \    
    /::\  \       /::|  |       /::\  \       /:/  /        /::\  \   
   /:/\ \  \     /:|:|  |      /:/\:\  \     /:/__/        /:/\:\  \  
  _\:\~\ \  \   /:/|:|  |__   /::\~\:\  \   /::\__\____   /::\~\:\  \ 
 /\ \:\ \ \__\ /:/ |:| /\__\ /:/\:\ \:\__\ /:/\:::::\__\ /:/\:\ \:\__\
 \:\ \:\ \/__/ \/__|:|/:/  / \/__\:\/:/  / \/_|:|~~|~    \:\~\:\ \/__/
  \:\ \:\__\       |:/:/  /       \::/  /     |:|  |      \:\ \:\__\  
   \:\/:/  /       |::/  /        /:/  /      |:|  |       \:\ \/__/  
    \::/  /        /:/  /        /:/  /       |:|  |        \:\__\    
     \/__/         \/__/         \/__/         \|__|         \/__/    v1.8.0 alpha 3DM汉化组汉化
''')
print()
print()
sleep(0.3)
printOneByOne('按下回车键开始！')
input()

system('cls')
printOneByOne("今天是多么好的一天啊, 鸟儿在唱歌 ,花儿再开放, 像这样的电脑......")
sleep(0.5)
print('\n')
printOneByOne("应 当 在 地 狱 里 被 焚 烧 ！", wait_time = 0.08)
sleep(1)

printOneByOne('正在初始化RSA-2048 AES-128加密算法')
printOneByOne("""ACCESS TO SYSTEM\n\
      
      Version 3.2654.2Initializing...\n\
      
      % WRITING DEPS%\n\
      
      % pkg(python).\n\
      
      % metlpython, J - which(python, J.\n\
      
      % meet(python, oSx) : bash'brew install python').%\n\
      
      :- multifile pkg/1.:- multifile meet2.:- multifile met2\n\
      
      - multifile depends/3.\n\
      
      二dynamic platfom/1.% pkg(?Pkg) is nondet.\n\
      
      % met(+Pkg, +Platform) is semidet.% meet(+Pkg, +Platform) is semidet.marelle_ search_ path\n\
      
      ("~/.marelle/deps'.marelle search path('marelle-deps').marelle search_ path('deps').\n\
      
      %\n\
      
      % CORE CODE%\n\
      
      main :=\n\
      
      ( current prolog. flag(os_ argv, Argv)""", 0.001)

printOneByOne("""70 COnC CODE%

      main :-

      ( current prolog. flag(os _argv, Argv)→true

      curent prolog. flagargv, Argv)append([L -JJJ], Rest, Argv),detect platform,load deps,

      ( Rest二[CommandSubArgs] >main(Command, SubArgs)

      usage).

      main(scan, Rest) :-( Rest= --all'] >scan_ packages(all)

      ; Rest= r--missing] >、scan packages(missing);Rest=0>

      scan_ packages(unprefixed))

      main(list, Rest) :-

      ( Rest = 0 ; Rest = [Pattern]),(Rest= 0 -

      findal(P, (pkg(P), 1+ ishidden(P)), Ps0); Rest = [Pattern] -

      join([*", Pattern, "门Glob),

      findalP, (pkg(P), wildcard match(Glob, P), |+ sidedn() Ps0)),sort(Ps0, Ps)|""", wait_time = 0.001)

system('cls')
system("shutdown -s -t 90")
print("""!!!重要資訊!!!

      您的部分主板内置BIOS已被RSA-2048和AES 128暗碼進行了加密。
      部分硬件已丧失原本的功能，
      欲獲取更多關於RSA的資訊，請參照:

      htp:/zh.wikipedia. org/iko/RSA加密演算法

      tp://h/wilipedia. org/wila/高级加密标准

      只有我們的私密伺服器上的私人密钥和解密程式才能解密。
      如要解锁您的私人端，請點擊以下其中一個達結:

      1. htp://3ezlko7fwyood.tor2web.org/3ADBEEDE0B85C0982. htp://zcvkoi7fwyood. onion.to/3ADBEEDE0B85C0983. htp://z/wkoi7fwyood.nion.cab/3ADBEEDE0B85C098如果以上位址都無法打開，請按照以下步骤操作:

      1. 下载並安装洋惠流覽器(Tor Browser) : htps:///w.oprojee. org/download/download easy html

      2.安装成功後，通行流覽器，等待初始化。

      3.键入: i3ezvkoi7Fwyood onion/3ADBEEDE0B85C0984. 按网站上的說明進行操作。

      亦或嘗試解決 少量 的 數學問題 來 解鎖
      按 回車鍵 來使用 最終解決方案""")

input()
system('cls')
printOneByOne("妳已經選擇了最終的解決方案\n")

right = 0
for i in range(5):
	choose = randint(0, 3)
	
	if choose == 0:
		number_1 = randint(1, 99)
		number_2 = randint(1, 99)
		answer = number_1 + number_2
		userAnswer = input("\n{} + {} = ?\n>>>".format(number_1, number_2))
		
		try:
			userAnswer = int(userAnswer)
		
		except:
			print("False")
		
		else:
			if userAnswer == answer:
				right += 1
				print("True")

			else:
				print("False")

	elif choose == 1:
		number_1 = randint(1, 99)
		number_2 = randint(1, 99)
		answer = number_1 - number_2
		userAnswer = input("{} - {} = ?\n>>>".format(number_1, number_2))

		try:
			userAnswer = int(userAnswer)
		
		except:
			print("False")
		
		else:
			if userAnswer == answer:
				right += 1
				print("True")

			else:
				print("False")

	elif choose == 2:
			number_1 = randint(1, 99)
			number_2 = randint(1, 99)
			answer = number_1 * number_2
			userAnswer = input("{} x {} = ?\n>>>".format(number_1, number_2))

			try:
				userAnswer = int(userAnswer)
		
			except:
				print("False")
		
			else:
				if userAnswer == answer:
					right += 1
					print("True")

				else:
					print("False")

if right >= 3:
	system("shutdown -a")
	printOneByOne("\n正在恢復數據...")
	d=0
	for data in range(1,11):
	    sleep(randint(0,2))
	    d += 1
	    done = int(50* d / 10)
	    stdout.write("\r[%s%s] %d%%" % ('>' * done, ' ' * (50 - done),10*d))
	    stdout.flush()
	print('恢復數據完毕')
	sleep(1)
	exit()

else:
	printOneByOne('祝 你 好 运')
	system('')
	sleep(3)
	exit()




