#!/usr/bin/env python

# Use the FadeCandy drivers to send random numbers into 64 RGB LEDs
from __future__ import division
import numpy as np
import opc, time, sys, signal
import argparse

parser = argparse.ArgumentParser(description='Randomly Flash the LEDs.')
parser.add_argument('refresh_period', metavar='tau', type=float,
                    help='LED Refresh Period [ms]')
args = parser.parse_args()

tau = args.refresh_period

numLEDs = 64
client = opc.Client('localhost:7890')

black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs

# catch the CTRL-C and die gracefully
def sigint_handler(signum, frame):
        print('\n')
        print('CTRL-C Encountered...Shutting down.\n')
        client.put_pixels(black)
        sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)



while True:
    g = np.floor(np.random.rand(numLEDs, 3) * 255)
    sleepTime = tau + np.random.random_sample()

    client.put_pixels(g)
    time.sleep(sleepTime)

