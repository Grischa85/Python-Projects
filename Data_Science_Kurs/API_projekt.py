import pandas_datareader as pdr
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd




ticker = pdr.get_data_yahoo("GAZ.DE", datetime(2020, 10, 1))
ticker = ticker.to_csv('ticker.csv', index=False)
ticker = pd.read_csv('ticker.csv')
print(ticker)

delta = ticker['Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down

ticker['RSI'] = 100 - (100/(1 + rs))

# Skip first 14 days to have real values
ticker = ticker.iloc[14:]


ticker_RSI = ticker['RSI'][-5:]




print(ticker.columns)
fig, (ax1, ax2) = plt.subplots(2)
ax1.get_xaxis().set_visible(False)
fig.suptitle("stock")

ticker['Close'].plot(ax=ax1)
ax1.set_ylabel('Price ($)')
ticker['RSI'].plot(ax=ax2)
ax2.set_ylim(0,100)
ax2.axhline(30, color='r', linestyle='--')
ax2.axhline(70, color='r', linestyle='--')
ax2.set_ylabel('RSI')

plt.show()

ticker_RSI = ticker['RSI'] [-1:]
print(ticker_RSI)
