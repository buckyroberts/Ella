class Trader:

    def __init__(self):
        self.cash = 1000
        self.portfolio = []
        self.data = [
            {'date': '1/1/17', 'price': 25.48, 'volume': 5500},
            {'date': '1/2/17', 'price': 19.64, 'volume': 1600},
            {'date': '1/3/17', 'price': 25.57, 'volume': 4800},
            {'date': '1/4/17', 'price': 32.63, 'volume': 2100},
            {'date': '1/5/17', 'price': 29.85, 'volume': 3700}
        ]
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
