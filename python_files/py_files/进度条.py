import time
import random
import requests
import sys
import os

print("")
d=0
for data in range(1,11):
    time.sleep(random.randint(0,2))
    d += 1
    done = int(50* d / 10)
    sys.stdout.write("\r[%s%s] %d%%" % ('>' * done, ' ' * (50 - done),10*d))
    sys.stdout.flush()
print("\nProgram started successfully.")
time.sleep(3)
input()