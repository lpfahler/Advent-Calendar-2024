# Maker Advent Calendar
# 12 Days of Codemas
# Day 4 - Use Potentiometer as a Dimmer for LEDs
# With a Nonlinear Dimming Equation
# Lori Pfahler
# Dec 2024

# Imports (including PWM and ADC)
from machine import ADC, Pin, PWM
from time import sleep

# set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# set up the LEDs and PWM frequencies
red = PWM(Pin(20))
yellow = PWM(Pin(19))
green = PWM(Pin(18))
red.freq(1000)
yellow.freq(1000)
green.freq(1000)

# create a variable for the pot reading
reading = 0

while True:
    # read the pot
    reading = potentiometer.read_u16()
    
    # use a nonlinear dimming equation that is on a 0 to 100 scale
    if reading < 1000:
        # make sure it turns all LEDs off
        DC16bit = 0
    elif reading > 60000:
        # all LEDs to full brightness
        DC16bit = 65535
    else:
        # put reading on 0-100 scale
        reading100 = (reading/65535)*100

        # nonlinear dimming equation
        eq100 = 100**(reading100/100)
       
        # scale eq100 to 0-65535 (16bit) scale for duty_u16() function
        DC16bit = int((eq100/100)*65535)
    
    # print potentiometer reading and adjusted duty cycle
    print(f'reading = {reading:5d}, DC16bit = {DC16bit:5d}')
    
    # set the  PWM duty cycle for each LED
    red.duty_u16(DC16bit)
    yellow.duty_u16(DC16bit)
    green.duty_u16(DC16bit)
    
    # short delay
    sleep(0.001)
