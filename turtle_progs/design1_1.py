import turtle

t = turtle.Turtle()

lst = ["red","green","blue","yellow","orange"]

angle = 140
d = 100

for i in range(10):
	t.color(lst[i%5])
	t.forward(d)
	t.left(angle)
	d = d - 1
	
t.hideturtle()

turtle.done()