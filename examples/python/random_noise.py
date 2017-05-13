#!/usr/bin/env python

# Use the FadeCandy drivers to send random numbers into 64 RGB LEDs
from __future__ import division
import numpy as np
import opc, time

numLEDs = 64
client = opc.Client('localhost:7890')

g = np.floor(np.random.rand(numLEDs, 3) * 255)

black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs

sleepTime = 0.02

while True:
    g = np.floor(np.random.rand(numLEDs, 3) * 255)
    sleepTime = 0.2 + np.random.random_sample()/2

    client.put_pixels(g)
    time.sleep(sleepTime)

