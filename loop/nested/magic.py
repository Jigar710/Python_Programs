for i in range(1,100):
    n=i
    s=0

    while(n!=0):
        a=n%10
        n=n//10
        #print(a,end='')
        s=s+a
   
    p=s
    m=0
    while(p!=0):
        b=p%10
        p=p//10
        m=m+b
  
    if(m==1):
        print(i,end=' , ')
print('These are Magic numbers')
