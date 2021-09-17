import pandas as pd
import pdb


def calc_boll(df, param):
    # 计算均值、标准差
    for idx in range(df.shape[0]-param):
        df.loc[idx+param, "mean"] = df.loc[idx:idx+param,"close"].mean()
        df.loc[idx+param, "std"] = df.loc[idx:idx+param,"close"].std()
    df.loc[:, "boll_up"] = df.loc[:,"mean"] + df.loc[:, "std"] * 2
    df.loc[:, "boll_down"] = df.loc[:,"mean"] - df.loc[:, "std"] * 2
    tmp = df[(df.close>=df.boll_down) & (df.close<=df.boll_up)]
    print(param, tmp.shape[0] / (df.shape[0] - param))

def main():
    df = pd.read_excel("../data/index/000001.xlsx", sheet_name=0)
    temp = ["open", "high", "low", "volume", "money", "index"]
    df.drop(temp, axis=1, inplace=True)
    for i in range(2, 400):
        calc_boll(df, i)

if __name__ == "__main__":
    main()