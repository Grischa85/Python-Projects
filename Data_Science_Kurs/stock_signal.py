import matplotlib.pyplot as plt
import yfinance as yf
import talib
from tensorflow import keras
from tensorflow.keras import layers

plt.style.use("seaborn")

'''Aktiensymbol eingeben, periode oder interval nach belieben einstellen'''
company = 'MX'
stock = yf.download({company}, period='3y', interval='1d')
close = stock['Adj Close']
date = stock.index[:]
rsi = close, date
RSI = talib.RSI(close)
k, d = talib.STOCH(RSI, RSI, RSI)
ema50 = talib.EMA(close, timeperiod=50)
ema200 = talib.EMA(close, timeperiod=200)
stock['RSI'] = RSI
stock['STOCH_k'] = k
stock['EMA50'] = ema50
stock['EMA200'] = ema200

'''Parameter oder Kriterien eingeben nach denen gesucht werden soll'''
stock['Signal'] = (stock['EMA50'] > (stock['EMA200']))

stock = stock[199:]

'''X = Input der vorher bestimmten daten. Y = Output der ergebnisse.'''
X = stock[['Adj Close', 'RSI', 'STOCH_k', 'EMA50', 'EMA200']].values
y = stock['Signal']

'''DL model'''
model = keras.Sequential([
    keras.Input(shape=(5,)),
    layers.Dense(1024, name='hidden', activation='relu'),
    layers.Dense(1, name='neuron', activation='sigmoid')])

model.load_weights('model_saved/')
model.compile(
    optimizer=keras.optimizers.RMSprop(),
    loss=keras.losses.BinaryCrossentropy()
)
'''sehr gute einstellungen: pred = model.fit(X, y, batch_size=10, epochs=60)'''
pred = model.fit(X, y, batch_size=25, epochs=6)

model.predict(X)

stock['Chance %'] = model.predict(X)
model.save_weights('model_saved/')

fig, ax = plt.subplots()
ax.set_title(f"{company}")
ax.plot(stock['Adj Close'])
ax.plot(ema50)
ax.plot(ema200)
plt.show()
