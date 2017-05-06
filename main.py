from models.brain import Brain
from simulator.trader import Trader


if __name__ == "__main__":
    trader = Trader()
    brain = Brain(trader.actions, trader.data)
    brain.run_simulation()
    print('\nFinal Value:', trader.get_current_value(trader.data[-1]['price']))
