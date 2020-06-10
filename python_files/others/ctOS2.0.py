import getpass
import time
from urllib import request
import sys
import random
import os

def internet_or_not():
    try:
        html = request.get("http://www.baidu.com",timeout=2)
    
    except Exception as e:
        print(repr(e))
        return False
    
    return True

print("Getting link from server...")
time.sleep(random.randint(1,2))

if internet_or_not() == True:
    print("Server connection successful. (Dynamic ADDR:{}.{}.{}.{}  PORT:No permission to view.)".format\
            (int(random.randint(1,999)),int(random.randint(1,999)),\
                int(random.randint(1,999)),int(random.randint(1,999))))

else:
    print('Network Error, try again later.')
    time.sleep(1.5)
    sys.exit()

input_0 = getpass.getpass("Account:")
input_1 = getpass.getpass("Password:")

if input_0.lower() != 'ethan' and input_1 != '20030909':
    print("Program initialization failure caused by user name and password mismatch, try again later.")
    time.sleep(1.5)
    sys.exit()

string_0 = 'Loading configurations...'
string_1 = 'Loading variables...'
string_2 = 'Loading system config...'
string_3 = 'Initializing Protocol ctOS...'

for i in range(len(string_0)):
    print(string_0[i], end = '')
    time.sleep(0.01)
    sys.stdout.flush()
time.sleep(random.randint(1,3))
print(' done')

for i in range(len(string_1)):
    print(string_1[i], end = '')
    time.sleep(0.01)
    sys.stdout.flush()
time.sleep(random.randint(1,3))
print(' done')

for i in range(len(string_2)):
    print(string_2[i], end = '')
    time.sleep(0.01)
    sys.stdout.flush()
time.sleep(random.randint(1,3))
print(' done')

for i in range(len(string_3)):
    print(string_3[i], end = '')
    time.sleep(0.01)
    sys.stdout.flush()
time.sleep(random.randint(1,3))
print(' done')

print('Initialization completed.')
time.sleep(0.5)
print("==================================================")
print()
print("ctOS Console version 2.0 (Dec 19 2019, 23:13:2) [64 bit (AMD64)] on win32")

numLetList = list('1234567890qwertyuiopasdfghjklzxcvbnm-*#')
dPerNum = ''
for i in range(20):
    dPerNum += random.choice(numLetList)

string_4 = '''
Authentication succeeded. Welcome.
Privilege level         : C-1
Real name               : Ethan Li
Dynamic personnel number: {}
Type '-helpme-' for more information.
Please follow and obey all the rules and regulations, good luck.'''.format(dPerNum)

for i in range(len(string_4)):
    print(string_4[i], end = '')
    time.sleep(0.01)
    sys.stdout.flush()
print()

while True:
    userType = input("->")
    
    if userType == '-helpme-':
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + \
            "> I believe you can learn how to use it by yourself(Compliments for you)")
    else:
        res = os.popen(userType).read()  
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '>', end = '')
        for line in res.splitlines():
            print(line)