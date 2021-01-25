class time:
    def set(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
    def display(self):
        print(self.h,"hours",self.m,"minutes",self.s,"seconds")
    def add(self,t1,t2):
        temp = t1.m + t2.m
        temp += t1.s/60 + t2.s/60
        temp += t1.h*60 + t2.h*60
        self.h = int(temp/60)
        self.m = int(temp%60)
        self.s = int(((temp%60)-self.m)*60)

t1 = time()
t2 = time()
t1.set(2,35,45)
t2.set(1,30,20)
t3 = time()
t3.add(t1,t2)
t3.display()