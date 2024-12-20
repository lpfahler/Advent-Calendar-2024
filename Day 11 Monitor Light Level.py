# Maker Advent Calendar
# 12 Days of Codemas
# Day 11 - Monitor Light Level (Activity 4) 
# Added in a graphic to indicate level visually
# Lori Pfahler
# Dec 2024

# Imports
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1)

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

# Define pin for our sensor
lightsensor = ADC(Pin(26))

# use try except to gracefully end program
try:
    while True:
        
        # Delay
        time.sleep(0.5)
        
        # Read sensor value, turn it into a percentage, round to 1 decimal
        # Store this in a variable called 'light'
        light = round((lightsensor.read_u16())/65535*100,1)
        
        # Print the light reading percentage
        print(light)
        
        # Clear the display
        display.fill(0)
        
        # Write two lines to the display
        # The line turns our light variable into a string, and adds '%' to the end
        display.text("Light level:",0,0)
        display.text((str(light) + "%"),0,12)
        
        # Create graphical display of light level
        if light < 15:
            display.ellipse(110, 18, 3, 3, 1, True)
        elif light < 50:
            display.ellipse(110, 18, 8, 8, 1, True)
        else:
            display.ellipse(110, 18, 12, 12, 1, True)

        # Update the display
        display.show()

except KeyboardInterrupt:
    # Clear the display
    display.fill(0)
    # Update the display
    display.show()
