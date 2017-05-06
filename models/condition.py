from utils.tools import random_attr_and_value, random_operator, operator_str


class Condition:

    def __init__(self, data):
        self.attr, self.value = random_attr_and_value(data)
        self.operator = random_operator()

    def __str__(self):
        return f"{self.attr} {operator_str(self.operator)} {self.value}"

    def evaluate(self, row):
        """
        Evaluate row with condition
        """

        return self.operator(row[self.attr], self.value)
