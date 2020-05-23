
import psutil
 
def find(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            print('Found it:' + pid)
            break
    else:
        print("not found")
        
find(input('Pname:'))
input()