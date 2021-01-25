import time
def countdown():
    n = 5
    while(n>0):
        yield n
        n = n -1


l = countdown()
for i in l:
    print(i)
    time.sleep(1)