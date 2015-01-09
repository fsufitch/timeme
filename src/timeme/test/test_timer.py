import time

from timeme import exceptions
from timeme.timer import Timer

from .utils import check_time_within

def test_simple():
    t = Timer()
    t.start()
    time.sleep(1)
    t.end()
    check_time_within(1.0, t.time, 0.1)

def test_context_mgr():
    t = Timer()
    with t:
        time.sleep(1)
    check_time_within(1.0, t.time, 0.1)
