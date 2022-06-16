# SPDX-FileCopyrightText: 2017 Mikey Sklar for Adafruit Industries
# SPDX-FileCopyrightText: Original code from https://learn.adafruit.com/kaleidoscope-eyes-neopixel-led-goggles-trinket-gemma/circuitpython-code
# SPDX-License-Identifier: MIT
# SPDX-FileContributor: Modified by Sam Knowles 2022

import board
import time
import random

import neopixel
from rainbowio import colorwheel

numpix = 32  # Number of NeoPixels
pixpin = board.MOSI  # Pin where NeoPixels are connected

offset = 0  # Position of spinny eyes
color = colorwheel(0)   # Colour of spinny eyes
prevtime = 0

# Change brightness if they're too bright or dim
pixels = neopixel.NeoPixel(pixpin, numpix, brightness=0.3, auto_write=False)

prevtime = time.monotonic()

while True:
    t = time.monotonic()

    # Spinny wheels (8 LEDs on at a time)
    for i in range(0, numpix):
        c = 0   # Sets the default colour to black (0)

        # 4 pixels on...
        if ((offset + i) & 7) < 2:
            # That are set to the selected colour!
            c = color

        pixels[i] = c  # First eye
        pixels[(numpix - 1) - i] = c  # Second eye (flipped)

    pixels.write()  # Write the pattern the pixels
    offset += 1     # Moves the pattern "forward" by one pixel each loop
    time.sleep(0.05)# And this controls how "fast" the pattern spins; a larger number will make it slower
    
    # Wait a random time between 1 and 10 seconds
    if (t - prevtime) > random.randrange(2,10):
        # Then set the colour to a random one!
        color = colorwheel(random.randrange(0,255))

        # And reset the timer
        prevtime = t
