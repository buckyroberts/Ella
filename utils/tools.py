from operator import gt, lt


def historical_values(data):
    """
    Dict keyed by attribute where value is set() of all historical values
    """

    results = {k: set() for k, v in data[0].items()}
    for row in data:
        for k, v in row.items():
            results[k].add(v)
    return results


def operator_str(func):
    """
    Convert operator function to human readable symbol
    """

    if func == gt:
        return '>'
    if func == lt:
        return '<'
