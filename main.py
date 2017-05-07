from models.brain import Brain
from simulators.stock_market.trader import Trader


if __name__ == "__main__":
    for _ in range(10000):
        trader = Trader()
        brain = Brain(trader.actions, trader.data)
        brain.run_simulation()
        final_value = trader.get_current_value(trader.data[-1]['price'])
        if final_value > trader.current_best:
            neurons = [str(neuron) for neuron in brain.neurons]
            trader.update_results(neurons, final_value)
