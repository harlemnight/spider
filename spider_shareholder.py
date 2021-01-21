import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import spider_cons as spcon
import datetime as dt
import ast
from lxml import etree
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
import time
import urllib.parse
import urllib.request
import urllib.error


def get_shareholders(symbol, per_symbol):
    """
        获取F10股东研究数据,
        1.股东人数情况
        2.实际控制人
        3.10大股东
        4.部分基金持股 以股票角度
    Parameters
    source : eastmoney（东方财富）
    Return
    --------
    """
    security_type = 'stock'
    source = spcon.SHAREHOLDERS_STOCKS_SOURCE[spcon.SHAREHOLDERS_STOCKS_SOURCE_IDX]
    base_url = spcon.SHAREHOLDERS_STOCKS[security_type][source]['url']
    params = spcon.SHAREHOLDERS_STOCKS[security_type][source]['params']
    headers = spcon.SHAREHOLDERS_STOCKS[security_type][source]['headers']
    try:
        base_url = base_url % per_symbol
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_shareholders_data(response, symbol, per_symbol, source)
    except RequestException:
        return None


def parse_shareholders_data(response, symbol, per_symbol, source):
    """
        解析股东信息
    Parameters
    response : 网络响应
    source : eastmoney（东方财富），netease(网易)， 10jqka（同花顺）
    Return
    --------
     """
    kggxs, gdrss, jjcgs, sdgds = [], [], [], []
    # eastmoney（东方财富）
    if source == spcon.SHAREHOLDERS_STOCKS_SOURCE[0]:
        kggx = response.json().get('kggx')
        gdrs = response.json().get('gdrs')
        jjcg = response.json().get('jjcg')
        sdgd = response.json().get('sdgd')
        if kggx:
            data = {}
            data['symbol'] = symbol
            data['sjkzr'] = kggx.get('sjkzr')
            data['cgbl'] = kggx.get('cgbl')
            kggxs.append(data)
        if gdrs:
            for i in range(len(gdrs)):
                data = {}
                data['rq'] = gdrs[i].get('rq')
                data['symbol'] = symbol
                data['cmjzd'] = gdrs[i].get('cmjzd')
                data['gdrs'] = gdrs[i].get('gdrs')
                data['gdrs_jsqbh'] = gdrs[i].get('gdrs_jsqbh')
                data['gj'] = gdrs[i].get('gj')
                data['qsdgdcghj'] = gdrs[i].get('qsdgdcghj')
                data['qsdltgdcghj'] = gdrs[i].get('qsdltgdcghj')
                data['rjcgje'] = gdrs[i].get('rjcgje')
                data['rjltg'] = gdrs[i].get('rjltg')
                data['rjltg_jsqbh'] = gdrs[i].get('rjltg_jsqbh')
                gdrss.append(data)
        if jjcg:
            for i in range(len(jjcg)):
                rq = jjcg[i].get('rq')
                jj = jjcg[i].get('jjcg')
                for i in range(len(jj)):
                    data = {}
                    data['rq'] = rq
                    data['symbol'] = symbol
                    data['jjdm'] = jj[i].get('jjdm')
                    data['jjmc'] = jj[i].get('jjmc')
                    data['cgs'] = jj[i].get('cgs')
                    data['cgsz'] = jj[i].get('cgsz')
                    data['zzgbb'] = jj[i].get('zzgbb')
                    data['zltb'] = jj[i].get('zltb')
                    jjcgs.append(data)
        if sdgd:
            for i in range(len(sdgd)):
                rq = sdgd[i].get('rq')
                gd = sdgd[i].get('sdgd')
                for i in range(len(gd)):
                    data = {}
                    data['rq'] = rq
                    data['symbol'] = symbol
                    data['gdmc'] = gd[i].get('gdmc')
                    data['gflx'] = gd[i].get('gflx')
                    data['cgs'] = gd[i].get('cgs')
                    data['zltgbcgbl'] = gd[i].get('zltgbcgbl')
                    sdgds.append(data)
    return kggxs, gdrss, jjcgs, sdgds


if __name__ == '__main__':
    kggxs, gdrss ,jjcgs, sdgds= get_shareholders('600519', 'SH600519')
    print(kggxs)
    print(gdrss)
    print(jjcgs)
    print(sdgds)