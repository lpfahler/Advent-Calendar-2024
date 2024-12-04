# Maker Advent Calendar
# 12 Days of Codemas
# Day 3 - Toggle LEDs with Buttons Using Interrupt Functions
# to improve button press accuracy
# Lori Pfahler
# Dec 2024

# Import modules
from machine import Pin
from time import sleep, ticks_ms, ticks_diff

# Set up Buttons

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up LEDs
green = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

# variables to track interrupt activiation and debouncing
greenFlag = 0
greenDebounceTime = 0
yellowFlag = 0
yellowDebounceTime = 0
redFlag = 0
redDebounceTime = 0

# green interrupt function
def greenHandler(button1):
    global greenFlag, greenDebounceTime
    if (ticks_diff(ticks_ms(), greenDebounceTime)) > 300:
        # if button pressed for real, set flag to 1
        # reset debounce time variable to current time in ms
        greenFlag = 1
        greenDebounceTime = ticks_ms()

# yellow interrupt function
def yellowHandler(button2):
    global yellowFlag, yellowDebounceTime
    if (ticks_diff(ticks_ms(), yellowDebounceTime)) > 300:
        yellowFlag = 1
        yellowDebounceTime = ticks_ms()

# red interrupt function
def redHandler(button3):
    global redFlag, redDebounceTime
    if (ticks_diff(ticks_ms(), redDebounceTime)) > 300:
        redFlag = 1
        redDebounceTime = ticks_ms()

# initiate interrupt requests
button1.irq(trigger = Pin.IRQ_RISING, handler = greenHandler)
button2.irq(trigger = Pin.IRQ_RISING, handler = yellowHandler)
button3.irq(trigger = Pin.IRQ_RISING, handler = redHandler)

while True:
    # turn on/off green LED when the button 1 is pressed
    if greenFlag == 1:
        # reset flag for next button press
        greenFlag = 0
        print("Button 1 pressed")
        green.toggle()
        
    # turn on/off yellow LED when the button 2 is pressed
    if yellowFlag == 1:
        # reset flag for next button press
        yellowFlag = 0
        print("Button 2 pressed")
        yellow.toggle()
        
    # turn on/off red LED when the button 3 is pressed
    if redFlag == 1:
        # reset flag for next button press
        redFlag = 0
        print("Button 3 pressed")
        red.toggle()

