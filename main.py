from models.brain import Brain
from simulators.stock_market.trader import Trader


if __name__ == "__main__":
    trader = Trader()

    print(trader.current_best)

    brain = Brain(trader.actions, trader.data)
    brain.run_simulation()
    trader.write_results([str(neuron) for neuron in brain.neurons])
