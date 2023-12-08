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