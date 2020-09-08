import urllib.request
import requests
from bs4 import BeautifulSoup
from lxml import html

url = 'http://baidu.com/s?wd='
url_with_query = url + urllib.request.quote('python web')
page = urllib.request.urlopen(url_with_query)
page = page.read()
print(page)
page = requests.get(url_with_query)
print(page.status_code)
print(page.content[:20])
print(page.headers)
print(page.cookies.items())
bs = BeautifulSoup(page.content, "lxml")
print(bs.title)
#findAll("span", {"class":{"green", "red"}})
#bsObj = BeautifulSoup(page.content, 'lxml')
#for child in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#    print(child)
print(bs.find_all('a')[0])
header_children = [c for c in bs.head.children]
print(header_children[0:3])

ta_divs = bs.find_all('div', id='rs')
#ta_divs注意返回的是result
for ta in ta_divs:
#ta才是elementTag
#elementTag都可以使用find_all
#不能直接点.直接点.是第一个找到的元素
    for a0 in ta.find_all('a'):
        print(a0.get_text())
        print(a0.get('href'))


# url = 'http://www.pythonscraping.com/pages/page3.html'
# page = requests.get(url)
# print(page.status_code)
# bsObj = BeautifulSoup(page.content, 'lxml')
# for child in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(child)

#/table/tbody/ chrome检查与lxml table/tr 有区别
#$x('//div[@id="rs"]/table/tbody/tr/th/a/@href');
page = html.parse(url_with_query)
proper_headers = page.xpath('//div[@id="rs"]/table/tr/th/a/@href')
proper_headers = page.xpath('//div[@id="rs"]/table/tr/th/a/text()')
print(proper_headers)
# for srchref in ta_divs.tr:
#      link = srchref.a.get_text()
#      print(link)

