# Functions to play songs on a passive buzzer
# From Pico W Series of videos to make a Buzzer Jukebox
# https://youtu.be/mU3y9iTukI8
# April 2023
# Lori Pfahler

# import modules
import machine
import utime

# function to play notes - adapted from Sunfounder Pico Kit
def tone(pin, frequency, duration):
    # set the pin frequency
    pin.freq(frequency)
    # use a duty cycle of 10,000 for Day 5 Maker Advent Calendar buzzer
    pin.duty_u16(10000)
    # hold the note for the duration needed
    utime.sleep_ms(duration)
    # turn the sound off
    pin.duty_u16(0)
    # a little bit of sleep to create a "break' between notes
    utime.sleep_ms(10)
    
# function for a rest in song - no sound played for the duration given
# Not used for Day 5
def rest(pin, duration):
    pin.duty_u16(0)
    utime.sleep_ms(duration)

# function for playing a song in a "paired tuple" list format
def playsong(pin, song, tempo = 1000):
    for a, b in song:
        print( a, b)
        if (a == "REST"):
            rest(pin, int(tempo/b))
        else:
            tone(pin, notes[a], int(tempo/b))
            
            
# dictionary for notes and frequencies from Tom's Hardware article
notes = {
"B0": 31,
"C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44,
"FS1": 46, "G1": 49, "GS1": 52, "A1": 55, "AS1": 58, "B1": 62,
"C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87,
"FS2": 93, "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123,
"C3": 131, "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175,
"FS3": 185, "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247,
"C4": 262, "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349,
"FS4": 370, "G4": 392, "GS4": 415, "A4": 440, "AS4": 466, "B4": 494,
"C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698,
"FS5": 740, "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988,
"C6": 1047,"CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397,
"FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976,
"C7": 2093, "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794,
"FS7": 2960, "G7": 3136, "GS7": 3322, "A7": 3520, "AS7": 3729, "B7": 3951,
"C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978
}
