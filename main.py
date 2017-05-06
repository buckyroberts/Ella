from models.action import Action
from models.condition import Condition
from models.neuron import Neuron
from simulator.trader import Trader


def create_brain(actions, data):
    """
    Create neurons (one for each action)
    """

    actions = [Action(name, event) for name, event in actions.items()]
    brain = create_neurons(actions, data)
    run_simulation(brain, data)


def create_neurons(actions, data):
    """
    For each action, create a neuron with a random condition
    """

    return [Neuron(action, Condition(data)) for action in actions]


def run_simulation(brain, data):
    """
    Analyze data with brain
    """

    for neuron in brain:
        print(neuron)

    for row in data:
        print(f"\n{row}")
        for neuron in brain:
            neuron.signal(row)


if __name__ == "__main__":
    trader = Trader()
    create_brain(trader.actions, trader.data)
    print('\nFinal Value:', trader.get_current_value(trader.data[-1]['price']))
