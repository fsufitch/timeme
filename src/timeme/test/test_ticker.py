import time

from timeme import exceptions
from timeme.ticker import Ticker

from .utils import check_time_within

def test_basic_ticker():
    ticks = []
    def tick():
        ticks.append('tick')
    
    t = Ticker(tick, 1)
    t.start()
    time.sleep(3.5)
    t.end()
    
    assert ticks == ['tick']*3, ticks    
    assert t.ticks == 3
