'''
#我的做法
nums_0 = list(range(1,10))
nums_1 = list(range(1,10))
nums = ""
active = True

while active:
	for n_0 in nums_0:
		if nums:
			print(nums)
		nums = ""
		for n_1 in nums_1:
			if n_0 <= n_1:
				a = (str(n_0) + "*" + str(n_1) + "=" + str(n_0*n_1) + " ")
				nums += a 
	print("9*9=81")
	active = False

#段字节的做方法
for x in range(1,10):
	for y in range(1,10):
		z = x * y
		print("{} * {} = {}".format(x,y,z))
input()
'''
for i in range(1,10):
	for j in range(1,i+1):
		print('%s*%s=%s' %(i,j,i*j),end = ' ')
	print()
input()

