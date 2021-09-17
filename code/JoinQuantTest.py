import pdb, json
from jqdatasdk import *
import pandas as pd
from sqlalchemy import create_engine
auth("17262775413", "920905")

print(is_auth())

# 查询当日剩余可调用数据条数
count=get_query_count()
print(count)
# {"total": 1000000,"spare": 996927}

# 获取ETF数据
# engine = create_engine("mysql+pymysql://root:liu920905@localhost/quant?charset=UTF8MB4")
# stock_list = ["510300.XSHG", "510500.XSHG"]
# # p = get_price(stock_list, start_date="2005-01-01", end_date="2020-05-05")
# p = get_price(stock_list, start_date="2005-01-01", end_date="2020-06-30")
# for stock in stock_list:
#     df = p.minor_xs(stock).dropna()
#     df.to_sql(stock, engine, if_exists="append", index_label="date")

# 1.1. 向JoinQuant获取股票所属的行业分类并持久化
import pymysql
connect = pymysql.connect("localhost", "root", "liu920905", "quant")
cursor = connect.cursor()
cursor.execute("SELECT `index` FROM stock;")
result = cursor.fetchall()
stock_codes = [ x[0] for x in result ]
# print(stock_codes)
# f = open("../data/stock/stock_industry.txt", "w")
# stock_industry = get_industry(security=stock_codes)  # 向JoinQuant获取数据
# print(stock_industry, file=f)
# 1.2. 从 data/stock/stock_industry.txt 取得股票所属行业数据

def update_stock_industry(stock_industry):
    # 对每个股票遍历
    for stock in stock_industry:
        stock_dict = stock_industry[stock]
        print(stock_industry[stock])
        params = []
        sql = "UPDATE stock SET "
        # 按照股票是否有对应行业分类设置sql
        if "sw_l1" in stock_dict:
            sql += "sw_l1_code=%s, sw_l1_name=%s, "
            params.extend([
                stock_dict["sw_l1"]["industry_code"], stock_dict["sw_l1"]["industry_name"]
            ])
        if "sw_l2" in stock_dict:
            sql += "sw_l2_code=%s, sw_l2_name=%s, "
            params.extend([
                stock_dict["sw_l2"]["industry_code"], stock_dict["sw_l2"]["industry_name"]
            ])
        if "sw_l3" in stock_dict:
            sql += "sw_l3_code=%s, sw_l3_name=%s, "
            params.extend([
                stock_dict["sw_l3"]["industry_code"], stock_dict["sw_l3"]["industry_name"]
            ])
        if "zjw" in stock_dict:
            sql += "zjw_code=%s, zjw_name=%s, "
            params.extend([
                stock_dict["zjw"]["industry_code"], stock_dict["zjw"]["industry_name"]
            ])
        if "jq_l1" in stock_dict:
            sql += "jq_l1_code=%s, jq_l1_name=%s, "
            params.extend([
                stock_dict["jq_l1"]["industry_code"], stock_dict["jq_l1"]["industry_name"]
            ])
        if "jq_l2" in stock_dict:
            sql += "jq_l2_code=%s, jq_l2_name=%s, "
            params.extend([
                stock_dict["jq_l2"]["industry_code"], stock_dict["jq_l2"]["industry_name"]
            ])
        # 补齐最后的筛选条件
        sql = sql.strip(", ") + " WHERE `index`=%s;"
        params.append(stock)
        print(params)
        try:
            cursor.execute(sql, params)
            connect.commit()
            print("update:", stock)
        except:
            connect.rollback()


def download_stock_concept():
    with open("../data/stock_concept.txt", "w") as f:
        # print("start", stock_codes)
        stock_concept = get_concept(security=stock_codes, date="2014-07-01")
        print(stock_concept, type(stock_concept))
        print(stock_concept, f)


def main():
    # 1. 获取股票对应的行业分类
    # f = open("../data/stock/stock_industry.txt", "r")
    # stock_industry = f.readlines()
    # stock_industry = json.loads(stock_industry[0])  # 这样终于返回正常值了
    # update_stock_industry(stock_industry)
    # 2. 获取股票对应的概念分类
    download_stock_concept()


if __name__ == "__main__":
    main()