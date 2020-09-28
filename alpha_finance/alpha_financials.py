import pandas as pd
alpha_key = "KHJ2YUD1E69AB3QK"

from alpha_vantage.timeseries import TimeSeries
# Your key here
key = alpha_key
ts = TimeSeries(key)
aapl, meta = ts.get_daily(symbol='AAPL')
print(aapl)

the_keys = []
the_values = []
for i in aapl.values():
    for x in i.values():
        for t in i.keys():
            the_keys.append(t)
            the_values.append(x)

the_dates = []
for i in aapl:
    the_dates.append(i)


the_dates
the_keys
the_values

df = pd.DataFrame({"keys": the_keys, "values": the_values})
df.head(100)

df.info()
