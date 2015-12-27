#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

from bottle import route, run
from light_control import LightControl
import json

import argparse

DEFAULT_GPIO_LED_PIN = 18
DEFAULT_GPIO_FREQUENCY = 120
DEFAULT_PORT = 9200

parser = argparse.ArgumentParser(description='Make rPI light breath using GPIO')
parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='HTTP API listening port')
parser.add_argument('--pin', type=int, default=DEFAULT_GPIO_LED_PIN, help='GPIO LED pin')
parser.add_argument('--frequency', type=int, default=DEFAULT_GPIO_FREQUENCY, help='GPIO frequency')

MODES = json.load(open('./modes.json', 'r'))

if __name__=='__main__':

    args = parser.parse_args()

    print "▶ use PIN %i at frequency %i" % (args.pin, args.frequency)

    thread = LightControl(args.pin, args.frequency, **MODES['slow'])

    thread.start()

    @route('/breath/:mode')
    def update(mode):
        print 'update', mode
        thread.update(MODES[mode])

    run(host='0.0.0.0', port=args.port)
