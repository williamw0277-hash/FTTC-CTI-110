# Willie Williams
# P4LAB1a - Turtle Graphics: Square and Triangle
# This program draws a square and a triangle using loops.

import turtle

t = turtle.Turtle()

# Draw a square using a for loop
for i in range(4):
    t.forward(100)
    t.right(90)

# Reposition turtle for triangle
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw a triangle using a while loop
count = 0
while count < 3:
    t.forward(120)
    t.left(120)
    count += 1

turtle.done()
