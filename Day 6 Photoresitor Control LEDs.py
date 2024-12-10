# Maker Advent Calendar
# 12 Days of Codemas
# Day 6 - Photoresistor Control of LEDs
# Lori Pfahler
# Dec 2024


# import modules
from machine import ADC, Pin
import time

# Set up the LED pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# set up photoresistor
lightSensor = ADC(Pin(26))

while True:    
    # read photoresistor; calculate percentage
    light = lightSensor.read_u16()
    lightPercent = (light/65535)*100

    # print using f strings
    print(f'light = {light:5d}, light percent = {lightPercent:5.1f}%')
    
    # delay
    time.sleep(1)

    # red LED
    if lightPercent <= 30:       
        red.on()
        yellow.off()
        green.off()
        print('Red Alert!\n')       
    # yellow LED
    elif 30 < lightPercent < 60:
        red.off()
        yellow.on()
        green.off()
        print('Yellow - Situation Normal\n')
    # green LED
    else:
        red.off()
        yellow.off()
        green.on()
        print('Green - All Systems Go!\n')