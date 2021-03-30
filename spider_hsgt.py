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


def get_stock_hsgt_tj(symbol, source):
    """
        获取股票沪深股通统计信息
    Parameters
    source : eastmoney（东方财富）
    Return
    --------
    """
    base_url = spcon.HSGT_TJ_STOCK[source]['url']
    headers = spcon.HSGT_TJ_STOCK[source]['headers']
    params = spcon.HSGT_TJ_STOCK[source]['params']
    try:
        base_url = base_url % symbol
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_hsgttj_data(response, symbol, source)
    except RequestException:
        return None


def parse_hsgttj_data(response, symbol, source):
    """
        解析股票沪深股通统计信息
    Parameters
    response : 网络响应
    source : eastmoney（东方财富）
    Return
    --------
     """
    hsgts = []
    # eastmoney（东方财富）
    if source == 'eastmoney':
        hsgt = response.json()
        if hsgt:
            for i in range(len(hsgt)):
                data = {}
                data['rq'] = hsgt[i].get('HDDATE')
                data['symbol'] = symbol
                data['symbol_name'] = hsgt[i].get('SNAME')
                data['shareholdsum'] = hsgt[i].get('SHAREHOLDSUM')
                data['sharesrate'] = hsgt[i].get('SHARESRATE')
                data['closeprice'] = hsgt[i].get('CLOSEPRICE')
                data['zdf'] = hsgt[i].get('ZDF')
                data['shareholdprice'] = hsgt[i].get('SHAREHOLDPRICE')
                data['shareholdpriceone'] = hsgt[i].get('SHAREHOLDPRICEONE')
                data['shareholdpricefive'] = hsgt[i].get('SHAREHOLDPRICEFIVE')
                data['shareholdpriceten'] = hsgt[i].get('SHAREHOLDPRICETEN')
                data['market'] = hsgt[i].get('MARKET')
                data['shareholdsumchg'] = hsgt[i].get('ShareHoldSumChg')
                data['zb'] = hsgt[i].get('Zb')
                data['zzb'] = hsgt[i].get('Zzb')
                hsgts.append(data)
    return hsgts


def get_stock_hsgt_mx(symbol, source, startdate, enddate):
    """
        获取股票沪深股通明细信息
    Parameters
    source : eastmoney（东方财富）
    Return
    --------
    """
    base_url = spcon.HSGT_MX_STOCK[source]['url']
    headers = spcon.HSGT_MX_STOCK[source]['headers']
    params = spcon.HSGT_MX_STOCK[source]['params']
    #不同市场参数type不同
    type_lx = 'HSGTSHHDDET'
    if symbol[0:3] in ['600', '601', '603', '605', '688']:
        type_lx = 'HSGTHHDDET'
    try:
        base_url = base_url % (symbol, startdate, enddate, type_lx)
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_hsgtmx_data(response, symbol, source)
    except RequestException:
        return None


def parse_hsgtmx_data(response, symbol, source):
    """
        解析股票沪深股通明细信息
    Parameters
    response : 网络响应
    source : eastmoney（东方财富）
    Return
    --------
     """
    hsgts = []
    # eastmoney（东方财富）
    if source == 'eastmoney':
        hsgt = response.json()
        if hsgt:
            for i in range(len(hsgt)):
                data = {}
                data['rq'] = hsgt[i].get('HDDATE')
                data['symbol'] = symbol
                data['symbol_name'] = hsgt[i].get('SNAME')
                data['participantcode'] = hsgt[i].get('PARTICIPANTCODE')
                data['participantname'] = hsgt[i].get('PARTICIPANTNAME')
                data['shareholdsum'] = hsgt[i].get('SHAREHOLDSUM')
                data['sharesrate'] = hsgt[i].get('SHARESRATE')
                data['closeprice'] = hsgt[i].get('CLOSEPRICE')
                data['zdf'] = hsgt[i].get('ZDF')
                data['shareholdprice'] = hsgt[i].get('SHAREHOLDPRICE')
                data['shareholdpriceone'] = hsgt[i].get('SHAREHOLDPRICEONE')
                data['shareholdpricefive'] = hsgt[i].get('SHAREHOLDPRICEFIVE')
                data['shareholdpriceten'] = hsgt[i].get('SHAREHOLDPRICETEN')
                data['market'] = hsgt[i].get('MARKET')
                data['shareholdsumchg'] = hsgt[i].get('ShareHoldSumChg')
                data['zb'] = hsgt[i].get('Zb')
                data['zzb'] = hsgt[i].get('Zzb')
                hsgts.append(data)
    return hsgts


if __name__ == '__main__':
    #rs = get_stock_hsgt_tj('600703', 'eastmoney')
    #print(rs)
    rs = get_stock_hsgt_mx('600837', 'eastmoney','2021-03-01','2021-03-30')
    print(rs)