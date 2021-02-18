from jqdatasdk import *
import pandas as pd


def get_jqdata_swhy(level):
     """
        获取聚宽申万行业代码表
     :param level: 聚宽申万行业1，2，3级 sw_l1,sw_l2,sw_l3
     :return:
     """
     data = get_industries(name=level)
     rs = dict(zip(data.index, data['name']))
     return rs


def get_jqdata_swhy_stocks(hy_dm):
    """
       获取申万行业成份股
    :param level: 聚宽申万行业1，2，3级 sw_l1,sw_l2,sw_l3
    :return:
    """
    stocks = get_industry_stocks(hy_dm)
    return stocks

if __name__ == '__main__':
    auth('13908366866', '366866')
    rs = get_jqdata_swhy('sw_l3')
    print(rs)
    datas = get_jqdata_swhy_stocks('801081')
    print(datas)
    print(len(datas))
    #d = get_industry("600519.XSHG", date=None)
    # print(rs)