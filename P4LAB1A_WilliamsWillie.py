# P4LAB1A_WilliamsWillie.py
# CTI 110
# This program draws a square and a triangle using for loops.

import turtle

# Set up screen and pen
t = turtle.Turtle()
t.pensize(3)
t.color("blue")

# Draw a square
for side in range(4):
    t.forward(100)
    t.right(90)

# Move slightly to the right to start triangle
t.penup()
t.goto(150, 0)
t.pendown()
t.color("red")

# Draw a triangle
for side in range(3):
    t.forward(100)
    t.left(120)

t.hideturtle()
turtle.done()
