from os.path import dirname, join, realpath
from utils.tools import json_to_list


class Trader:

    def __init__(self):
        self.cash = 1000
        self.portfolio = []
        self.data = json_to_list(join(dirname(realpath(__file__)), 'data.json'))
        self.actions = {
            'BUY': lambda stock: self.buy(stock),
            'SELL': lambda stock: self.sell(stock['price'])
        }

    def get_current_value(self, last_price):
        """
        Current value of account
        """

        portfolio_value = len(self.portfolio) * last_price
        return portfolio_value + self.cash

    def buy(self, stock):
        """
        Decrease cash and add stock to portfolio
        """

        self.cash -= stock['price']
        self.portfolio.append(stock)

        print('BUYING:', stock)
        print('CURRENT:', self.get_current_value(stock['price']))

    def sell(self, last_price):
        """
        Increase cash and remove stock from portfolio
        """

        if not len(self.portfolio):
            print('Nothing to sell...')
            return

        self.cash += last_price
        self.portfolio.pop()

        print('SELLING:', last_price)
        print('CURRENT:', self.get_current_value(last_price))
