import json
from urllib.request import urlopen

response = urlopen('https://poloniex.com/public?command=returnTicker')
response_data = response.read()

for k, _ in json.loads(response_data).items():
    if k[:3] == 'BTC':
        print(k)

if __name__ == "__main__":
    pass
