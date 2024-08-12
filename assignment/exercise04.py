#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

from machine import Pin, PWM
import utime

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def bequiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.3  # seconds

for i in range(64):
    print(freq)
    playtone(freq, duration)
    freq = int(freq * 1.1)

# Turn off the PWM
speaker.duty_u16(0)
