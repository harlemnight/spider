import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import spider_cons as spcon
import ast
from lxml import etree
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_areas(source):
    """
        获取地域列表
        Parameters
        source : 10jqka(同花顺),eastmoney(东财)
        Return
    --------
    """
    base_url = spcon.AREA[source]['url']
    headers = spcon.AREA[source]['headers']
    params = spcon.AREA[source]['params']
    rs = []
    try:
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            rs = parse_areas_data(response, source)
    except RequestException:
        return None
    return rs


def parse_areas_data(response, source):
    """
        解析股票地域定义
    Parameters
    response : 网络响应
    source : 10jqka（同花顺）eastmoney(东财)
    Return
    --------
     """
    rs = []
    # 10jqka(同花顺)
    if source == 'eastmoney':
        items = response.json().get('data').get('diff')
        for i in range(len(items)):
            data = {}
            data['area_dm'] = items[i].get('f12')
            data['area_name'] = items[i].get('f14')
            rs.append(data)
    return rs


def get_area_stocks(source, concept_dm):
    """
        获取地域成份股
        Parameters
        source : 10jqka(同花顺) eastmoney(东财)
        Return
    --------
    """
    if source == 'eastmoney':
        base_url = spcon.AREA_STOCKS[source]['url']
        headers = spcon.AREA_STOCKS[source]['headers']
        params = spcon.AREA_STOCKS[source]['params']
        base_url  = base_url % concept_dm
        rs = []
        try:
            response = requests.get(base_url + urlencode(params), headers=headers)
            if response.status_code == 200:
                rs = parse_area_stocks_data(response,concept_dm, source)
        except RequestException:
            return None
        return rs


def parse_area_stocks_data(response, concept_dm, source):
    """
        解析股票地域成份股
    Parameters
    response : 网络响应
    source : 10jqka（同花顺） eastmoney(东财)
    Return
    --------
     """
    rs = []
    # 10jqka(同花顺)
    if source == 'eastmoney':
        items = response.json().get('data').get('diff')
        for i in range(len(items)):
            data = {}
            data['area_dm'] = concept_dm
            data['symbol'] = items[i].get('f12')
            data['symbol_name'] = items[i].get('f14')
            rs.append(data)
    return rs


if __name__ == '__main__':
    rs = get_areas('eastmoney')
    print(rs)
    rs = get_area_stocks('eastmoney', 'BK0145')
    print(rs)
