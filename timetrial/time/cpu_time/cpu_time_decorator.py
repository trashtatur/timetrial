import os
from pathlib import Path
from time import process_time
from typing import Callable

from collect.collector import collect_cpu_time, final_round
from timetrial.time.checkpoint_time.checkpoint import checkpoint


def cpu_timerun(collect_data=False, average=False, console=False) -> Callable:
    def wrapper_function(function: Callable):
        def time_trial_standard_time(*args, **kwargs):
            start = process_time()
            function(*args, **kwargs)
            end = process_time()
            if console:
                print('{:5.3f}s'.format(end - start), end='  ')
                print('\n')
            if collect_data:
                collect_cpu_time(function.__name__, end - start, average)
            return function
        return time_trial_standard_time
    return wrapper_function


@cpu_timerun(True, False, False)
def bla():
    print('KOO')


@cpu_timerun(True, False, False)
def ble():
    print('KAAA')


def blo():
    checkpoint('blo', True)


for _ in range(1, 100):
    bla()
    ble()
    blo()

final_round(Path.home())
