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


def get_rzrq_stocks(source):
    """
            获取融资融券的股票
        Parameters
        source : eastmoney（东方财富）
        Return
        --------
        """
    base_url = spcon.RZRQ[source]['url']
    headers = spcon.RZRQ[source]['headers']
    params = spcon.RZRQ[source]['params']
    page = 1
    page_date = '2021-3-25'
    page_count = 0
    try:
        base_url = base_url % (page, page_date)
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            page_count =  parse_rzrq_data_count(response, source)
    except RequestException:
        page_count = 0
    if page_count > 0 :
        for i in page_count:



def parse_rzrq_data_count(response, source):
    """
        解析融资融券的股票列表页数
    Parameters
    response : 网络响应
    source : eastmoney（东方财富）
    Return
    --------
     """
    rzrqs_pages = 0
    # eastmoney（东方财富）
    if source == 'eastmoney':
        try:
            rzrqs_pages = response.json().get('result').get('pages')
        except Exception as e:
            return 0
    return rzrqs_pages


def parse_rzrq_data(response, symbol, source):
    """
        解析融资融券的股票列表
    Parameters
    response : 网络响应
    source : eastmoney（东方财富）
    Return
    --------
     """
    rzrqs = []
    # eastmoney（东方财富）
    if source == 'eastmoney':
        try:
            rzrq = response.json().get('result').get('data')
            if rzrq:
                for i in range(len(rzrq)):
                    data = {}
                    data['symbol'] = symbol
                    data['symbol_name'] = rzrq[i].get('SECNAME')
                    rzrqs.append(data)
        except Exception as e:
            return None
    return rzrqs


def get_stock_rzrq(symbol, source):
    """
        获取股票融资融券信息
    Parameters
    source : eastmoney（东方财富）
    Return
    --------
    """
    base_url = spcon.RZRQ_STOCK[source]['url']
    headers = spcon.RZRQ_STOCK[source]['headers']
    params = spcon.RZRQ_STOCK[source]['params']
    try:
        base_url = base_url % symbol
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_stock_rzrq_data(response, symbol, source)
    except RequestException:
        return None


def parse_stock_rzrq_data(response, symbol, source):
    """
        解析股票融资融券信息
    Parameters
    response : 网络响应
    source : eastmoney（东方财富）
    Return
    --------
     """
    rzrqs = []
    # eastmoney（东方财富）
    if source == 'eastmoney':
        try:
            rzrq = response.json().get('result').get('data')
            if rzrq:
                for i in range(len(rzrq)):
                    data = {}
                    data['rq'] = rzrq[i].get('DATE')
                    data['symbol'] = symbol
                    data['symbol_name'] = rzrq[i].get('SECNAME')
                    data['rzye'] = rzrq[i].get('RZYE')
                    data['rqyl'] = rzrq[i].get('RQYL')
                    data['rzrqye'] = rzrq[i].get('RZRQYE')
                    data['rqye'] = rzrq[i].get('RQYE')
                    data['rqmcl'] = rzrq[i].get('RQMCL')
                    data['rzrqyecz'] = rzrq[i].get('RZRQYECZ')
                    data['rzmre'] = rzrq[i].get('RZMRE')
                    data['sz'] = rzrq[i].get('SZ')
                    data['rzyezb'] = rzrq[i].get('RZYEZB')
                    data['rzche'] = rzrq[i].get('RZCHE')
                    data['rzjme'] = rzrq[i].get('RZJME')
                    data['rqchl'] = rzrq[i].get('RQCHL')
                    data['rqjmg'] = rzrq[i].get('RQJMG')
                    data['spj'] = rzrq[i].get('SPJ')
                    data['zdf'] = rzrq[i].get('ZDF')
                    data['rqjmg'] = rzrq[i].get('RQJMG')
                    rzrqs.append(data)
        except Exception as e:
            return None
    return rzrqs


if __name__ == '__main__':
    rs = get_stock_rzrq('000070', 'eastmoney')
    print(rs)