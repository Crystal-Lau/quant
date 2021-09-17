import pandas as pd
import pdb


# 有缺陷，20日均线和60日均线是事先写在excel中的
def over_ma(df, *args):
    for idx in range(df.shape[0]):
        if idx <= args[0]:
            continue
        elif df.loc[idx, "close"] >= df.loc[idx, "mean60"] \
                and df.loc[idx-1, "close"] <= df.loc[idx-1, "mean60"]:
            print(args[0], ":", df.loc[idx, "date"])
        # if df.loc[idx, "close"] >= df.loc[idx, "mean60"] \
        #         and df.loc[idx-1, "close"] <= df.loc[idx-1, "mean60"]:
        #     print(args[1], ":", df.loc[idx, "date"])

def main():
    # 研究上证指数有多少次站上20日均线，60日均线
    df = pd.read_excel("../data/index/000001.xlsx", sheet_name=0)
    over_ma(df, 60)  # 按照由小到大顺序传入2nd, 3rd...参数

if __name__ == "__main__":
    main()