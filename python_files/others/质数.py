#2 3 5 7
n = ""
nums = list(range(1,1000))
for num in nums:
	if num % 2 == 0:
		if num != 2:
			nums.remove(num)

for num in nums:
	if num % 3 == 0:
		if num != 3:
			nums.remove(num)

for num in nums:
	if num % 5 == 0:
		if num != 5:
			nums.remove(num)

for num in nums:	
	if num % 7 == 0:
		if num != 7:
			nums.remove(num)

print(nums)