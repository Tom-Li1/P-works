'''
import sched,time

def func(a):
    print(time.time(),"Hello Sched!",a)

print (time.time())
s = sched.scheduler(time.time,time.sleep)

# 2为延后时间，1为优先级，func为函数名，("test1",)为函数参数
s.enter(2,1,func,("test1",))
s.enter(2,0,func,("test2",))
s.run()
print(time.time())
for i in range(2,):
	print(str(i))


a = [1,2,3]
if len(a) == 3:
	print("OK")

asd = ['7316717653133', '6249192251196744265747423553491949349698352', '6326239578318', '18694788518438586156', '7891129494954595', '17379583319528532', '698747158523863', '435576689664895', '4452445231617318564', '987111217223831136222989342338', '81353362766142828', '64444866452387493', '1724271218839987979', '9377665727333', '594752243525849', '632441572215539753697817977846174', '86256932197846862248283972241375657', '79729686524145351', '6585412275886668811642717147992444292823', '863465674813919123162824586178664583591245665294765456828489128831426', '96245544436298123', '9878799272442849', '979191338754992', '559357297257163626956188267']
aaa = []
for a in asd:
	aaa.append(len(a))
print(min(aaa))
print(max(aaa))

def listchengji(lst):
	a = lst[0] * lst[1]
	for x in lst[2:]:
		a = a * x
	return a

a = [1,2,3,4,5,6,7,8,9]
#长度9 单位长度3
#数列长度 - 单位长度 + 1 = 以单位长度组成的数列数量
#切片[0——以单位长度组成的数列数量()-1  ：单位长度至列表元素数]
print(a[0:3])
print(a[1:4])
print(a[2:5])
print(a[3:6])
print(a[4:7])
print(a[5:8])
print(a[6:9])

dictionary = {1:2,3:4,5:6}
for a, b in dictionary.items():
	print(a)
	print(b)

dick = {}
dick["a"]="b"
print(dick)

acc = list(range(1,11))
bmm = list(range(10,21))
big_dick = {}
for x, y in zip(acc, bmm): #用zip()可以将两个值封装，便于在for循环中将二个变量关联到二个数据结构
	big_dick[x] = y
print(big_dick)



def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x  
    return result

def xianglinshuzi(ls, unit):
	waiting_for_multiply = []
	for x in ls:
		if len(x) == unit:
			waiting_for_multiply.append(int(x))
		else:
			for y, z in zip(range(0,len(x)-unit+1-1), range(unit,len(x))):
				waiting_for_multiply.append(int(x[y:z]))
		waiting_for_multiply.append(int(x[-unit:]))

	return waiting_for_multiply

a = ['7316717653133', '6249192251196744265747423553491949349698352', '6326239578318', '18694788518438586156', '7891129494954595', '17379583319528532', '698747158523863', '435576689664895', '4452445231617318564', '987111217223831136222989342338', '81353362766142828', '64444866452387493', '1724271218839987979', '9377665727333', '594752243525849', '632441572215539753697817977846174', '86256932197846862248283972241375657', '79729686524145351', '6585412275886668811642717147992444292823', '863465674813919123162824586178664583591245665294765456828489128831426', '96245544436298123', '9878799272442849', '979191338754992', '559357297257163626956188267']
b = xianglinshuzi(a, 13)
str_nums = []
for c in b:
	str_nums.append(str(c))

results = []
for str_num in str_nums:
	ls = []
	for ls_num in str_num:
		ls.append(int(ls_num))
	results.append(multiplyList(ls))
print(max(results))

def isNetOK(testserver=('www.baidu.com')):
	s=socket.socket()
	s.settimeout(3)
	try:
		status = s.connect_ex(testserver)
		if status == 0:
			s.close()
			return True
		else:
			return False
	except Exception as e:
			return False

if isNetOK == True:
	print("OK")
else:
	print("Error.")

import requests
def internet_or_not():
	try:
		html = requests.get("http://www.baidu.com",timeout=2)
	except:
		return False
	return True

print(internet_or_not())

a = "WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<server._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x03E41490>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')"

import time
for i in range(4):
	time.sleep(1)
	print(str(int(time.time()))[-2:])

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[5m'
 
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
print(bcolors.WARNING + "Warning" + bcolors.ENDC)
import shutil
shutil.move("C:\\Users\\Ethan Li\\Desktop\\b.txt",\
 "C:\\a\\b.txt")
info = "段字节"
del info[0]
print(info)
'''
import random
for i in range(15):
	print(random.randint(0,2))