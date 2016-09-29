import time

class StopWatch:
    # single underscore to show it's a 'private' variable
    _startTime = 0 # Use double underscore to prevent clashes of names with
    _endTime = 0 # names defined by subclasses. Also known as name mangling

    def __init__(self):
        self.stops = []
        self.start()

    def start(self):
        self._startTime = time.time()

    def stop(self):
        self._endTime = time.time()
        self.stops.append( self._endTime - self._startTime )

    def getElapsedTime(self):
        self.stop()
        return self.stops[len(self.stops)-1]

    def pop(self):
        return self.stops.pop()

size = 1000000
stopWatch = StopWatch()
sum = 0

for i in range(1, size + 1):
    sum += i

stopWatch.stop()
print("The loop time is", stopWatch.getElapsedTime(), "milliseconds")
