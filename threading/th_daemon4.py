import threading

t1 = threading.Thread()
print(t1.isDaemon())
print(threading.current_thread().isDaemon())