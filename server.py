#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

from bottle import route, run
from light_control import LightControl
import json

import argparse

DEFAULT_GPIO_LED_PIN = 18
DEFAULT_GPIO_FREQUENCY = 120
DEFAULT_PORT = 9200
DEFAULT_BREATH_INTENSITY = 5
DEFAULT_BREATH_DELAY=0.01

parser = argparse.ArgumentParser(description='Make rPI light breath using GPIO')
parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='HTTP API listening port')
parser.add_argument('--pin', type=int, default=DEFAULT_GPIO_LED_PIN, help='GPIO LED pin')
parser.add_argument('--frequency', type=int, default=DEFAULT_GPIO_FREQUENCY, help='GPIO frequency')
parser.add_argument('--intensity', type=int, default=DEFAULT_BREATH_INTENSITY, help='Max breath intensity')
parser.add_argument('--delay', type=float, default=DEFAULT_BREATH_DELAY, help='Breath refresh delay in seconds')

MODES = json.load(open('./modes.json', 'r'))

if __name__=='__main__':

    args = parser.parse_args()

    print "▶ use PIN %i at frequency %i" % (args.pin, args.frequency)

    thread = LightControl(args.pin, args.frequency, intensity=args.intensity, delay=args.delay)

    thread.start()

    # some default modes
    @route('/breath/mode/:mode')
    def mode(mode):
        print 'update mode', mode
        thread.update(MODES[mode])

    # custom settings
    @route('/breath/<intensity:int>/<delay:float>')
    def update(intensity, delay):
        thread.update({
            'intensity': intensity,
            'delay': delay
        })

    run(host='0.0.0.0', port=args.port)
