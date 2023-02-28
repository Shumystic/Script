import time
from itertools import count

def buzzergen(period):
    nexttime = time.time() + period
    for i in count():
        now = time.time()
        tosleep = nexttime - now
        if tosleep > 0:
            time.sleep(tosleep)
            nexttime += period
        else:
            nexttime = now + period
        yield i, nexttime