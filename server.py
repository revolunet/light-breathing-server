#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

from bottle import route, run

from dim import Dim

GPIO_LED_PIN = 18
GPIO_FREQUENCY = 120

PORT = 9200

MODES = {
    'fast': {
        'intensity': 100,
        'delay': 0.005
    },
    'slow': {
        'intensity': 30,
        'delay': 0.05
    }
}

if __name__=='__main__':

    thread = Dim(GPIO_LED_PIN, GPIO_FREQUENCY, **MODES['slow'])
    thread.start()

    @route('/fast')
    def fast():
        thread.update(MODES['fast'])

    @route('/slow')
    def slow():
        thread.update(MODES['slow'])

    run(host='0.0.0.0', port=PORT)
