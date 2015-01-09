timeme - Timer Utility
======================

Tired of writing and re-writing timing functions? `timeme` is a small
library for multithreaded timing and callbacks. 

`timeme` has (or will have) a variety of modules for different use
cases of time in your code. Some examples are below:

Simple Timer
------------

Just need to measure how long something took? Use the simple base
timer:

    >>> from timeme.timer import Timer
    >>> import time
    >>> t = Timer()
    >>> t.start()
    >>> time.sleep(3)
    >>> t.time
    3.0026791095733643
    >>> time.sleep(2)
    >>> t.time
    5.004983425140381
    >>> t.end()
    >>> time.sleep(1)
    >>> t.time
    5.005068302154541

Timers get started using `Timer.start()` and can get frozen using
`Timer.end()`.

To reset them, simply use `Timer.reset()`.

You can also use the timer as a context manager:

    >>> with Timer() as t:
    ...      time.sleep(3)
    ...      print(t.time)
    ...      time.sleep(2)
    ...      print(t.time)
    ... 
    3.0030922889709473
    5.004152536392212

Timer takes an optional `on_complete` argument to run when the timer
ends. Tip: use this to measure how long something in a context took.

    >>> def show_time(timer):
    ...     print("That took %.2f seconds!" % timer.time)
    ... 
    >>> with Timer(on_complete=show_time) as t:
    ...     time.sleep(2)
    ... 
    That took 2.00 seconds!

Ticker
------

Need a function called at a regular interval? `Ticker` is a subclass
of `Timer` that lets you specify a function to be called at a regular
interval in a separate thread.

    >>> from timeme.ticker import Ticker
    >>> def tickfunc(ticker):
    ...     print('tock')
    ... 
    >>> with Ticker(tickfunc, 2) as t:
    ...     time.sleep(1)
    ...     for i in range(3):
    ...         print('tick')
    ...         time.sleep(2)
    ... 
    tick
    tock
    tick
    tock
    tick
    tock
    >>> t.ticks
    3
