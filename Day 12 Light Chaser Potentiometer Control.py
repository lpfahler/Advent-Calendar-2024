# Maker Advent Calendar
# 12 Days of Codemas
# Day 12 - Light Chaser Revised (Activity 5) 
# Incorporate a mapping function to allow better
# control of speed via potentiometer
# Lori Pfahler
# Dec 2024

# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# make a "map" function like we have in Arduino code
def myMap(x, in_min, in_max, out_min, out_max):
    x = float(x)
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(21), 15)

# Set up the potentiometer on ADC pin 26
potentiometer = ADC(Pin(26))

# Color variables
red = (255, 0, 0)
orange = (255, 125, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
violet = (125, 0, 255)
magenta = (255, 0,255)           
black = (0, 0, 0)

# Define color list
colors = [red, orange, yellow, green, cyan, violet, magenta, blue]

try:
    while True:

        # Iterate over the colors
        for j in colors:
            
            # Then iterate over 15 leds
            for i in range(15):
                
                # Set the next LED in the range to light with a color
                strip[i] = (j)
                
                # Read the potentiometer
                # Use myMap function to control speed
                potValue = potentiometer.read_u16()
                myDelay = myMap(potValue, 0, 65535, 0.005, 0.5)
                print(myDelay)
                
                # Delay - the speed of the chaser
                time.sleep(myDelay)
                
                # Send the data to the strip
                strip.write()

except KeyboardInterrupt:
    strip.fill(black)
    strip.write()