from math import sqrt

def isInteger(n):
	if str(n).split('.')[1] =='0':
		return True
	else:
		return False
a_list = b_list = list(range(1, 10001))
triplets = []

print("Coculating, please wait...")
for a in a_list:
	for b in b_list:
		c = sqrt(a ** 2 + b ** 2)
		if isInteger(c) == True:
			triplets.append([a, b, c])
print('\n' + '=' * 20)
for triplet in triplets:
	print(triplet)
print('=' * 20)
print('\nChecking correct triplet......')
for t in triplets:
	if sum(t) == 1000:
		print('\nAnswer found:', t)
		print('\nProduct:', t[0] * t[1] * t[2])
input()