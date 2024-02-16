from machine import *
led = Pin("LED", Pin.OUT)

def flash(timer):
    led.toggle()

tim = Timer()
tim.init(freq=2, mode=Timer.PERIODIC, callback=flash)