import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/index/000001.xlsx")
for i in range(1, len(df.index)):
    df.loc[i, "gain"] = (df.loc[i, "close"] / df.loc[i-1, "close"] - 1) * 100
# print(df.head())
quan = 0.174
print(quan, df.gain.quantile(q=quan))
# df.plot(kind="box", y="gain", )
# plt.xlabel("index")
# plt.ylabel("gain")
# plt.show()
# -1.0004[0.1739,0.174]-0.9994