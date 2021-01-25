import turtle

t = turtle.Turtle()

t.begin_fill()
t.fillcolor("red")
t.circle(50)
t.end_fill()

t.forward(100)
t.begin_fill()
t.fillcolor("green")
t.circle(50)
t.end_fill()

t.forward(100)
t.begin_fill()
t.fillcolor("yellow")
t.circle(50)
t.end_fill()

t.forward(100)
t.begin_fill()
t.fillcolor("orange")
t.circle(50)
t.end_fill()

turtle.done()