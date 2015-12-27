RPI = True
try:
    import RPi.GPIO as GPIO
except:
    print "\nGPIO module not detected: DEV MODE\n"
    RPI = False
import time
import threading

import breath

DEFAULT_INTENSITY = 30
DEFAULT_DELAY = 0.03

class LightControl(threading.Thread):

    def __init__(self, power_led_pin, pwm_frequency, intensity=DEFAULT_INTENSITY, delay=DEFAULT_DELAY):
        threading.Thread.__init__(self)
        self.daemon = True

        self.step = 1
        self.intensity = intensity
        self.delay = delay

        self._stopevent = threading.Event()

        if RPI:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(power_led_pin, GPIO.OUT)
            self.dim = GPIO.PWM(power_led_pin, pwm_frequency)
            self.dim.start(1)

    def stop(self):
        print "got stop"
        self._stopevent.set()
        if RPI:
            self.dim.stop()
            GPIO.cleanup()

    def update(self, params):
        for attr, value in params.items():
            setattr(self, attr, value)

    def run(self):
        while not self._stopevent.isSet():
            if RPI:
                self.dim.start(1)
            value = max(min(100, breath.breath(intensity=self.intensity)), 0)
            print '+' * int(value)
            if RPI:
                self.dim.ChangeDutyCycle(value)
            time.sleep(self.delay)

if __name__ == '__main__':
    thread = LightControl()
    thread.start()
    while 1:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            thread.stop()
            raise
