from matplotlib import pylab as plt
import pandas as pd

df = pd.read_csv("TGT.csv")
print(df.head())
df['Date'] = pd.to_datetime(df.Date)
mean = df["Close"].mean()

df2 = pd.read_csv("WMT.csv")
print(df2.head())
df2['Date'] = pd.to_datetime(df2.Date)
mean2 = df2["Close"].mean()

plt.figure("Target and Walmart Stock")
plt.plot(df["Date"], df["Close"], 'r-', linewidth=0.6, label="Target Stock Price, mean="+str(mean))
plt.plot(df2["Date"], df2["Close"], 'r-', linewidth=0.6, label="Walmart Stock Price, mean="+str(mean2),color="blue")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
