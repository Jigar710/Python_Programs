import threading
import time


def firstmethod():
    for i in range(1, 11):
        print(threading.current_thread().name, i)
        time.sleep(1)


def secmethod():
    for i in range(10, 110, 10):
        print(threading.current_thread().name, i)
        time.sleep(1)


t1 = threading.Thread(target=firstmethod)
t2 = threading.Thread(target=secmethod)

t1.start()
t2.start()

for i in range(100, 1100, 100):
    print(threading.current_thread().name, i)
    time.sleep(1)
