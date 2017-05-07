from models.brain import Brain
from poloniex.trader import Trader
from scripts.tickers import get_tickers


def run_poloniex_trader():
    """
    Analyze Ethereum prices
    """

    trader = Trader('BTC_ETH')
    brain = Brain(trader.actions, trader.data)
    brain.run_simulation()
    final_value = trader.get_current_value(trader.data[-1]['close'])
    if final_value > trader.current_best:
        neurons = [str(neuron) for neuron in brain.neurons]
        trader.update_results(neurons, final_value)


if __name__ == "__main__":

    for ticker in get_tickers():
        print(ticker)

    for _ in range(100):
        run_poloniex_trader()
