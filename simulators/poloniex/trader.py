from os.path import dirname, join, realpath
from utils.tools import read_json, write_json


class Trader:

    def __init__(self):
        self.input_file = join(dirname(realpath(__file__)), 'data/input.json')
        self.output_file = join(dirname(realpath(__file__)), 'data/output.json')
        self.btc = 10
        self.current_best = self.get_current_best()
        self.data = read_json(self.input_file)
        self.portfolio = []
        self.actions = {
            'BUY': lambda coin: self.buy(coin),
            'SELL': lambda coin: self.sell(coin['close'])
        }

    def buy(self, coin):
        """
        Decrease BTC and add coin to portfolio
        """

        self.btc -= coin['close']
        self.portfolio.append(coin)

    def get_current_best(self):
        """
        Current best results
        """

        data = read_json(self.output_file)
        return data.get('results') if data.get('results') else 0

    def get_current_value(self, last_price):
        """
        Current value of account
        """

        portfolio_value = len(self.portfolio) * last_price
        return portfolio_value + self.btc

    def sell(self, last_price):
        """
        Increase BTC and remove coin from portfolio
        """

        if len(self.portfolio):
            self.btc += last_price
            self.portfolio.pop()

    def update_results(self, neurons, final_value):
        """
        Write results to JSON file 
        """

        print(
            f"\nNeurons: {neurons} "
            f"\nNew best: {final_value} "
            f"\nOld best: {self.current_best} "
        )
        self.current_best = final_value
        data = {'neurons': neurons, 'results': final_value}
        write_json(self.output_file, data)
