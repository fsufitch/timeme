class TimeMeException(Exception):
    pass

class TimerAlreadyRunningException(TimeMeException):
    pass

class TimerNotRunningException(TimeMeException):
    pass

class TimerFinishedException(TimeMeException):
    pass
