import turtle

t = turtle.Turtle()

lst = ["red","green","blue","orange"]

for i in range(4):
	t.begin_fill()
	t.fillcolor(lst[i])
	t.circle(50)
	t.end_fill()
	
	t.up()
	t.forward(100)
	t.down()

t.hideturtle()
turtle.done()