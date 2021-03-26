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
    page_date = dt.date.today() + dt.timedelta(-1)
    rs_count = []
    try:
        base_url = base_url % (page, page_date)
        print(base_url + urlencode(params))
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            rs_count = parse_rzrq_data_count(response, source)
    except RequestException:
        rs_count = []
    rs = []
    print(rs_count)
    if rs_count is not None:
        for i in range(rs_count[0]):
            base_url = spcon.RZRQ[source]['url']
            base_url = base_url % (i+1, page_date)
            print(base_url)
            response = requests.get(base_url + urlencode(params), headers=headers)
            if response.status_code == 200:
                rzrqs = parse_rzrq_data(response, source)
            if rzrqs is None:
                return None
            rs.extend(rzrqs)
    return rs


def parse_rzrq_data_count(response, source):
    """
        解析融资融券的股票列表页数
    Parameters
    response : 网络响应
    source : eastmoney（东方财富）
    Return
    --------
     """
    rzrqs_pages = []
    # eastmoney（东方财富）
    if source == 'eastmoney':
        try:
            rs = response.json().get('result')
            rzrqs_pages.append(rs.get('pages'))
            rzrqs_pages.append(rs.get('count'))
        except Exception as e:
            return None
    return rzrqs_pages


def parse_rzrq_data(response,source):
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
                    data['symbol'] = rzrq[i].get('SCODE')
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
    rs = get_rzrq_stocks('eastmoney')
    print(len(rs))
    #rs = get_stock_rzrq('000070', 'eastmoney')
    #print(rs)