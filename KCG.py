import turtle
t = turtle.Turtle()

def draw_letterK():
	t.color("brown")
	t.penup()
	t.goto(-160, -100)
	t.pendown()

	t.goto(-120, -100)
	t.goto(-170, 0)
	t.goto(-120, 100)
	t.goto(-160, 100)
	t.goto(-210, 0)
	t.goto(-160, -100)

	t.penup()
	t.goto(-190, -100)
	t.pendown()

	t.color("white")
	t.begin_fill()
	t.goto(-190, 100)
	t.goto(-230, 100)
	t.goto(-230, -100)
	t.goto(-190, -100)
	t.end_fill()

	t.color("brown")
	t.goto(-190, 100)
	t.goto(-230, 100)
	t.goto(-230, -100)
	t.goto(-190, -100)

def draw_letterC():
        t.left(90)
        t.color("brown")
        t.penup()
        t.goto(50, 0)
        t.circle(50, 30)
        t.pendown()

        t.circle(50, 300)
        t.left(30)

        t.penup()
        t.goto(100, 0)
        t.circle(100, 30)
        t.pendown()

        t.circle(100, 300)
        t.right(30)

        t.penup()
        t.goto(0, 0)
        t.forward(50)
        t.pendown()

        t.forward(50)
        t.right(60)

        t.penup()
        t.goto(0, 0)
        t.forward(50)
        t.pendown()

        t.forward(50)
        t.left(30)

def draw_letterG():
        t.left(90)
        t.color("brown")
        t.penup()
        t.goto(270, 0)
        t.circle(50, 30)
        t.pendown()

        t.circle(50,300)
        t.left(120)
        t.forward(40)
        t.goto(220, 0)
        t.right(180)
        t.forward(100)
        t.left(90)

        t.penup()
        t.circle(100, 30)
        t.pendown()

        t.circle(100, 330)
        t.goto(220, 0)
        t.right(60)

        t.penup()
        t.forward(50)
        t.pendown()
        t.forward(50)
        t.right(30)

def draw_outline():
	t.color("blue")
	t.penup()
	t.goto(340, -120)
	t.pendown()

	t.goto(-250, -120)
	t.goto(-250, 120)
	t.goto(340, 120)
	t.goto(340, -120)

	t.penup()
	t.goto(345, -125)
	t.pendown()

	t.goto(-255, -125)
	t.goto(-255, 125)
	t.goto(345, 125)
	t.goto(345, -125)

while True:
        user_input = input("Enter any choice:(k, c, g, outline)\n").upper()
        if user_input == 'K':
                draw_letterK()
        if user_input == 'C':
                draw_letterC()
        if user_input == 'G'.upper():
                draw_letterG()
        if user_input == 'OUTLINE':
                draw_outline()
        if user_input == 'END':
                print("Thank you!")
                break
