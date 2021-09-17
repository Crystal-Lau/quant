# 计算各个均线单独作为买卖交易原则的收益率
import pandas as pd
import numpy as np
import pdb

def computeProfit(df, aver):
    buy_date, pre_close, df.profit = 0, 0, np.nan
    for i in df.index:
        if i < aver:
            continue
        df.loc[i, "mean"] = df.loc[i-aver:i,"close"].mean()
        if buy_date == 0 and df.loc[i, "close"] >= df.loc[i, "mean"] \
            and df.loc[i-1, "mean"] <= df.loc[i, "mean"]:
            buy_date, pre_close = i, df.loc[i, "close"]
        elif buy_date > 0 and df.loc[i, "close"] <= df.loc[i, "mean"]:
            df.loc[i, "profit"] = round((df.loc[i, "close"] / pre_close - 1), 6)
            buy_date = 0
    profit = df[df.profit.notnull()].profit  # 到2020-3-20是442次交易，注意index重排了
    total = 1
    for i in profit.index:
        total *= (profit[i] + 1)
    print(aver, profit.shape, round(total, 4), round(total**(1/15), 6))
    return total


df = pd.read_excel("data/index/000001.xlsx", sheet_name=0)
# 5日线在15年的收益：走到最后交易了442笔，利率4.1034，年化收益率1.098692
# computeProfit(df, 4)
# 20日线在15年的收益：走到最后交易了163笔，利率10.4339，年化收益率1.169221
# computeProfit(df, 19)
# 60日线在15年的收益：走到最后交易了83笔，利率8.0604，年化收益率1.149274
# computeProfit(df, 59)

max, max_date = 0, 0
for i in range(1, 100):
    tmp = computeProfit(df, i)
    if tmp > max:
        max, max_date = tmp, i
print("最大收益N日线的N = %d，15年收益 = %.4f，年化收益率 = %.4f" % (max_date, max, max**(1/15)))