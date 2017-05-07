from models.action import Action
from models.condition import Condition
from models.neuron import Neuron


class Brain:

    def __init__(self, actions, data):
        self.actions = [Action(name, event) for name, event in actions.items()]
        self.data = data
        self.neurons = [Neuron(action, Condition(self.data)) for action in self.actions]

    def run_simulation(self):
        """
        Iterate over the dataset row by row and invoke all action events (fire the neuron) if a condition is met
        """

        for row in self.data:
            for neuron in self.neurons:
                neuron.signal(row)
