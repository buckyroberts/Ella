from os.path import dirname, join, realpath
from utils.tools import read_json, write_json


class Trader:

    def __init__(self):
        self.cash = 1000
        self.input_file = join(dirname(realpath(__file__)), 'data/input.json')
        self.output_file = join(dirname(realpath(__file__)), 'data/output.json')
        self.portfolio = []
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

        print('BUYING:', stock)
        print('CURRENT:', self.get_current_value(stock['price']))

    @property
    def current_best(self):
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

        if not len(self.portfolio):
            return

        self.cash += last_price
        self.portfolio.pop()

        print('SELLING:', last_price)
        print('CURRENT:', self.get_current_value(last_price))

    def write_results(self, neurons):
        """
        Write results to JSON file 
        """

        data = {
            'neurons': neurons,
            'results': self.get_current_value(self.data[-1]['price'])
        }
        write_json(self.output_file, data)
