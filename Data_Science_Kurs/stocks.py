import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
import talib


plt.style.use("seaborn")

Company = "BMW.DE"


stock = yf.download(Company, start='2021-1-1', end=datetime.today())
close = stock['Adj Close']
ema50 = talib.EMA(close, timeperiod=50)
ema200 = talib.EMA(close, timeperiod=200)


fig, (ax1, ax2) = plt.subplots(2)
ax1.set_title(f"{Company}")
ax1.plot(stock['Close'])
ax1.plot(ema50)
ax1.plot(ema200)
plt.show()
