# object as an return value
class time:
    def set(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def disp(self):
        print(self.h, self.m, self.s)

    def __add__(self, x):
        t = time()
        '''
        t.h = self.h + x.h
        t.m = self.m + x.m
        t.s = self.s + x.s
        '''
        t.set(self.h + x.h, self.m + x.m, self.s + x.s)
        return t


t1 = time()
t2 = time()
t3 = time()

# t1.set(1,2,3)
t1.h = 1
t1.m = 2
t1.s = 3

t2.set(10, 20, 30)

t3 = t1 + t2
# t3 = t1.__add__(t2)

t3.disp()
