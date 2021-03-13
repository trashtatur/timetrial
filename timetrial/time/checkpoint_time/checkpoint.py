from time import time

from collect.collector import collect_checkpoint


def checkpoint(name: str, collect=False):
    checkpoint_value = time()
    if collect:
        collect_checkpoint({'name': name, 'value': checkpoint_value})
    else:
        print(f'name: {name}, value: {checkpoint_value}')
