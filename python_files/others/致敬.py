import time

def eat():
	print("Eat!",end = " ")

def code():
	print("Code!",end = " ")

def sleep():
	print("Sleep",end = " ")

print("\n                -----This is their life-----")

time.sleep(1)
alive = True
while alive:
	eat()
	code()
	sleep()
