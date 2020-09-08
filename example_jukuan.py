from jqdatasdk import *
import requests
import re
from requests.exceptions import RequestException
import time
import json
from lxml import etree
import urllib.request
import lxml as html
from urllib.parse import urlencode
import psycopg2 as pg2
import spider_cons as spcon
from selenium import webdriver
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions
import unittest

def juKuanLogin():
    auth('13908366866', '366866')


def get_Stock(ls_security,ls_start_date,ls_end_date):
    get_price(ls_security,
                start_date=ls_start_date,
                end_date=ls_end_date,
                frequency='daily',
              fields=None,
              skip_paused=False,
              fq='pre',
              fill_paused=True)


def get_one_page(url):
    #如果提取的html出现验证的情况添加headers
    try:
         headers = {
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
             'Accept - Encoding': 'gzip, deflate, br',
             'Accept-Language': 'zh-CN,zh;q=0.9,nb;q=0.8',
             'Cache - Control': 'max - age = 0',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
             'Cookie': '__mta=251442873.1593396666299.1593437467209.1593437479694.7; uuid_n_v=v1; uuid=894C2110B9AD11EA9DFDD3B2EAEB07E5CA4ED479F67F4265BB105B26989042B5; _csrf=a99b0a50172ef2170cc1623ab6766424ab25f98ca525b3ef74b3a5de731a0d22; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593396666; _lxsdk_cuid=172fdd79ce4c8-091e9be2d59403-65141775-100200-172fdd79ce5c8; _lxsdk=894C2110B9AD11EA9DFDD3B2EAEB07E5CA4ED479F67F4265BB105B26989042B5; mojo-uuid=128a005937b3b4616f70d6344e434256; mojo-session-id={"id":"ebf62f3c07b4457e0c947ac2c2bb237a","time":1593437147542}; mojo-trace-id=10; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593437479; _lxsdk_s=1730041523c-4b-faa-992%7C%7C14'
         }
         response = requests.get(url, headers=headers)
         if response.status_code == 200:
             #print(response.text)
             return response.text
         return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                         '(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
                         '(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
             'index': item[0],
             'image': item[1],
             'title': item[2],
             'actor': item[3].strip()[3:],
             'time': item[4].strip()[5:15],
             'score': item[5].strip() + item[6].strip()
         }


def write_to_file(content):
    with open(f'result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


def baidu_search():
    url = 'http://baidu.com/s?wd='
    url_with_query = url + urllib.request.quote('python web')
    page = html.parse(url_with_query)
    # /table/tbody/ chrome检查与lxml table/tr 有区别
    # $x('//div[@id="rs"]/table/tbody/tr/th/a/@href');
    proper_headers = page.xpath('//div[@id="rs"]/table/tr/th/a/@href')
    print(proper_headers)
    proper_headers = page.xpath('//div[@id="rs"]/table/tr/th/a/text()')
    print(proper_headers)


def web_screen_spider():
    chrome_options = Options()
    chrome_options.add_argument(
        'User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/78.0.3904.70 Safari/537.36')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    for i in range(35):
        try:

            # chrome_options.add_argument('Accept=text/html,application/xhtml+xml,application/xml;q=0.9,'
            #                             'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3')
            # chrome_options.add_argument('Accept-Encoding=gzip, deflate')
            # chrome_options.add_argument('Accept-Language=zh-CN,zh;q=0.9,nb;q=0.8')
            # chrome_options.add_argument('Cache-Control=max-age=0')
            # chrome_options.add_argument('Connection=keep-alive')
            # chrome_options.add_argument('Upgrade-Insecure-Requests=1')

            #chrome_options.add_argument('headless')
            # 规避检测
            #option = ChromeOptions()
            #option.add_experimental_option('excludeSwitches', ['enable-automation'])
            # driver = webdriver.Chrome(chrome_options=chrome_options, options=option)

            url = "http://q.10jqka.com.cn/gn/detail/field/264648/page/%s/ajax/1/code/300008"
            m = int(i+1)

            driver.delete_all_cookies()
            driver.get(url % m)
            cookie = driver.get_cookie(name='v')
            print(cookie)
            time.sleep(1)
        except Exception as e:
            driver.execute_script('window.stop()')
    driver.quit()


def maoyan_example():
    for i in range(10):
        main(i*10)
        time.sleep(1)


def great_html_sample():
    text = '''
    <div>
    <ul>
    <li class="item-0"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-inactive"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
    <li class="li li-first"><a href＝"link.html">six item</a></li>
    <li class ="li li-first" name="item" ><a href="link.html" >seven item</a></li>
    </ul>
    </div>
    '''
    return text


def parse_sample_html():
    text = great_html_sample()
    #test_html = etree.parse('test.html', etree.HTMLParser())
    #print(etree.tostring(test_html))
    sample_html = etree.HTML(text)
    result = etree.tostring(sample_html)
    print(result.decode('utf-8'))
    #//li/a[@href="link3.html"]/../@class 通过属性找节点的父节点的属性
    #//li[@class="item-inactive"]/a/text() 通过属性找节点的某节点的文本
    #属性多个值情况
    #//li[contains(@class ,"li")]/a/text()
    #多属性
    #//li[contains(@class ,"li") and @name="item" ]/a/text()
    #按序列位置节点
    #//li[1]/a/text()
    #//li[last()-2]/a/text()
    #//li[position()<3]/a/text()
    #节点轴获取上下级节点
    #//li[1]/ancestor::*|div 所有父级或div
    #//li[1]/attribute::* 所有属性
    #//li[1]/child::a[@href="linkl.html"]  child所有直接子节点限定a的属性为
    #//li[l]/descendant::span  descendant所有子孙节点限定span
    #//li[1]/following::*[2] 当前节点之后的所有节点 把子孙节点和同级节点并列计算
    #//li[1]/following-sibling::* 取当前节点之后的所有同级节点
    result = sample_html.xpath('//li[1]/following-sibling::*')
    print(result)
    #print(result[0])


def jqka10(url):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,nb;q=0.8',
            'Cache - Control': 'max - age = 0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'Cookie': '__mta=251442873.1593396666299.1593437467209.1593437479694.7; uuid_n_v=v1; uuid=894C2110B9AD11EA9DFDD3B2EAEB07E5CA4ED479F67F4265BB105B26989042B5; _csrf=a99b0a50172ef2170cc1623ab6766424ab25f98ca525b3ef74b3a5de731a0d22; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593396666; _lxsdk_cuid=172fdd79ce4c8-091e9be2d59403-65141775-100200-172fdd79ce5c8; _lxsdk=894C2110B9AD11EA9DFDD3B2EAEB07E5CA4ED479F67F4265BB105B26989042B5; mojo-uuid=128a005937b3b4616f70d6344e434256; mojo-session-id={"id":"ebf62f3c07b4457e0c947ac2c2bb237a","time":1593437147542}; mojo-trace-id=10; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593437479; _lxsdk_s=1730041523c-4b-faa-992%7C%7C14'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.text)
            return response.text
        return None
    except RequestException:
        return None


def get_cook():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/78.0.3904.70 Safari/537.36'}
    url = 'http://q.10jqka.com.cn/gn/detail/field/264648/page/1/ajax/1/code/300800'
    session = requests.session()
    response = session.get(url, headers=headers)
    cookie = response.headers
    print(cookie)


from http import cookiejar
import urllib.parse
import urllib.request
def get_cook2():
    loginUrl = "http://q.10jqka.com.cn/gn/detail/field/264648/page/1/ajax/1/code/300800";
    # 通过cookieJar（）类构建一个cookieJar（）对象，用来保存cookie的值

    cookie = cookiejar.CookieJar()

    # 通过HTTPCookieProcessor（）处理器类构建一个处理器对象，用来处理cookie
    # 参数就是构建的CookieJar（）对象
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

    # 构建一个自定义的opener
    opener = urllib.request.build_opener(cookie_handler)

    # 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
    opener.addhandlers = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                         "Chrome/78.0.3904.70 Safari/537.36")]
    # 人人网的登陆接口
    url = loginUrl
    # 需要登陆的账户密码
    # 通过URL encode（）编码转换
    request = urllib.request.Request(url)
    response = opener.open(request)
    print(response.headers)


def req_cooke():
    login_url = 'http://q.10jqka.com.cn/gn'
    headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,' \
         'application/signed-exchange;v=b3'
    }
    res = requests.get(url=login_url, headers=headers)
    cookies = res.cookies
    print(cookies)
    cookie = requests.utils.dict_from_cookiejar(cookies)
    print(cookie)


if __name__ == '__main__':
    # juKuanLogin()
    # is_auth = is_auth()
    web_screen_spider()
    #get_cook2()
    #req_cooke()
    # res = get_all_securities(types=[], date=None)
    # print(res)
    # stocks = get_index_stocks('000300.XSHG')
    # print(stocks)
    # margincash_stocks = get_margincash_stocks()
    # print(margincash_stocks)
    # print(get_query_count())
    # print(get_index_weights('000300.XSHG', date=None))
    # rs = get_price('000001.XSHE', start_date='1990-01-01', end_date='2020-07-09', frequency='daily',
    #                fields=['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused', 'open_interest']
     #               )
    # print(rs)
    # maoyan_example()
    # parse_sample_html()
    # http://stockpage.10jqka.com.cn/002163/
    # http://q.10jqka.com.cn/
    # result_html = jqka10('http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/')
    # print(result_html)