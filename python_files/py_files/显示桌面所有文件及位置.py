import os

for root, dirs, files in os.walk(r"C:\Users\Ethan Li\Desktop"):
	print("----------ROOT----------")
	print(root)
	print("\n")

	print("-----DIRS-----")
	for dir_0 in dirs:
		print(dir_0)
	print("\n")
	
	print("-----FILES-----")
	for file in files:
		print(file)
	print("\n")

input()

	