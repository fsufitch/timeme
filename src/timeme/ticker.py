import time
from threading import Thread, Event

from timeme import exceptions
from timeme.timer import Timer

class Ticker(Timer):
    def __init__(self, on_tick, tick_interval=1.0, *args, **kwargs):
        super(Ticker, self).__init__(*args, **kwargs)
        if not callable(on_tick):
            raise TypeError("`on_tick` not callable: %s" % on_tick)
        self.on_tick = on_tick
        self.thread = Thread(target=self.ticker)
        self._tick_event = Event()
        self.ticks = 0
        self.tick_interval = tick_interval


    def ticker(self):
        while not self._tick_event.wait(self.tick_interval):
            self.ticks += 1
            self.on_tick(self)

    def start(self):
        super(Ticker, self).start()
        self.thread.start()

    def end(self):
        super(Ticker, self).end()
        self._tick_event.set()

    def reset(self):
        super(Ticker, self).reset()
        self.thread = Thread(target=self.ticker)
        self.ticks = 0
        self._tick_event.clear()
        
