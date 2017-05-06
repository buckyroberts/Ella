from utils.tools import operator_to_str


class Neuron:

    def __init__(self, action, condition):
        self.action = action
        self.condition = condition

    def __str__(self):
        return f"{self.condition} - {self.action}"

    @staticmethod
    def display_signal(condition, row):
        """
        Display details of row evaluation by condition
        """

        print(
            f"{condition.attribute} "
            f"{row[condition.attribute]} "
            f"{operator_to_str(condition.operator)} "
            f"{condition.value}"
        )

    def signal(self, row):
        """
        Analyze row and invoke action event if condition is met
        """

        if self.condition.evaluate(row):
            self.display_signal(self.condition, row)
            self.action.event(row)
