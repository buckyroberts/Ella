import random
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


def random_attr_and_value(data):
    """
    Random numeric attribute, random historical value
    """

    attr = random_numeric_attr(data)
    history = historical_values(data)
    value = random.choice(list(history[attr]))
    return attr, value


def random_numeric_attr(data):
    """
    Random numeric attribute from data (uses first item in data for analysis)
    """

    return random.choice([k for k, _ in data[0].items() if isinstance(data[0][k], (int, float, complex))])


def random_operator():
    """
    Random comparison operator
    """

    return random.choice([gt, lt])
