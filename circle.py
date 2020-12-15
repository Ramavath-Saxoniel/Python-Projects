import turtle
t = turtle.Turtle()

turtle.bgcolor("green")
colour = "white"
colour1 = "blue"
colour2 = "red"

t.color(colour, colour1)
t.begin_fill()
t.circle(100, 180)
t.circle(200, 180)
t.circle(100, -180)
t.end_fill()

t.penup()
t.goto(0, 50)
t.pendown()
t.color(colour, colour2)
t.begin_fill()
t.circle(-50)
t.end_fill()
