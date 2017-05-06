import random
from operator import gt, lt
from utils.tools import historical_values, operator_str


class Condition:

    def __init__(self, data):
        self.data = data
        self.attribute = self.get_random_attribute()
        self.operator = self.get_random_operator()
        self.value = self.get_random_value()

    def __str__(self):
        return f"{self.attribute} {operator_str(self.operator)} {self.value}"

    def evaluate(self, row):
        """
        Evaluate row with condition
        """

        return self.operator(row[self.attribute], self.value)

    def get_random_attribute(self):
        """
        Random numeric attribute 
        """

        return random.choice([k for k, _ in self.data[0].items() if isinstance(self.data[0][k], (int, float, complex))])

    @staticmethod
    def get_random_operator():
        """
        Random comparison operator
        """

        return random.choice([gt, lt])

    def get_random_value(self):
        """
        Random historical value for attribute
        """

        history = historical_values(self.data)
        return random.choice(list(history[self.attribute]))
