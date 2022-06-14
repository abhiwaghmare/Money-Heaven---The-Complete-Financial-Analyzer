import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
print(pdr.get_data_yahoo("BTC-USD", period="5y"))