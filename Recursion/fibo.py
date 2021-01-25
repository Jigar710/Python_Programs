m = 0
def fibo1(n):
    global m
    m = n-2
    print("0\n1")
    fibo2(0,1)
def fibo2(a,b):
    global m
    print(a+b)
    m = m - 1
    if m > 0:
        a,b = b,a+b
        fibo2(a,b)
fibo1(10)