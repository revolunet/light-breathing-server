#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

from bottle import route, run

from dim import Dim

GPIO_LED_PIN = 18
GPIO_FREQUENCY = 120

PORT = 9200

if __name__=='__main__':

    thread = Dim(GPIO_LED_PIN, GPIO_FREQUENCY, intensity=30, delay=0.05)
    thread.start()

    @route('/fast')
    def fast():
        thread.update({
            'intensity': 100,
            'delay': 0.005
        })

    @route('/slow')
    def slow():
        thread.update({
            'intensity': 30,
            'delay': 0.05
        })

    run(host='0.0.0.0', port=PORT)
