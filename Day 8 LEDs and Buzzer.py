# Maker Advent Calendar
# 12 Days of Codemas
# Day 8 - Use Temp Sensor DS19x20 with LEDs and Buzzer
# Sort of combining Activities 2 and 3 and mixing it up a bit
# Lori Pfahler
# Dec 2024

# Import Modules
import onewire, ds18x20, time
from machine import Pin, PWM

# Set up the LED pins
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)
 
# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)
 
# DS18B20 sensor object
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()

# use try except to gracefully end program with <crtl><c>
try:
    while True: 
        time.sleep(4)
        # For each sensor found (just 1 in our case)
        for rom in roms:
            # Convert the sensor units to centigrade
            sensor.convert_temp() 
            # Always wait 1 second after converting
            time.sleep(1) 
            # Take a temperature reading
            reading = sensor.read_temp(rom)
            # Calculate temperature in Fahrenheit
            readingF = reading*(9/5)+32
            # Print the reading
            print(f'Temp C: {reading:4.1f}, Temp F: {readingF:4.1f}')
            
            # If reading is less than or equal to 18 turn on RED LED
            # and make low sound
            if reading <= 18: 
                red.on() 
                yellow.off()
                green.off()
                # make a "low buzz"
                buzzer.duty_u16(5000)
                buzzer.freq(500)
                time.sleep(1)
                buzzer.duty_u16(0)                
            # If reading is between 18 and 25,
            # turn on yellow LEd and make "mid-level" sound
            elif 18 < reading < 25: 
                red.off() 
                yellow.on()
                green.off()
                # make a "mid-level" buzz
                buzzer.duty_u16(5000)
                buzzer.freq(2000)
                time.sleep(1)
                buzzer.duty_u16(0)
            # If reading is greater than or equal to 25
            # turn on green LED and make high sound
            else: 
                red.off() 
                yellow.off()
                green.on()
                # make a "high" buzz
                buzzer.duty_u16(5000)
                buzzer.freq(5000)
                time.sleep(1)
                buzzer.duty_u16(0)

except KeyboardInterrupt:
    # turn off LEDs and buzzer
    red.off() 
    yellow.off()
    green.off()
    buzzer.duty_u16(0)
    
