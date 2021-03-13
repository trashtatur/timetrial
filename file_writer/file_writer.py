import csv
import os
from typing import List, TextIO


def write(time_collections: dict, cpu_time_collections: dict, checkpoint_collections: dict, path: str or None):
    if path is None:
        return
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        return

    if cpu_time_collections:
        prepared_collection = __prepare_collection_for_csv(cpu_time_collections)
        __write_prepared_collection(prepared_collection, path, 'cpu_time.csv')

    if time_collections:
        prepared_collection = __prepare_collection_for_csv(time_collections)
        __write_prepared_collection(prepared_collection, path, 'time.csv')

    if checkpoint_collections:
        prepared_collection = __prepare_collection_for_csv(checkpoint_collections)
        __write_prepared_collection(prepared_collection, path, 'checkpoints.csv')


def __prepare_collection_for_csv(unprepared_collection: dict) -> List[List]:
    csv_data = []
    for key, collection in unprepared_collection.items():
        if len(csv_data) == 0:
            csv_data.append([key])
        else:
            csv_data[0].append(key)
        for index in range(0, len(collection['values']) - 1):
            index_accounting_title_row = index + 1
            if len(csv_data) <= index_accounting_title_row:
                csv_data.append([collection['values'][index]])
            else:
                csv_data[index_accounting_title_row].append(collection['values'][index])
    return csv_data


def __write_prepared_collection(collection: List[List], path, filename: str) -> None:
    full_path = os.path.join(path, filename)
    mode = 'x'
    if os.path.isfile(full_path):
        mode = 'w'
    with open(os.path.join(path, filename), mode, newline='') as new_data_file:
        writer = __writer_factory(new_data_file)
        for entry in collection:
            writer.writerow(entry)
        new_data_file.close()


def __writer_factory(filestream: TextIO):
    return csv.writer(filestream, dialect='excel', delimiter=';')
