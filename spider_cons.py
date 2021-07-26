"""
Created on 2020/07/29
@author: HarlemNight
"""

VERSION = '0.0.1'
SAVE_CSV = False
# http头部信息
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,' \
         'image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
ACCEPT_ENCODING = 'gzip, deflate'
ACCEPT_LANGUAGE = 'zh-CN,zh;q=0.9,nb;q=0.8'
CACHE_CONTROL = 'max-age=0'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

CONNECTION = 'keep-alive'
HEADERS = {
    'Accept': ACCEPT,
    'Accept-Encoding': ACCEPT_ENCODING,
    'Accept-Language': ACCEPT_LANGUAGE,
    'Cache-Control': CACHE_CONTROL,
    'User-Agent': USER_AGENT,
    'Connection': CONNECTION
}
# ######################行情基础数据##################################################################################
# 获取平台支持的所有股票、基金、指数、期货代码名称信息
SECURITY_SOURCE_IDX = 0
SECURITY_SOURCE = ['eastmoney', 'neteasy', '10jqka']
SECURITY = {
  'stock': {
    'eastmoney': {
        'url': 'http://push2.eastmoney.com/api/qt/clist/get?',
        'params': {
          'pn': '1',
          'pz': '10000',
          'po': '1',
          'np': '1',
          'fltt': '2',
          'fs': 'm:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23',
          'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,'
                    'f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'
        },
        'headers': HEADERS
    },
    'neteasy': {
        'url': 'http://quotes.money.163.com/hs/service/diyrank.php?',
        'params': {
            'page': '0',
            'query': 'STYPE:EQA',
            'count': '10000',
            'type': 'query'
        },
        'headers': HEADERS
    }
  }
}

############################################################# 获取股票，期货，等的历史行情信息
HISTORY_PRICE_SOURCE_IDX = 0
HISTORY_PRICE_SOURCE = ['neteasy_csv', 'neteasy_html']
HISTORY_PRICE = {
  'stock': {
    'neteasy_csv': {
        'url': 'http://quotes.money.163.com/service/chddata.html?',
        'params': {
            'code': '%s',
            'start': '%s',
            'end': '%s',
            'fields': 'TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        },
        'headers': HEADERS
    },
    # html 未实现
    'neteasy_html': {
        'url': 'http://quotes.money.163.com/trade/lsjysj_%s.html?',
        'params': {
            'year': '%s',
            'season': '%s'
        },
        'headers': HEADERS
    }
  }
}

###################################################### 获取股票，期货，等当日收盘行情信息
CURRENT_PRICE_SOURCE_IDX = 0
CURRENT_PRICE_SOURCE = ['eastmoney']
CURRENT_PRICE = {
  'stock': {
    'eastmoney': {
        'url': 'http://push2.eastmoney.com/api/qt/clist/get?',
        'params': {
          'pn': '1',
          'pz': '10000',
          'po': '1',
          'np': '1',
          'fltt': '2',
          'fs': 'm:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23',
          'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,'
                    'f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'
        },
        'headers': HEADERS
    }
  }
}

######################################################## 获取申万二级行业成份股个数
SW_INDUSTRY2_COUNT_SOURCE_IDX = 0
SW_INDUSTRY2_COUNT_SOURCE = ['sina']
SW_INDUSTRY2_COUNT = {
    'sina': {
        'url': 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?',
        'params': {
          'node': 'sw2_%s'
        },
        'headers': HEADERS
    }

}
# 获取申万二级行业成份股
SW_INDUSTRY2_SOURCE_IDX = 0
SW_INDUSTRY2_SOURCE = ['sina']
SW_INDUSTRY2 = {
    'sina': {
        'url': 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?',
        'params': {
          'page': '%s',
          'num': '100',
          'node': 'sw2_%s'
        },
        'headers': HEADERS
    }
}

########################################################## 获取概念定义
CONCEPTS_SOURCE_IDX = 0
CONCEPTS_SOURCE = ['10jqka']
CONCEPTS = {
    '10jqka': {
        'url': 'http://q.10jqka.com.cn/gn/',
        'params': {
        },
        'headers': HEADERS
    },
    'eastmoney': {
        'url': 'http://push2.eastmoney.com/api/qt/clist/get?',
        'params': {
            'pn': '1',
            'pz': '10000',
            'po': '1',
            'np': '1',
            'fs': 'm:90+t:3+f:!50',
            'fields': 'f12,f14'
        },
        'headers': HEADERS
    }
}
###################################################### 获取概念成分股###########################
CONCEPT_STOCKS = {
    '10jqka': {
        'url': 'http://q.10jqka.com.cn/gn/detail/field/264648/page/%s/ajax/1/code/%s',
        'params': {
        },
        'headers': HEADERS
    },
    'eastmoney': {
            'url': 'http://push2.eastmoney.com/api/qt/clist/get?fs=b:%s&',
            'params': {
                'pn': '1',
                'pz': '10000',
                'po': '1',
                'np': '1',
                'fields': 'f12,f14'
            },
            'headers': HEADERS
        }
}

#####################获取地域信息#############################################
AREA = {
    'eastmoney': {
        'url': 'http://push2.eastmoney.com/api/qt/clist/get?',
        'params': {
            'pn': '1',
            'pz': '10000',
            'po': '1',
            'np': '1',
            'fs': 'm:90+t:1+f:!50',
            'fields': 'f12,f14'
        },
        'headers': HEADERS
    }
}

#####################获取地域信息#############################################
AREA_STOCKS = {
    'eastmoney': {
            'url': 'http://push2.eastmoney.com/api/qt/clist/get?fs=b:%s&',
            'params': {
                'pn': '1',
                'pz': '10000',
                'po': '1',
                'np': '1',
                'fields': 'f12,f14'
            },
            'headers': HEADERS
        }
}





# ######################F10股东研究数据################################################################################
SHAREHOLDERS_STOCKS_SOURCE_IDX = 0
SHAREHOLDERS_STOCKS_SOURCE = ['eastmoney']
SHAREHOLDERS_STOCKS = {
  'stock': {
    'eastmoney': {
        'url': 'http://f10.eastmoney.com/ShareholderResearch/ShareholderResearchAjax?code=%s',
        'params': {
        },
        'headers': HEADERS
    }
  }
}

# ######################F10财务数据主要指标################################################################################
FINANCE_MAIN_STOCKS_SOURCE_IDX = 0
FINANCE_MAIN_STOCKS_SOURCE = ['eastmoney']
FINANCE_MAIN_STOCKS = {
  'stock': {
    'eastmoney': {
        'url': 'http://f10.eastmoney.com/NewFinanceAnalysis/MainTargetAjax?type=0&code=%s',
        'params': {
        },
        'headers': HEADERS
    }
  }
}

# ######################F10财务数据杜邦分析################################################################################
FINANCE_DUPONT_STOCKS_SOURCE_IDX = 0
FINANCE_DUPONT_STOCKS_SOURCE = ['eastmoney']
FINANCE_DUPONT_STOCKS = {
  'stock': {
    'eastmoney': {
        'url': 'http://f10.eastmoney.com/NewFinanceAnalysis/DubangAnalysisAjax?code=%s',
        'params': {
        },
        'headers': HEADERS
    }
  }
}


# ######################融资融券################################################################################
RZRQ = {
    'eastmoney': {
            'url': 'http://datacenter.eastmoney.com/api/data/get?p=%s&filter=(TRADE_MARKET_CODE in ("069001001001",'
                   '"069001001006","069001002001","069001002002","069001002003"))(date=\'%s\')&',
            'params': {
                'type': 'RPTA_WEB_RZRQ_GGMX',
                'sty': 'ALL',
                'st': 'SCODE',
                'sr': '1',
                'p': '1',
                'ps': '10000'
            },
            'headers': HEADERS
        }
}

RZRQ_STOCK = {
    'eastmoney': {
            'url': 'http://datacenter.eastmoney.com/api/data/get?filter=(scode="%s")&',
            'params': {
                'type': 'RPTA_WEB_RZRQ_GGMX',
                'sty': 'ALL',
                'st': 'date',
                'sr': '-1',
                'p': '1',
                'ps': '90'
            },
            'headers': HEADERS
        }
}


#######################沪深股通################################################################################
HSGT_SH = {
    'eastmoney': {
            'url': 'http://push2.eastmoney.com/api/qt/clist/get?',
            'params': {
                'pn': '1',
                'pz': '10000',
                'po': '1',
                'np': '1',
                'fs': 'b:BK0707',
                'fields': 'f12,f14'
            },
            'headers': HEADERS
        }
}

HSGT_SZ = {
    'eastmoney': {
            'url': 'http://push2.eastmoney.com/api/qt/clist/get?',
            'params': {
                'pn': '1',
                'pz': '10000',
                'po': '1',
                'np': '1',
                'fs': 'b:BK0804',
                'fields': 'f12,f14'
            },
            'headers': HEADERS
        }
}

HSGT = {
    'eastmoney': {
            'url': 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?'
                   'filter=(DateType=\'1\' and HdDate=\'%s\')&',
            'params': {
                'token': '894050c76af8597a853f5b408b759f5d',
                'type': 'HSGT20_GGTJ_SUM',
                'st': 'ShareSZ_Chg_One',
                'sr': '-1',
                'p': '1',
                'ps': '10000'
            },
            'headers': HEADERS
        }
}

HSGT_TJ_STOCK = {
    'eastmoney': {
            'url': 'http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?'
                   'filter=(SCODE=\'%s\')&',
            'params': {
                'token': '70f12f2f4f091e459a279469fe49eca5',
                'type': 'HSGTHDSTA',
                'st': 'HDDATE',
                'sr': '-1',
                'p': '1',
                'ps': '10000'
            },
            'headers': HEADERS
        }
}

HSGT_MX_STOCK = {
    'eastmoney': {
            'url': 'http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?'
                   'filter=(SCODE=''%s'')(HDDATE>=^%s^ and HDDATE<=^%s^)&type=%s&',
            'params': {
                'token': '70f12f2f4f091e459a279469fe49eca5',
                'st': 'HDDATE,SHAREHOLDPRICE',
                'sr': '3',
                'p': '1',
                'ps': '100000'
            },
            'headers': HEADERS
        }
}


##-------------------------彩票----------------------------------------------------
#https://zst.aicai.com/ssq
#https://datachart.500.com/ssq/history/history.shtml
LOTTERY = {
    '500caipiao': {
            'url': 'https://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=',
            'params': {
            },
            'headers': HEADERS
        },
    'SINA':{
        'url': 'https://datachart.500.com/ssq/history/newinc/history.php?start=03001&end=21083',
            'params': {
            },
            'headers': HEADERS

    }
}
