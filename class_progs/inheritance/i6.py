'''
import i2

t = i2.test()
'''

from i2 import test
t = test()
print(t.a)
print(t._a)
print(t._test__a)
print(t.__dict__)

from i3 import test

t = test()
t.disp1()
t._disp2()
t._test__disp3()
