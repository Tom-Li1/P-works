nums = []
for x in range(100,1001):
	for y in range(100,1001):
		z = x * y
		if len(str(z)) == 5:
			if str(z)[0] == str(z)[-1] and str(z)[1] == str(z)[-2]:
				print(str(x)+'*'+str(y)+'='+str(z), end = ' ')
				nums.append(z)
		if len(str(z)) == 6:
			if str(z)[0] == str(z)[-1] and str(z)[1] == str(z)[-2] and str(z)[2] == str(z)[-3]:
				print(str(x)+'*'+str(y)+'='+str(z), end = ' ')
				nums.append(z)
print()
print("\nThe biggest number of them is:" + str(max(nums)))


