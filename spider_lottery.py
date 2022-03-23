import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import spider_cons as spcon
from lxml import etree


def get_lottery_list(source,start):
    try:
        base_url = spcon.LOTTERY[source]['url']
        headers = spcon.LOTTERY[source]['headers']
        params = spcon.LOTTERY[source]['params']
        base_url = base_url % start
        response = requests.get(base_url + urlencode(params), headers=headers)
        if response.status_code == 200:
            return parse_lottery_data(response, source)
    except RequestException:
        return None


def parse_lottery_data(response, source):
    if source == '500caipiao':
        return_html = etree.HTML(response.text)
        result = return_html.xpath('//tbody[@id="tdata"]/tr')
        print(result)
        res = []
        for tr in result:
            num = tr.xpath('./td/text()')
            print(num)
            res.append(dict(zip(['ssq','red_v1','red_v2','red_v3','red_v4','red_v5',
                                 'red_v6','blue_v1','blue_v2','jcje','top1','top1_je',
                                 'top2','top2_je','tz_je','rq'],
                                [
                                 num[0], num[1],num[2],num[3],num[4], num[5],num[6],num[7],num[8],
                                 num[9], num[10],num[11],num[12],num[13],num[14],num[15]
                                ]
                                )))
    return res


if __name__ == '__main__':
    rs = get_lottery_list('500caipiao')
