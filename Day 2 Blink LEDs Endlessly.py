# Maker Advent Calendar
# 12 Days of Codemas
# Day 2 - Let's Get Blinky Code Adapted
# Lori Pfahler
# Dec 2024

# import modules
from machine import Pin
from time import sleep

# setup LEDs
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# blink LEDs endlessly
while True:
    red.on()
    yellow.on()
    green.on()

    sleep(0.5)

    red.off()
    yellow.off()
    green.off()
    
    sleep(0.5)
