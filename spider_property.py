import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import spider_cons as spcon
import ast
from lxml import etree
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_industry_stocks_count(hy_dm):
    """
            获取行业对应的成份股个数便于处理分页数据
        Parameters
        hy_dm : 申万二级行业 当前
        Return
    --------
    """
    source = spcon.SW_INDUSTRY2_COUNT_SOURCE[spcon.SW_INDUSTRY2_COUNT_SOURCE_IDX]
    base_url = spcon.SW_INDUSTRY2_COUNT[source]['url']
    params = spcon.SW_INDUSTRY2_COUNT[source]['params']
    headers = spcon.SW_INDUSTRY2_COUNT[source]['headers']
    params = ast.literal_eval(str(params) % hy_dm)
    try:
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_industry_stocks_count_data(response, source)
    except RequestException:
        return None
    print('获取行业成份股个数')


def parse_industry_stocks_count_data(response, source):
    """
        解析响应数据返回个数
    Parameters
    response : 网络响应
    source : sina（新浪）
    hy_dm : 申万二级行业标准代码
    Return
    --------
     """
    rs = None
    # sina(新浪)
    if source == spcon.SW_INDUSTRY2_COUNT_SOURCE[0]:
        rs = response.text
    return rs


def get_industry_stocks(hy_dm):
    """
            获取行业对应的成份股 根据情况分页调用
            Parameters
            hy_dm : 申万二级行业 当前
            Return
    --------
    """
    stock_number = get_industry_stocks_count(hy_dm).replace('"', '')
    source = spcon.SW_INDUSTRY2_SOURCE[spcon.SW_INDUSTRY2_SOURCE_IDX]
    base_url = spcon.SW_INDUSTRY2[source]['url']
    headers = spcon.SW_INDUSTRY2[source]['headers']
    page_size = spcon.SW_INDUSTRY2[source]['params']['num']
    page_count = int(stock_number) // int(page_size) + 1
    rs = []
    if stock_number:
        for i in range(page_count):
            params = spcon.SW_INDUSTRY2[source]['params']
            params = ast.literal_eval(str(params) % (int(i+1), hy_dm))
            print(base_url + urlencode(params))
            try:
                response = requests.get(base_url + urlencode(params), headers=headers)
                if response.status_code == 200:
                    res = parse_industry_stocks_data(response, source, hy_dm)
                    rs.extend(res)
            except RequestException:
                return None
    if int(stock_number) > len(rs):
        return None
    return rs


def parse_industry_stocks_data(response, source, hy_dm):
    """
        根据申万二级行业代码获取成分股
    Parameters
    response : 网络响应
    source : sina（新浪）
    hy_dm : 申万二级行业标准代码
    Return
    --------
     """
    rs = []
    # sina(新浪)
    if source == spcon.SW_INDUSTRY2_SOURCE[0]:
        items = response.json()
        for i in range(len(items)):
            data = {}
            data['hy_dm'] = hy_dm
            data['symbol'] = items[i].get('code')
            data['symbol_name'] = items[i].get('name')
            rs.append(data)
    return rs


def get_concepts(source):
    """
        获取概念列表
        Parameters
        source : 10jqka(同花顺),eastmoney(东财)
        Return
    --------
    """
    base_url = spcon.CONCEPTS[source]['url']
    headers = spcon.CONCEPTS[source]['headers']
    params = spcon.CONCEPTS[source]['params']
    rs = []
    try:
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            rs = parse_concepts_data(response, source)
    except RequestException:
        return None
    return rs


def parse_concepts_data(response, source):
    """
        解析股票概念定义
    Parameters
    response : 网络响应
    source : 10jqka（同花顺）eastmoney(东财)
    Return
    --------
     """
    rs = []
    # 10jqka(同花顺)
    if source == '10jqka':
        return_html = etree.HTML(response.text)
        result = return_html.xpath('//div[@class="cate_items"]/a')
        pattern = re.compile(r'\d{6}')
        for a in result:
            data = {}
            concept_dm = re.findall(pattern, a.attrib.get('href'))[0]
            data['concept_dm'] = concept_dm
            data['concept_name'] = a.text
            rs.append(data)
    # eastmoney(东财)
    else:
        items = response.json().get('data').get('diff')
        for i in range(len(items)):
            data = {}
            data['concept_dm'] = items[i].get('f12')
            data['concept_name'] = items[i].get('f14')
            rs.append(data)
    return rs


def get_concept_stocks(source, concept_dm):
    """
        获取概念成份股
        Parameters
        source : 10jqka(同花顺) eastmoney(东财)
        Return
    --------
    """
    if source == '10jqka':
        # 由于同花顺使用了实时更新cookie暂只能通过无头浏览器每次获取页面数据
        # 由于使用浏览器避免每次请求都打开浏览器
        # 因为多次握手浏览器会自动设置cookie如果实时更新cookie那么删除上一次的cookie就行了
        # 具体情况具体分析
        # user_agent = spcon.USER_AGENT
        chrome_options = Options()
        # chrome_options.add_argument('User-Agent='+user_agent)
        # 隐藏UI
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        base_url = spcon.CONCEPT_STOCKS[source]['url']
        base_url = base_url % (1, concept_dm)
        driver.delete_all_cookies()
        driver.get(base_url)
        page_count = parse_concept_stocks_count_data(driver.page_source, source)
        rs = []
        if page_count:
            for i in range(int(page_count)):
                base_url = spcon.CONCEPT_STOCKS[source]['url']
                base_url = base_url % (int(i + 1), concept_dm)
                driver.delete_all_cookies()
                driver.get(base_url)
                res = parse_concept_stocks_data(driver.page_source, concept_dm, source)
                if res is None:
                    return None
                rs.extend(res)
        driver.quit()
        return rs
    # eastmoney(东财)
    else:
        base_url = spcon.CONCEPT_STOCKS[source]['url']
        headers = spcon.CONCEPT_STOCKS[source]['headers']
        params = spcon.CONCEPT_STOCKS[source]['params']
        base_url  = base_url % concept_dm
        rs = []
        try:
            response = requests.get(base_url + urlencode(params), headers=headers)
            if response.status_code == 200:
                rs = parse_concept_stocks_data(response,concept_dm, source)
        except RequestException:
            return None
        return rs


def parse_concept_stocks_data(response, concept_dm, source):
    """
        解析股票概念成份股
    Parameters
    response : 网络响应
    source : 10jqka（同花顺） eastmoney(东财)
    Return
    --------
     """
    rs = []
    # 10jqka(同花顺)
    if source == '10jqka':
        return_html = etree.HTML(response)
        tr_html = return_html.xpath('//tbody/tr')
        for tr in tr_html:
            symbol = tr.xpath('./td/a/text()')
            if symbol:
                rs.append(dict(zip(['concept_dm', 'symbol'], [concept_dm, symbol[0]])))
    # eastmoney(东财)
    else:
        items = response.json().get('data').get('diff')
        for i in range(len(items)):
            data = {}
            data['concept_dm'] = concept_dm
            data['symbol'] = items[i].get('f12')
            data['symbol_name'] = items[i].get('f14')
            rs.append(data)
    return rs


def parse_concept_stocks_count_data(response_text, source):
    """
        解析概念响应数据
    Parameters
    response : 网络响应
    source : 10jqka（同花顺）
    Return
    --------
     """
    # 10jqka(同花顺)
    if source == spcon.CONCEPT_STOCKS_SOURCE[0]:
        return_html = etree.HTML(response_text)
        page_number = return_html.xpath('//a[@class="changePage" or @class="cur"][last()]/@page')
        rs = page_number[0] if page_number else 1
        return rs


if __name__ == '__main__':
    # 10jqka概念基本被废弃
    # rs = get_concepts('10jqka')
    # rs = get_concepts('eastmoney')
    # print(rs)
    rs = get_concept_stocks('eastmoney', 'BK0490')
    print(rs)