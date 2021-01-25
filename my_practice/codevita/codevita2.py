import time

def square():
    for x in range(2,1000000000):
        yield x*x


def sf(n):
    temp = []
    for i in range(1, n + 1):
        if (n % i == 0):
            temp.append(i)
    temp.remove(1)
    for p in temp:
        s = square()
        for q in s:
            if(p == q):
                return False
            if(p < q):
                break
    return True
#n = int(input("Enter the num: "))
start = time.time()
n = 297290
print(n)
lst=[]
for i in range(1,n+1):
    if (n%i==0):
        lst.append(i)
lst.remove(1)
count = 0
for i in lst:
    if sf(i)==True:
        count += 1
print(count)
end = time.time()
print(end-start)


