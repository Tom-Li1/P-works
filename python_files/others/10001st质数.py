x = 1
active = [2]
#while len(active) < 10001:
while True:
	#print(len(active))
	state = True
	if x <= 2:
		state = False
	else:
		for y in range(2, x):
			if x % y == 0:
				state = False	
	if state == True:
		active.append(x)
		print(x)
	x = x + 1
print("\n-----ANSWER-----")
print(str(active[-1]))