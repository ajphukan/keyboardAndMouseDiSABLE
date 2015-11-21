import os
import time
list_id=[]
id = os.popen('xinput |grep -iv "master"|grep -iv "core"|grep -P -o "id=[0-9]+"|grep -P -o "[0-9]+"')
for i in id:
	list_id.append(i)



def lockSystem():
	for i in list_id:
		os.system("xinput disable " + i )

def unlockSystem():
	for i in list_id:
		os.system("xinput enable " + i)

####an example for test run	

lockSystem()
print "System Locked"
time.sleep(10)
unlockSystem()
print "System Unlocked"
#######
