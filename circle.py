import turtle
def draw_img(t, sz, rev, points):
    for i in range(points): # Amount of times it loops
        t.fd(sz) # Go forward
        t.rt(360/points*rev) # Turn left 90 degrees
 
wn=turtle.Screen() # Adds screen
wn.bgcolor("pink") # Screen Colour
wn.title("functions...")
alex=turtle.Turtle() # Creates Turtle, called alex
alex.color("blue") # Sets alex's colour
 
for i in range(1):
    draw_img(alex, 50, rev=1, points=30) # How many points and how many turns = shape
 
wn.mainloop() # Loop to make full image