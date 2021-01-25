import operator
a = 10
b = 20
print(operator.add(a,b))
print(operator.__add__(a,b))
print(operator.concat(str(a),str(b)))
print(operator.concat([1,2],[3]))

print("%13s"%"hello")