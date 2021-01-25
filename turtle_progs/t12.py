import turtle

t = turtle.Turtle()

t.begin_fill()
t.fillcolor("red")
t.circle(50)
t.end_fill()

t.up()
t.forward(100)
t.down()

t.begin_fill()
t.fillcolor("green")
t.circle(50)
t.end_fill()

turtle.done()