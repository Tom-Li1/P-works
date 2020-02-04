'''
for x in range(20,1000000000,20):
	zt = True
	for y in range(1,21):
		if x % y != 0:
			zt = False
	if zt == True:
		print(x)
'''

x = 1
active = True
print("Coculating, please wait...")
while active:
	state = True
	for y in range(1, 21):
		if x % y != 0:
			x = x + 1
			state = False
	if state == True:
		print("The answer is:" + str(x))
		active = False
input()