# Maker Advent Calendar
# 12 Days of Codemas
# Day 7 - Activity 2 - Alarm System
# Lori Pfahler
# Dec 2024


# Imports
from machine import Pin, PWM
import time

# Set up the LED pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set PWM duty to 0% at program start
buzzer.duty_u16(0)
 
# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Warm up/settle PIR sensor
print("Warming up...")
# Delay to allow the sensor to initialize
time.sleep(10) 
print("Sensor ready!")

# define alarm function  
def alarm():   
    # Set PWM duty (volume up)
    buzzer.duty_u16(5000)
    # run the for loop twice
    for i in range(2):
        # High pitch
        buzzer.freq(5000)         
        red.on()
        yellow.on()
        green.on()        
        time.sleep(0.5)
        # Low pitch 
        buzzer.freq(500)       
        red.off() 
        yellow.off()
        green.off()        
        time.sleep(0.5)
    # Set PWM duty (volume off)
    buzzer.duty_u16(0)
    # needed more sleep to reset PIR
    time.sleep(2)

# use try and except to gracefully exit program using <ctrl><c>
try:
    while True:
        # Delay to stop unnecessary program speed
        time.sleep(0.1)
        # If PIR detects movement
        if pir.value() == 1:        
            print("I SEE YOU!")
            # Call alarm function
            alarm()
            # Alert that sensor is active again
            print("Sensor active")

except KeyboardInterrupt:
    # make sure LEDs are off
    red.off() 
    yellow.off()
    green.off() 
    # turn buzzer off
    buzzer.duty_u16(0)
