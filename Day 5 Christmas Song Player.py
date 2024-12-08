# Maker Advent Calendar
# 12 Days of Codemas
# Day 5 - Christmas Song Player
# Lori Pfahler
# Dec 2024

# import modules
from machine import Pin, PWM
import utime
import songs
import song_player

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

try:
    while True:
        # give list of songs
        print('Christmas Songs:')
        print('1. Jingle Bells')
        print('2. Wish You a Merry Chrismas')
        print('3. Santa Claus is Coming to Town')
        # get user choice
        mySong = int(input('Enter Your Choice: '))
        # play user selected song
        if mySong == 1:
            song_player.playsong(buzzer, songs.jingleBells, tempo = 2000) 
        if mySong == 2:
            song_player.playsong(buzzer, songs.wishMerryXmas, tempo = 1500)   
        if mySong == 3:
            song_player.playsong(buzzer, songs.santaClausHigh, tempo = 1500) 

        utime.sleep(1)
except KeyboardInterrupt:
    # Duty to 0 to turn the buzzer off
    buzzer.duty_u16(0)  
