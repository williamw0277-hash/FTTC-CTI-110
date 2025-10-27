# Willie Williams
# P4LAB1b - Turtle Graphics: Initials
# This program uses turtle graphics to draw the initials "W W"

import turtle

t = turtle.Turtle()
t.pensize(5)

# Draw first W
for i in range(2):
    t.left(70)
    t.forward(100)
    t.right(140)
    t.forward(100)
    if i == 0:
        t.penup()
        t.forward(40)
        t.pendown()

# Move to position for second W
t.penup()
t.forward(150)
t.pendown()

# Draw second W
for i in range(2):
    t.left(70)
    t.forward(100)
    t.right(140)
    t.forward(100)
    if i == 0:
        t.penup()
        t.forward(40)
        t.pendown()

turtle.done()
