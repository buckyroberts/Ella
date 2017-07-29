import json
from operator import gt, lt, ge, le


def historical_values(data):
    """
    Dict keyed by attribute where value is set() of all historical values
    """

    results = {k: set() for k, v in data[0].items()}
    for row in data:
        for k, v in row.items():
            results[k].add(v)
    return results


def read_json(file):
    """
    Read JSON file
    """

    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data


def operator_to_str(func):
    """
    Convert operator function to human readable symbol
    """

    if func == gt:
        return '>'
    if func == lt:
        return '<'
    if func == ge:
        return '>='
    if func == le:
        return '<='

def write_json(file, data):
    """
    Write JSON file
    """

    with open(file, 'w') as f:
        json.dump(data, f)
