import ccxt
from pprint import pprint
import time

ex = ccxt.binanceusdm({"enableRateLimit": True})


start = time.time()


DURATION = 60   # total run time (1 minute)
INTERVAL = 5


symbols = ["BTC/USDT","ETH/USDT", "XRP/USDT" ]

while time.time() - start < DURATION:


    ex.load_markets()

    t = ex.fetchTickers(symbols)
    funding = ex.fetch_funding_rates(symbols)


    # pprint(funding)


    for symbol, ticker in t.items():
        print(symbol + "\n")

        fun = funding.get(symbol)
        print ("Funding Rate : "+str(fun['fundingRate']))
        print("Last Price :"+ticker['info']['lastPrice'])

        ask = ticker['ask']
        bid = ticker['bid']
        print('Ask :' + str(ask))
        print('Bid :' + str(bid))
        
        print('24h volume :' + str(ticker['baseVolume']))
        print('Market Price :' + str(fun['markPrice']))

        spread     = (ask - bid) if bid and ask else None
        mid_price  = ((bid + ask) / 2) if bid and ask else None
        spread_bps = (spread / mid_price * 10000) if spread is not None and mid_price else None

        print('Spread :' + str(spread))
        print('Mid Price :' + str(mid_price)) 
        print('Spread Bps :' + str(spread_bps)) 
        print ("\n")
        print("-------------------------")

    time.sleep(INTERVAL)

    

