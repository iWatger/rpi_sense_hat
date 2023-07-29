# this is a test of the raspberry pi sense hat
# Ethan Fox 29 July 2023

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

i = 0
j = 0
c = 0
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

colors = [red, green, blue]
color = red

while True:
    event = sense.stick.wait_for_event(emptybuffer=True)
    print(event.direction)
    direction = event.direction
    
    if direction == "up":
        i = (i + 1) % 8
    elif direction == "down":
        i = (i - 1) % 8
    elif direction == "left":
        j = (j - 1) % 8
    elif direction == "right":
        j = (j + 1) % 8
    else:
        color = colors[(c+1)%3]
        c += 1
    sense.clear()
    sense.set_pixel(i,j, color)
    sleep(0.25)
