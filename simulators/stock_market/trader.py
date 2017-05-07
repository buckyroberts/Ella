from os.path import dirname, join, realpath
from utils.tools import read_json, write_json


class Trader:

    def __init__(self):
        self.cash = 1000
        self.input_file = join(dirname(realpath(__file__)), 'data/input.json')
        self.output_file = join(dirname(realpath(__file__)), 'data/output.json')
        self.portfolio = []
        self.current_best = self.get_current_best()
        self.data = read_json(self.input_file)
        self.actions = {
            'BUY': lambda stock: self.buy(stock),
            'SELL': lambda stock: self.sell(stock['price'])
        }

    def buy(self, stock):
        """
        Decrease cash and add stock to portfolio
        """

        self.cash -= stock['price']
        self.portfolio.append(stock)

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
        return portfolio_value + self.cash

    def sell(self, last_price):
        """
        Increase cash and remove stock from portfolio
        """

        if len(self.portfolio):
            self.cash += last_price
            self.portfolio.pop()

    def update_results(self, neurons, final_value):
        """
        Write results to JSON file 
        """

        print(
            f"\nNew best: {final_value} "
            f"\nOld best: {self.current_best} "
        )
        self.current_best = final_value
        data = {'neurons': neurons, 'results': final_value}
        write_json(self.output_file, data)
