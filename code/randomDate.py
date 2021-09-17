import pandas as pd
import random
import pdb

df = pd.read_excel("data/index/000001.xlsx")
result = pd.read_excel("data/results/pearson.xlsx", index_col="ID")
l = [random.randint(1,3667) for i in range(10)]
l.sort()
for i in l:
    start = df.loc[i+1,"date"].strftime("%Y-%m-%d")
    end = df.loc[i+23,"date"].strftime("%Y-%m-%d")
    profit = df.loc[i+23, "close"] / df.loc[i+23, "close"]
    print(i, start+"~"+end)
# print(result.loc[l:,["1","2","3","4"]])