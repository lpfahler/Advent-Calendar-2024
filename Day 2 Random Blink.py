# Maker Advent Calendar
# 12 Days of Codemas
# Day 2 - Random Blink - kind of like a flame?
# Lori Pfahler
# Dec 2024

# import modules
from machine import Pin
from time import sleep
from random import randint

# setup LEDs
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# blink LEDs randomly fast
while True:
    red.value(randint(0, 1))
    yellow.value(randint(0, 1))
    green.value(randint(0,1))

    sleep(0.05)

