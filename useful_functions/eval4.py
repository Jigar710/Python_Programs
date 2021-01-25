x = 10
y = 20
# evaluate x + y expression, and return a.
a = eval('x + y')
print('a: ', a)

#****************************************************************************************
# evaluate x + y expression, but use globals parameter to override global x(10), y(20) value to x(1), y(2)
b = eval('x + y', {'x': 1, 'y': 2})
print('b: ', b)

#****************************************************************************************
# evaluate x + y expression, but set global x value to 1, and y is used a local variable y's value 3.
c = eval('x + y', {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
print('c: ', c)


#****************************************************************************************
# execute output function print and return None.
d = eval('print(x, y)')
print('d: ', d)
