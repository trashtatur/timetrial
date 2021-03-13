from file_writer.file_writer import write

time_collections = {}
cpu_time_collections = {}
checkpoint_collections = {}


def collect_standard_time(key: str, value: any, average: bool):
    if key not in time_collections:
        time_collections[key] = {'values': []}
    time_collections[key]['values'].append(value)
    if average:
        time_collections[key]['avg'] = sum(time_collections[key]['values']) / len(time_collections[key]['values'])


def collect_cpu_time(key: str, value: any, average: bool):
    if key not in cpu_time_collections:
        cpu_time_collections[key] = {'values': []}
    cpu_time_collections[key]['values'].append(value)
    if average:
        cpu_time_collections[key]['avg'] = sum(cpu_time_collections[key]['values']) / len(cpu_time_collections[key]['values'])


def collect_checkpoint(checkpoint: dict):
    if checkpoint['name'] not in checkpoint_collections:
        checkpoint_collections[checkpoint['name']] = {'values': []}
    checkpoint_collections[checkpoint['name']]['values'].append(checkpoint['value'])


def final_round(path=None):
    write(time_collections, cpu_time_collections, checkpoint_collections, path)
