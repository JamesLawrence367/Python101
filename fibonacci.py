import math
from turtle import *

last = 0
current = 10
for i in range(8):
    circle(current, 90, int(current*(math.pi)))
    current, last = current + last, current
