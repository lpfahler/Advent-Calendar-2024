# Maker Advent Calendar
# 12 Days of Codemas
# Day 4 - Potentiometer Control of LEDs
# No changes to tutuorial code
# Lori Pfahler
# Dec 2024

# import modules
from machine import ADC, Pin
from time import sleep

# set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# set up the LEDs
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# create a variable for the pot reading
reading = 0

while True: 
    # read pot
    reading = potentiometer.read_u16() 
    # print pot reading
    print(reading)
    # delay
    sleep(0.1)
    
    # turn on red LED if <= 20,000
    if reading <= 20000: 
        red.on()
        yellow.off()
        green.off()
    
    # turn on yellow if between
    # 20,000 and 40,000
    elif 20000 < reading < 40000: 
        red.off()
        yellow.on()
        green.off()
    
    # turn of green of >= 40,000
    elif reading >= 40000: 
        red.off()
        yellow.off()
        green.on()
