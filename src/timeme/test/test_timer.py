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

def test_context_mgr_with_exception():
    t = Timer()
    try:
        with t:
            time.sleep(1)
            raise Exception()
            time.sleep(1)
    except Exception:
        pass
    check_time_within(1.0, t.time, 0.1)

def test_measure_before_end():
    t = Timer()
    with t:
        time.sleep(1)
        check_time_within(1.0, t.time, 0.1)
        time.sleep(1)
        check_time_within(2.0, t.time, 0.1)
        time.sleep(1)
    check_time_within(3.0, t.time, 0.1)
