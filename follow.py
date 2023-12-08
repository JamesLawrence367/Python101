"""""
import turtle, mouse
from threading import Thread

def follow():
    while True:
        xy = mouse.get_position()
        my.setpos(xy[0], xy[1])
        print(xy[0], xy[1])

wn = turtle.Screen()
wn.bgcolor("orange")
my=turtle.Turtle()

t1 = Thread(target=follow)
t1.start()

wn.mainloop()
"""
from turtle import *


def drag(x, y):
    t.ondrag(None) # stop backtracking 
    t.setheading(t.towards(x, y)) # sets direction
    t.goto(x, y) # go to co-ords
    t.ondrag(drag) # repeat


sc = Screen() # create canvas
sc.bgcolor("lightgreen") #Optional details
t = Turtle() # create turtle/pointer
t.shape("turtle")
t.speed(10)
t.ondrag(drag) # call function when dragged
sc.mainloop()