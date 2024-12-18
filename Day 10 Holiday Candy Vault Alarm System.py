# Maker Advent Calendar
# 12 Days of Codemas
# Day 10 - Holiday Candy Vault Alarm System
# Lori Pfahler
# Dec 2024

# Imports
from machine import Pin, PWM
from time import sleep

# Set up the Beam pin
beam = Pin(21, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Start with the buzzer volume off (duty 0)
buzzer.duty_u16(0)

# Set up the LED pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)


try:
    while True:        
        print(beam.value())
        if beam.value() == 0:
            # turn on LEDs
            red.on()
            yellow.on()
            green.on()
            # turn on buzzer
            buzzer.duty_u16(10000)
            # make alarm sound
            for i in range(3):
                buzzer.freq(1000)
                sleep(0.2)
                buzzer.freq(500)
                sleep(0.2)
            # turn buzzer off
            buzzer.duty_u16(0)
            # turn LEDs off
            red.off()
            yellow.off()
            green.off()
        # delay
        sleep(0.1)

except KeyboardInterrupt:
    # turn buzzer off
    buzzer.duty_u16(0)
    # turn LEDs off
    red.off()
    yellow.off()
    green.off()
        
    
