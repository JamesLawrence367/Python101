

from turtle import *
from time import *
import mouse

turtle = Turtle()
screen = Screen()
if mouse.is_pressed("left"):
    pendown()
    screen.onscreenclick(turtle.goto)
if mouse.is_pressed("right"):
    penup()
    screen.onscreenclick(turtle.goto)
turtle.getscreen()._root.mainloop()
