from jqdatasdk import *
import pandas as pd


def get_jqdata_swhy(level):
     rs = get_industries(name=level)
     print(rs)
     dao = rs.to_dict(orient='index')
     print(dao)
     print(dao.keys())

     print(dao.values()[])
     #dao2 = dict(zip(dao.keys(),dao.values()['name']))
     #print(dao2)


if __name__ == '__main__':
    auth('13908366866', '366866')
    rs = get_jqdata_swhy('sw_l1')

    #d = get_industry("600519.XSHG", date=None)
    # print(rs)