from models.brain import Brain
from simulators.poloniex.trader import Trader


def run_poloniex_trader():
    """
    Analyze Ethereum prices
    """

    trader = Trader()
    brain = Brain(trader.actions, trader.data)
    brain.run_simulation()
    final_value = trader.get_current_value(trader.data[-1]['close'])
    if final_value > trader.current_best:
        neurons = [str(neuron) for neuron in brain.neurons]
        trader.update_results(neurons, final_value)


if __name__ == "__main__":
    for _ in range(1000):
        run_poloniex_trader()
