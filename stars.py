# Making a little stary night with the raspberry pi sensehat
# Ethan Fox 29 Jul 2023
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_PRESSED
from time import sleep

sense = SenseHat()


def pushed_down(event):
    if event.action == ACTION_RELEASED:
        print("Hey")

sense.stick.direction_any = pushed_down

