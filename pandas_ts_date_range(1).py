# -*- coding: utf-8 -*-
"""pandas_ts_date_range(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hXl0dU3fWWga5Dwbe5fRPbQSFAz_uilT

<h1 style="color:blue;" align="center">Pandas Time Series Analysis : date_range</h1>
"""

import pandas as pd

df = pd.read_csv("DPZ_withoutdate.csv")
df.head()

rng = pd.date_range(start="11/29/2020",end="12/29/2020",freq='B')
rng

# to set the index ... we are using set
df.set_index(rng, inplace=True)
df.head(10)

"""<h3 style="color:purple">Finding missing dates from datetimeindex</h3>"""

daily_index = pd.date_range(start="6/1/2016",end="6/30/2016",freq='D')
daily_index

daily_index.difference(df.index)

"""<h3 style="color:purple">Benefits of having DatetimeIndex</h3>"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
df.Close.plot()

df["2016-06-01":"2016-06-10"].Close.mean()

"""<h3 style="color:purple">asfreq</h3>"""

df.index

df.asfreq('D',method='pad')

df.asfreq('W',method='pad')

df.asfreq('H',method='pad')

"""<h3 style="color:purple"> generating DatetimeIndex with periods argument</h3>"""

rng = pd.date_range('1/1/2011', periods=72, freq='H')
rng

import numpy as np
ts = pd.Series(np.random.randint(0,10,len(rng)), index=rng)
ts.head(20)