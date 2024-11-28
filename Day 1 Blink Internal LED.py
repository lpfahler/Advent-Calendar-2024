# Maker Advent Calendar
# 12 Days of Codemas
# Day 1 - Blink Internal LED
# Lori Pfahler
# Dec 2024

# import modules
from machine import Pin
from time import sleep

# setup internal LED that is on Pin #25
onboardLED = Pin(25, Pin.OUT)

while True:
    # blink internal LED
    onboardLED.toggle()
    # sleep 1/2 second so we can see the blink
    sleep(0.5)
    
