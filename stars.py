# Making a little stary night with the raspberry pi sensehat
# Ethan Fox 29 Jul 2023
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_PRESSED
from time import sleep

sense = SenseHat()

pixels = [[0,0,0]] * 64

while True:

    sense.set_pixels(pixels)
    for i in range(64):
        pixels[i] = [pixels[i][0] + 1, pixels[i][1] + 1, pixels[i][2] + 1]
    sleep(0.01)