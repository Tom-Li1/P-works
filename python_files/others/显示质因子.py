def test(x):
	if x > 1:
		for y in range(2, x):
			if x % y == 0:
				return False
				break
		else:
			return True
	else:
		return False

while True:
	nums = int(input("Enter the number you want to test(must be a number)" + "\n>>>"))
	for num in range(1, nums+1):
		if nums % num == 0:
			if test(num) == True:
				print(str(num), end=" ")
				print()


