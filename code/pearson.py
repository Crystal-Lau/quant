import math


# 比较一次形态相似度
# Pearson皮尔森相关系数计算
# (∑XY-∑X*∑Y/N)/(Math.sqrt((∑X^2-(∑X)^2/N)*((∑Y^2-(∑Y)^2/N)))
# 以下通用：source是源K线数据，是X；data是对比K线，是是对比字段；

# 子func1: 协方差计算，公式∑XY-∑X*∑Y/N
def calcCovariance(source, data):
    mulTotal = 0     # 计算∑XY
    sourceTotal = 0  # 计算∑X
    dataTotal = 0    # 计算∑Y
    for i in range(len(source)):
        mulTotal += source.iat[i] * data.iat[i]
        sourceTotal += source.iat[i]
        dataTotal += data.iat[i]
    return mulTotal - sourceTotal * dataTotal / len(source)


# 皮尔森分母计算，公式Math.sqrt((∑X^2-(∑X)^2/N)*((∑Y^2-(∑Y)^2/N))
def calcDenominator(source, data):
    sourceSquareAdd = 0  # 计算∑X^2
    sourceAdd = 0        # 计算∑X
    dataSquareAdd = 0    # 计算∑Y^2
    dataAdd = 0          # 计算∑Y
    for i in range(len(source)):
        sourceSquareAdd += source.iat[i] * source.iat[i]
        sourceAdd += source.iat[i]
        dataSquareAdd += data.iat[i] * data.iat[i]
        dataAdd += data.iat[i]
    total = math.sqrt((sourceSquareAdd - sourceAdd * sourceAdd / len(source))\
        * (dataSquareAdd - dataAdd * dataAdd / len(source))) 
    return total
    
def compare(source, data):
    if len(source) != len(data):
        print("length is different!")
    numerator = calcCovariance(source, data)
    denominator = calcDenominator(source, data)
    return numerator / denominator


# 测试
# testSource=[{"value":1},{"value":2},{"value":3}]
# testData=[{"value":3},{"value":2},{"value":1}]
# print(compare(testSource,testData,"value"))

# pandas&&series测试
# import pandas as pd
# testSource = pd.DataFrame([{"value":1},{"value":2},{"value":3}])
# testData = pd.DataFrame([{"value":3},{"value":2},{"value":1}])
# print(compare(testSource.loc[:, "value"], testData.loc[:, "value"]))