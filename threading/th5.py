import threading
import time

def firstmethod():
	for i in range(1,6):
		print(i)
		time.sleep(1)
		
print("welcome to main")
t = threading.Thread(target=firstmethod,daemon=True)
t.start()
time.sleep(2)
print("bye from main")