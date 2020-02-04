import random
import time
import sys

string_1 = "你觉得你是一个很傻的玩意儿吗?\n选一个结果吧，对于你来说选择题很简单(y/n)\n>>>"
string_2 = "我觉得你选不出来，太笨了，你做点加法题吧，都是十以内的挺简单\n"

for x in range(len(string_1)):
	print(string_1[x], end = '')
	time.sleep(0.04)
	sys.stdout.flush() #刷新缓冲区

time.sleep(2)

for x in range(len(string_2)):
	print(string_2[x],end='')
	time.sleep(0.04)
	sys.stdout.flush()

while True:
	number_1 = random.randint(1,10)
	number_2 = random.randint(1,10)
	print(str(number_1) + " + " + str(number_2) + " = ?")
	answer = input(">>>")
	if answer.lower() == 'q':
		break

	if int(answer) == number_1 + number_2:
	    print("居然对了")
	    continue
	
	else:
	    print("这都做不对，你真是牛逼，答案是" + str(number_1 + number_2) + ".")
