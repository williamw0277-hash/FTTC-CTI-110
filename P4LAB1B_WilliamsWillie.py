# P4LAB1B_WilliamsWillie.py
# CTI 110
# This program draws the initials W W using loops.

import turtle

t = turtle.Turtle()
t.pensize(4)
t.color("purple")

# Function to draw a 'W'
def draw_W():
    t.left(250)
    t.forward(80)
    t.right(140)
    t.forward(40)
    t.left(140)
    t.forward(40)
    t.right(140)
    t.forward(80)
    t.penup()

# Draw first W
t.goto(-150, 0)
t.pendown()
draw_W()

# Move to position for second W (last initial)
t.goto(50, 0)
t.pendown()
draw_W()

t.hideturtle()
turtle.done()
