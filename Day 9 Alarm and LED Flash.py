# Maker Advent Calendar
# 12 Days of Codemas
# Day 9 - Tilt Switch - Alarm and LED flash
# Flash the LEDs and turn on buzzer when switch tilted
# When the switch is upright - contact is made and reads HIGH
# "Tilted" means the switch will read LOW for how I have it set up
# This is opposite of PiHut's definition and setup
# Lori Pfahler
# Dec 2024

# Import modules
from machine import Pin, PWM
from time import sleep

# Set up tilt sensor pin
tilt = Pin(7, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set up the LED pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)


# Set PWM frequency to 1000
buzzer.freq(1000)

# use try and except to end program with <crtl><c>
try:
    while True: 
        # print tilt switch value
        print(tilt.value())
        if tilt.value() == 0:
            # turn buzzer and LEDS on
            buzzer.duty_u16(10000)
            red.on()
            yellow.on()
            green.on()
            
            sleep(1)
            
            # turn all off
            buzzer.duty_u16(0)
            red.off()
            yellow.off()
            green.off()
            
        sleep(0.1)    

except KeyboardInterrupt:
    # turn all off
    buzzer.duty_u16(0)
    red.off()
    yellow.off()
    green.off()    
    
    
    
    
    
    
    
    
    