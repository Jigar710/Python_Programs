'''
import i2

t = i2.test()
'''

from i2 import test as t1
from i3 import test as t2


t = t1()
print(t.a)
print(t._a)
print(t._test__a)
print(t.__dict__)

t = t2()
t.disp1()
t._disp2()
t._test__disp3()
