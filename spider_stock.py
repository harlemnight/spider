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
# https://blog.csdn.net/yxStory/article/details/78085444
# https://www.cnblogs.com/chaihy/p/10149222.html
# https://www.jb51.net/article/135952.htm
# https://blog.csdn.net/taichitaichi/article/details/104240239
# https://www.jianshu.com/p/cfb48170c0a5
# https://zhuanlan.zhihu.com/p/26361809


def get_stocks():
    """
        获取所有股票的代码和名称
    Parameters
    security_type : stock(股票)
    source : netease(网易)， eastmoney（东方财富），10jqka（同花顺）
    Return
    --------
    """
    source = spcon.SECURITY_SOURCE[spcon.SECURITY_SOURCE_IDX]
    base_url = spcon.SECURITY['stock'][source]['url']
    params = spcon.SECURITY['stock'][source]['params']
    headers = spcon.SECURITY['stock'][source]['headers']
    try:
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_stocks_data(response, 'stock', source)
    except RequestException:
        return None


def get_batch_current_price(security_type):
    """
        批量获取当日股票，期货，指数收盘行情
    Parameters
    security_type : stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），
            fjb（分级B），fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）,
            bond_fund（债券基金）, stock_fund（股票型基金）, QDII_fund（QDII 基金）,
            money_market_fund（场外交易的货币基金）, mixture_fund（混合型基金）, options(期权)
    source : netease(网易)， eastmoney（东方财富），10jqka（同花顺）
    Return
    --------
    """
    source = spcon.CURRENT_PRICE_SOURCE[spcon.CURRENT_PRICE_SOURCE_IDX]
    base_url = spcon.CURRENT_PRICE[security_type][source]['url']
    params = spcon.CURRENT_PRICE[security_type][source]['params']
    headers = spcon.CURRENT_PRICE[security_type][source]['headers']
    try:
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_batch_current_price_data(response, security_type, source)
    except RequestException:
        return None


def get_history_price(security_type, symbol, start_date, end_date):
    """
       获取相应时间的所有股票、基金、指数、期货的历史行情,
       主要是在第一次初始化金额的时候调用，后期为补偿业务，例如漏了某一天的行情数据，
       则使用此方法
    Parameters
    security_type : stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），
            fjb（分级B），fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）,
            bond_fund（债券基金）, stock_fund（股票型基金）, QDII_fund（QDII 基金）,
            money_market_fund（场外交易的货币基金）, mixture_fund（混合型基金）, options(期权)
    symbol : 0000001(平安银行)
    start : 19900101(YYYYMMDD)
    end   : 20200807(YYYYMMDD)
    source : neteasy_html(网易页面), neteasy_csv(网易CSV下载)
    Return
    --------
     """
    source = spcon.HISTORY_PRICE_SOURCE[spcon.HISTORY_PRICE_SOURCE_IDX]
    base_url = spcon.HISTORY_PRICE[security_type][source]['url']
    params = spcon.HISTORY_PRICE[security_type][source]['params']
    headers = spcon.HISTORY_PRICE[security_type][source]['headers']
    # str to dict
    params = ast.literal_eval(str(params) % (symbol, start_date, end_date))
    try:
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_history_price_data(response, security_type, source)
    except RequestException:
        return None


def parse_history_price_data(response, security_type, source):
    """
        根据不同的网络源处理抓取的标的历史交易明细数据
    Parameters
    response : 网络响应
    security_type : stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），
            fjb（分级B），fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）,
            bond_fund（债券基金）, stock_fund（股票型基金）, QDII_fund（QDII 基金）,
            money_market_fund（场外交易的货币基金）, mixture_fund（混合型基金）, options(期权)
    source : neteasy_csv(网易CSV下载),neteasy_html(网易页面)
    Return
    --------
     """
    rs = []
    # neteasy_csv(网易CSV下载)
    if source == spcon.HISTORY_PRICE_SOURCE[0] and security_type == 'stock':
        items = response.text.split('\r\n')
        # 去掉头标题和尾部空行
        for item in items[1:len(items)-1]:
            data = {}
            data['trade_date'] = item.split(',')[0]
            data['symbol'] = item.split(',')[1].replace("'", "")
            data['symbol_name'] = item.split(',')[2]
            data['close'] = item.split(',')[3]
            data['high'] = item.split(',')[4]
            data['low'] = item.split(',')[5]
            data['open'] = item.split(',')[6]
            data['pre_close'] = item.split(',')[7]
            data['change_amount'] = item.split(',')[8].replace("None", "0")
            data['change_rate'] = item.split(',')[9].replace("None", "0")
            data['amplitude'] = 0
            data['turnover'] = item.split(',')[10].replace("None", "0")
            data['volume'] = item.split(',')[11]
            data['money'] = item.split(',')[12]
            data['total_market'] = item.split(',')[13]
            data['circulate_market'] = item.split(',')[14]
            rs.append(data)
    return rs


def parse_batch_current_price_data(response, security_type, source):
    """
        解析当前股票行情
    Parameters
    response : 网络响应
    security_type : stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），
            fjb（分级B），fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）,
            bond_fund（债券基金）, stock_fund（股票型基金）, QDII_fund（QDII 基金）,
            money_market_fund（场外交易的货币基金）, mixture_fund（混合型基金）, options(期权)
    source : eastmoney（东方财富），netease(网易)， 10jqka（同花顺）
    Return
    --------
     """
    rs = []
    # eastmoney（东方财富）
    if source == spcon.CURRENT_PRICE_SOURCE[0] and security_type == 'stock':
        items = response.json().get('data').get('diff')
        today = dt.datetime.now().strftime('%Y%m%d')
        for i in range(len(items)):
            data = {}
            data['trade_date'] = today
            data['symbol'] = items[i].get('f12')
            data['symbol_name'] = items[i].get('f14')
            data['close'] = items[i].get('f2')
            data['high'] = items[i].get('f15')
            data['low'] = items[i].get('f16')
            data['open'] = items[i].get('f17')
            data['pre_close'] = items[i].get('f18')
            data['change_amount'] = items[i].get('f4')
            data['change_rate'] = items[i].get('f3')
            data['amplitude'] = items[i].get('f7')
            data['turnover'] = items[i].get('f8')
            data['volume'] = items[i].get('f5')
            data['money'] = items[i].get('f6')
            data['total_market'] = items[i].get('f20')
            data['circulate_market'] = items[i].get('f21')
            data['syldt'] = items[i].get('f9')
            data['sjl'] = items[i].get('f23')
            rs.append(data)
    return rs


def parse_stocks_data(response, security_type, source):
    """
        根据不同的网络源处理抓取的标的数据
    Parameters
    response : 网络响应
    security_type : stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），
            fjb（分级B），fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）,
            bond_fund（债券基金）, stock_fund（股票型基金）, QDII_fund（QDII 基金）,
            money_market_fund（场外交易的货币基金）, mixture_fund（混合型基金）, options(期权)
    source : eastmoney（东方财富），netease(网易)， 10jqka（同花顺）
    Return
    --------
     """
    rs = []
    # eastmoney（东方财富）
    if source == spcon.SECURITY_SOURCE[0]:
        items = response.json().get('data').get('diff')
        for i in range(len(items)):
            data = {}
            data['type'] = security_type
            data['symbol'] = items[i].get('f12')
            data['symbol_name'] = items[i].get('f14')
            data['syldt'] = items[i].get('f9')
            data['sjl'] = items[i].get('f23')
            rs.append(data)
    # netease(网易)
    if source == spcon.SECURITY_SOURCE[1]:
        items = response.json().get('list')
        for item in items:
            data = {}
            data['type'] = security_type
            data['symbol'] = item.get('SYMBOL')
            data['symbol_name'] = item.get('SNAME')
            rs.append(data)
    return rs


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
            rs.append(data)
    return rs


def get_concepts(source):
    """
        获取概念列表
        Parameters
        source : 10jqka(同花顺)
        Return
    --------
    """
    source = spcon.CONCEPTS_SOURCE[spcon.CONCEPTS_SOURCE_IDX]
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
    source : 10jqka（同花顺）
    Return
    --------
     """
    rs = []
    # 10jqka(同花顺)
    if source == spcon.CONCEPTS_SOURCE[0]:
        return_html = etree.HTML(response.text)
        result = return_html.xpath('//div[@class="cate_items"]/a')
        pattern = re.compile(r'\d{6}')
        for a in result:
            data = {}
            concept_dm = re.findall(pattern, a.attrib.get('href'))[0]
            data['concept_dm'] = concept_dm
            data['concept_name'] = a.text
            rs.append(data)
    return rs


def get_concept_stocks(concept_dm):
    """
        获取概念成份股
        Parameters
        source : 10jqka(同花顺)
        Return
    --------
    """
    #由于同花顺使用了实时更新cookie暂只能通过无头浏览器每次获取页面数据
    #由于使用浏览器避免每次请求都打开浏览器
    #因为多次握手浏览器会自动设置cookie如果实时更新cookie那么删除上一次的cookie就行了
    #具体情况具体分析
    source = spcon.CONCEPT_STOCKS_SOURCE[spcon.CONCEPT_STOCKS_SOURCE_IDX]
    #user_agent = spcon.USER_AGENT
    chrome_options = Options()
    #chrome_options.add_argument('User-Agent='+user_agent)
    chrome_options.add_argument('headless')#隐藏UI
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


def parse_concept_stocks_data(response_text, concept_dm, source):
    """
        解析股票概念成份股
    Parameters
    response : 网络响应
    source : 10jqka（同花顺）
    Return
    --------
     """
    rs = []
    # 10jqka(同花顺)
    if source == spcon.CONCEPT_STOCKS_SOURCE[0]:
        return_html = etree.HTML(response_text)
        tr_html = return_html.xpath('//tbody/tr')
        for tr in tr_html:
            symbol = tr.xpath('./td/a/text()')
            if symbol:
                rs.append(dict(zip(['concept_dm', 'symbol'], [concept_dm, symbol[0]])))
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
    rs = get_concept_stocks('300008')
    print(rs)
    print(len(rs))