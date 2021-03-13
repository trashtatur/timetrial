from time import time
from typing import Callable
from collect.collector import collect_standard_time, final_round


def timerun(collect_data=False, average=False, console=False) -> Callable:
    def wrapper_function(function: Callable):
        def time_trial_standard_time(*args, **kwargs):
            start = time()
            function(*args, **kwargs)
            end = time()
            if console:
                print('{:5.3f}s'.format(end - start), end='  ')
                print('\n')
            if collect_data:
                collect_standard_time(function.__name__, end-start, average)
            return function
        return time_trial_standard_time
    return wrapper_function
