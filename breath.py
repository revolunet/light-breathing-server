import math
import time
import random


def breath(intensity=1, time_offset=0, duration=1.0, minimum=0, add_randomness=False):
    value = ((math.exp(math.sin((time.time() + time_offset) / duration * math.pi)) - 0.36787944) / 2.36) * intensity
    value = max(minimum, value)
    if add_randomness:
        # add some randomness
        value *= (1 + random.random() / 50)
    return value


if __name__ == '__main__':
    while 1:
        value = breath(intensity=80)
        print int(value) * '-'
        time.sleep(0.1)
