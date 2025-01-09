import math
from turtle import *

def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

speed(0) 
bgcolor('black')
color("red")
penup()

for i in range(2000):
    t = i * 0.01
    x = heart_x(t)
    y = heart_y(t)
    goto(x * 20, y * 20)
    pendown()

done()
