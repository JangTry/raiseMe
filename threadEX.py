import threading
import time

def f1(my,friend,sleep):
	while (True):
		print("Hoi! I'm ",my, "dis is mi freind ",friend)
		time.sleep(sleep)

cnt=0
def up():
	global cnt
	cnt+=2
	print(cnt)
# th=threading.Thread(target=up)
# th.start()
# for x in range(50):
# 	print(cnt)
# 	cnt+=1
# 	time.sleep(0.1)

t=threading.Timer(1,up)
t.start()