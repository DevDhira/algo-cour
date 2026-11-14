import ccxt
ex = ccxt.binanceusdm({"enableRateLimit": True})
ex.load_markets()

symbol = "BTC/USDT:USDT"
ticker = ex.fetch_ticker(symbol)
book= ex.fetch_order_book(symbol, limit=20)
candles = ex.fetch_ohlcv(symbol, timeframe="1h", limit=100)
funding = ex.fetch_funding_rate(symbol)

print(funding)