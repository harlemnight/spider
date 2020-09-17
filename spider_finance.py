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


def get_finance_main(symbol, per_symbol):
    """
        获取主要指标
    Parameters
    source : eastmoney（东方财富）
    Return
    --------
    """
    security_type = 'stock'
    source = spcon.FINANCE_MAIN_STOCKS_SOURCE[spcon.FINANCE_MAIN_STOCKS_SOURCE_IDX]
    base_url = spcon.FINANCE_MAIN_STOCKS[security_type][source]['url']
    params = spcon.FINANCE_MAIN_STOCKS[security_type][source]['params']
    headers = spcon.FINANCE_MAIN_STOCKS[security_type][source]['headers']
    try:
        base_url = base_url % per_symbol
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_finance_main_data(response, symbol, per_symbol, source)
    except RequestException:
        return None


def parse_finance_main_data(response, symbol, per_symbol, source):
    """
        解析当前股票行情
    Parameters
    response : 网络响应
    source : eastmoney（东方财富），netease(网易)， 10jqka（同花顺）
    Return
    --------
     """
    finance_mains = []
    # eastmoney（东方财富）
    if source == spcon.FINANCE_MAIN_STOCKS_SOURCE[0]:
        items = response.json()
        j = 0
        for i in range(len(items)):
            data = {}
            data['symbol'] = symbol
            data['rq'] = items[i].get('date')
            data['chzzts'] = items[i].get('chzzts')
            data['gsjlr'] = items[i].get('gsjlr')
            data['gsjlrgdhbzz'] = items[i].get('gsjlrgdhbzz')
            data['gsjlrtbzz'] = items[i].get('gsjlrtbzz')
            data['jbmgsy'] = items[i].get('jbmgsy')
            data['jll'] = items[i].get('jll')
            data['jqjzcsyl'] = items[i].get('jqjzcsyl')
            data['jyxjlyysr'] = items[i].get('jyxjlyysr')
            data['kfjlr'] = items[i].get('kfjlr')
            data['kfjlrgdhbzz'] = items[i].get('kfjlrgdhbzz')
            data['kfjlrtbzz'] = items[i].get('kfjlrtbzz')
            data['kfmgsy'] = items[i].get('kfmgsy')
            data['ldbl'] = items[i].get('ldbl')
            data['ldzczfz'] = items[i].get('ldzczfz')
            data['mggjj'] = items[i].get('mggjj')
            data['mgjyxjl'] = items[i].get('mgjyxjl')
            data['mgjzc'] = items[i].get('mgjzc')
            data['mgwfply'] = items[i].get('mgwfply')
            data['mll'] = items[i].get('mll')
            data['mlr'] = items[i].get('mlr')
            data['sdbl'] = items[i].get('sdbl')
            data['sjsl'] = items[i].get('sjsl')
            data['tbjzcsyl'] = items[i].get('tbjzcsyl')
            data['tbzzcsyl'] = items[i].get('tbzzcsyl')
            data['xsmgsy'] = items[i].get('xsmgsy')
            data['xsxjlyysr'] = items[i].get('xsxjlyysr')
            data['yskyysr'] = items[i].get('yskyysr')
            data['yszkzzts'] = items[i].get('yszkzzts')
            data['yyzsr'] = items[i].get('yyzsr')
            data['yyzsrgdhbzz'] = items[i].get('yyzsrgdhbzz')
            data['yyzsrtbzz'] = items[i].get('yyzsrtbzz')
            data['zcfzl'] = items[i].get('zcfzl')
            data['zzczzy'] = items[i].get('zzczzy')
            finance_mains.append(data)
            if j == 1:
                break
            j = j+1
    return finance_mains


def get_finance_dupont(symbol, per_symbol):
    """
        获取杜邦
    Parameters
    source : eastmoney（东方财富）
    Return
    --------
    """
    security_type = 'stock'
    source = spcon.FINANCE_DUPONT_STOCKS_SOURCE[spcon.FINANCE_DUPONT_STOCKS_SOURCE_IDX]
    base_url = spcon.FINANCE_DUPONT_STOCKS[security_type][source]['url']
    params = spcon.FINANCE_DUPONT_STOCKS[security_type][source]['params']
    headers = spcon.FINANCE_DUPONT_STOCKS[security_type][source]['headers']
    try:
        base_url = base_url % per_symbol
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_finance_dupont_data(response, symbol, per_symbol, source)
    except RequestException:
        return None


def parse_finance_dupont_data(response, symbol, per_symbol, source):
    """
        解析当前股票行情
    Parameters
    response : 网络响应
    source : eastmoney（东方财富），netease(网易)， 10jqka（同花顺）
    Return
    --------
     """
    duponts = []
    # eastmoney（东方财富）
    if source == spcon.FINANCE_DUPONT_STOCKS_SOURCE[0]:
        items = response.json().get('bgq')
        j = 0
        for i in range(len(items)):
            data = {}
            data['symbol'] = symbol
            data['rq'] = items[i].get('date')
            data['cbze'] = items[i].get('cbze')
            data['ch'] = items[i].get('ch')
            data['cqdtfy'] = items[i].get('cqdtfy')
            data['cyzdqtz'] = items[i].get('cyzdqtz')
            data['dysdszc'] = items[i].get('dysdszc')
            data['fldzc'] = items[i].get('fldzc')
            data['fzze'] = items[i].get('fzze')
            data['gdzc'] = items[i].get('gdzc')
            data['glfy'] = items[i].get('glfy')
            data['gsmgsgddjlr'] = items[i].get('gsmgsgddjlr')
            data['gyjzbdsy'] = items[i].get('gyjzbdsy')
            data['hbzj'] = items[i].get('hbzj')
            data['jlr'] = items[i].get('jlr')
            data['jyxjrzc'] = items[i].get('jyxjrzc')
            data['jzcsyl'] = items[i].get('jzcsyl')
            data['kfzc'] = items[i].get('kfzc')
            data['kgcsjrzc'] = items[i].get('kgcsjrzc')
            data['ldzc'] = items[i].get('ldzc')
            data['qjfy'] = items[i].get('qjfy')
            data['qtfldzc'] = items[i].get('qtfldzc')
            data['qtldzc'] = items[i].get('qtldzc')
            data['qtysk'] = items[i].get('qtysk')
            data['qycs'] = items[i].get('qycs')
            data['sdsfy'] = items[i].get('sdsfy')
            data['srze'] = items[i].get('srze')
            data['sy'] = items[i].get('sy')
            data['tzsy'] = items[i].get('tzsy')
            data['tzxfdc'] = items[i].get('tzxfdc')
            data['wxzc'] = items[i].get('wxzc')
            data['xsfy'] = items[i].get('xsfy')
            data['yfzk'] = items[i].get('yfzk')
            data['yszk'] = items[i].get('yszk')
            data['yycb'] = items[i].get('yycb')
            data['yyjlrl'] = items[i].get('yyjlrl')
            data['yysjjfj'] = items[i].get('yysjjfj')
            data['yysr'] = items[i].get('yysr')
            data['yywsr'] = items[i].get('yywsr')
            data['yywzc'] = items[i].get('yywzc')
            data['zcfzl'] = items[i].get('zcfzl')
            data['zcjzss'] = items[i].get('zcjzss')
            data['zcze'] = items[i].get('zcze')
            data['zjgc'] = items[i].get('zjgc')
            data['zzcjll'] = items[i].get('zzcjll')
            data['zzczzl'] = items[i].get('zzczzl')
            duponts.append(data)
            if j == 1:
                break
            j = j+1
    return duponts


if __name__ == '__main__':
    ms = get_finance_main('000505', 'SZ000505')
    #ms = get_finance_dupont('000505', 'SZ000505')
    print(ms)
