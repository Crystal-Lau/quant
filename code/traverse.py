from pearson import compare
import pandas as pd
import time
import pdb


# 遍历计算
# 2个属性20ms，最高相似度0.9505
# 600570:600571{position: 20130415, similar: 0.9505145006910938}
duration = 22  # 近多少日的相似K线

# 蛮力遍历
def compareSimilarKViolent(data):
    start = time.time()  # 记录开始时间
    col = ["1", "2", "3", "4", "5"]
    result = pd.DataFrame(columns=col)  # 保存所有日期的pearson结果
    # i 为被对比的起始日期，第一天的不对比，最近的30天也不对比
    for i in range(6, len(data)-30):
        if i % 10 == 1:
            print(i, data.loc[i, "date"])
        sourceData = data.loc[i:i+duration, "close"]  # 按顺序取被对比源, pd.Series
        similar = pd.DataFrame(columns=["date", "result"])
        for j in range(i-5):
            compareData = data.loc[j:j+duration, "close"]  # 按顺序找匹配的对比K线, pd.Series
            cons = compare(sourceData, compareData)
            # 剔除结果太低的
            if cons <= 0.8:
                continue
            # 记录pearson系数
            similar.loc[j, "date"] = data.loc[j, "date"]
            similar.loc[j, "result"] = round(cons, 4)
        if len(similar) == 0:
            continue
        # 排序取前5个
        similar.sort_values(by="result", ascending=False, inplace=True)
        tmp = similar.head(5).reset_index()
        for j in range(len(tmp)):
            d = tmp.loc[j, "date"].strftime("%Y-%m-%d")[0:10]
            result.loc[i, col[j]] = str(d) + "@@" + str(tmp.loc[j, "result"])
    end = time.time()  # 记录结束时间
    result.to_excel("data/results/pearson.xlsx")
    print("All time is %dmins %ds"%( (start-end)/60, (start-end)%60))

index = pd.read_excel("data/index/000001.xlsx")
compareSimilarKViolent(index)