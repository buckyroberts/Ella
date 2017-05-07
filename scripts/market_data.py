import json
from urllib import parse, request
from utils.tools import write_json


def save_response(ticker, url):
    """
    Request data from API and save response 
    """

    response = request.urlopen(url)
    response_data = response.read()
    write_json(f"poloniex/input/{ticker}.json", json.loads(response_data))


def download_market_data(tickers):
    """
    Download market data for tickers 
    """

    for ticker in tickers:
        url = f"https://poloniex.com/public"
        params = {
            'command': 'returnChartData',
            'currencyPair': ticker,
            'start': 1493669112,
            'end': 9999999999,
            'period': 1800
        }
        query_string = parse.urlencode(params)
        save_response(ticker, f"{url}?{query_string}")
