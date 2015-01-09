import time

from timeme import exceptions

class Timer(object):
    def __init__(self, on_complete=None, name=''):
        self.on_complete = on_complete
        self.name = name
        self.start_time = None
        self.end_time = None
        
    def reset(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        if self.end_time:
            raise exceptions.TimerFinishedException()
        if self.start_time:
            raise exceptions.TimerAlreadyRunningException()
        self.start_time = time.time()

    def end(self):
        if not self.start_time:
            raise exceptions.TimerNotRunningException()
        if self.end_time:
            raise exceptions.TimerFinishedException()
        self.end_time = time.time()
        if self.on_complete:
            self.on_complete(self)

    @property
    def time(self):
        if not self.start_time:
            raise exceptions.TimerNotRunningException()
        end = self.end_time
        if not end:
            end = time.time()
        return end-self.start_time
            

    def __enter__(self):
        self.start()

    def __exit__(self):
        self.end()

