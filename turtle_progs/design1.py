import turtle

t = turtle.Turtle()
angle = 90
d = 100

for i in range(100):
	t.forward(d)
	t.left(angle)
	d = d - 1

turtle.done()