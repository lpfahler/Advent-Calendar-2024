# Maker Advent Calendar
# 12 Days of Codemas
# Day 3 - Press toggle LEDs without interrupts
# Lori Pfahler
# Dec 2024

# Import modules
from machine import Pin
import time

# Set up Buttons

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up LEDs
green = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

while True:
    # Small delay for debouncing
    time.sleep(0.2)
    
    # green LED and button 1
    if button1.value() == 1: 
        green.toggle()
        
    # yellow LED and button 2
    if button2.value() == 1: 
        yellow.toggle()
        
    # red LED and button 3
    if button3.value() ==1:
        red.toggle()




