inf = input("----斐波那契数列1—?-----" + "\n>>>")
print("\n-----Conputer coculating，wait......-----")

num_0 = [1, 1]
num_1 = 0
while num_1 <= int(inf):
	num_1 = num_0[-1] + num_0[-2]
	num_0.append(num_1)

num_2 = []
for num_3 in num_0:
	if num_3 % 2 == 0:
		num_2.append(num_3)

print("\n-----斐波那契数列表-----")
print(num_0)
print("\n-----其中的偶数-----")
print(num_2)
print("\n-----数字数量-----")
print(str(len(num_0)))
print("\n-----偶数项的和-----")
print(str(sum(num_2)))