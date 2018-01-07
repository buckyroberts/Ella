from models.brain import Brain
from poloniex.trader import Trader
from scripts.market_data import download_market_data
from scripts.tickers import get_tickers

#just checking bro
def run_poloniex_trader(currency_pair):
    """
    Analyze Ethereum prices
    """

    trader = Trader(currency_pair)
    brain = Brain(trader.actions, trader.data)
    brain.run_simulation()
    final_value = trader.get_current_value(trader.data[-1]['close'])
    if final_value > trader.current_best:
        neurons = [str(neuron) for neuron in brain.neurons]
        trader.update_results(neurons, final_value)


if __name__ == "__main__":

    tickers = get_tickers()
    # download_market_data(tickers)

    for ticker in tickers:
        for _ in range(1000):
            run_poloniex_trader(ticker)
