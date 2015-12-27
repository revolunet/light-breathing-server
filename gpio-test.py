import time
import RPi.GPIO as GPIO
import breath

PIN = 12
FREQUENCY = 150

DELAY = 0.05

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

p = GPIO.PWM(PIN, FREQUENCY)
p.start(1)


def main():
    while 1:
        value = breath.breath(intensity=50)
        p.ChangeDutyCycle(value)
        print int(value) * '-'
        time.sleep(DELAY)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


