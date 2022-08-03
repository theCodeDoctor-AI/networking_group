from typing import Any, Union


class Queue():
    '''A simple implementation of a Queue using a list for storage'''

    MAX_VALUE = 90
    MIN_VALUE = 20

    def __init__(self):
        self.data = []  # empty list for storage
        self.size = 0
        self.max_size = 40
        self.data_lost = 0

    def enqueue(self, data: Any) -> None:
        '''Add data point to the back of the queue.'''
        self.check_size()
        self.validate
        self.data.append(data)
        self.size += 1
    
    def dequeue(self) -> Union[Any, None]:
        '''Remove and return the data point at the front of the queue (or None if empty).'''
        try:
            self.data.pop(0)
            self.size -= 1
        except IndexError:
            return None

    def check_size(self):
        '''Checks size against the max size and purges the last oldest data point if full.'''
        if self.size == self.max_size:
            self.data.pop(0)        # get rid of the oldest data point
            self.data_lost += 1
            self.size -= 1

    def get_lost(self):
        '''Return the current amount of data points lost'''
        return self.data_lost
    