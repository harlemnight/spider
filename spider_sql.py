###############################股票###########################################################################
# 标的信息
SQL_DELETE_SECURITY_BY_TYPE = 'delete from  t_china_security_list where type = %(type)s'
SQL_INSERT_SECURITY = 'insert into t_china_security_list(type, symbol_name, symbol,syldt,sjl) values ' \
                      '(%(type)s, %(symbol_name)s, %(symbol)s,%(syldt)s,%(sjl)s)'

# 标的历史行情
SQL_INSERT_STOCK_HISTORY_PRICE = 'insert into t_china_stock_trade_history(trade_date, symbol,symbol_name,close' \
                                 ',high,low ,open,pre_close,change_amount,change_rate,amplitude,turnover,volume,' \
                                 'money,total_market,circulate_market) values (%(trade_date)s,%(symbol)s,' \
                                 '%(symbol_name)s,%(close)s,%(high)s,%(low)s,%(open)s,%(pre_close)s,' \
                                 '%(change_amount)s ,%(change_rate)s,%(amplitude)s,%(turnover)s,%(volume)s,' \
                                 '%(money)s,%(total_market)s,%(circulate_market)s)'
# 标的历史行情的标信息获取网易历史
SQL_GET_STOCK_LIST_NET_EASY = 'select l.symbol,t.market||l.symbol pre_symbol from t_china_security_list l,' \
                         ' t_china_security_market t  ' \
                         'where 1=1 and substr(l.symbol,1,3) = t.pre_symbol and l.type = %(type)s' \
                         ' and not exists (  select null from t_xt_logger_mx mx where mx.symbol = l.symbol' \
                         ' and mx.security_type = %(type)s and mx.operation = \'init_price\' ) '
# 标的当日行情
SQL_INSERT_STOCK_CURRENT_PRICE = 'insert into t_china_stock_trade_current(trade_date, symbol,symbol_name,close,high,' \
                                 'low ,open,pre_close,change_amount,change_rate,amplitude,turnover,volume,money,total' \
                                 '_market,circulate_market,syldt,sjl) values (%(trade_date)s,%(symbol)s,%(symbol_name)s,' \
                                 '%(close)s,%(high)s,%(low)s,%(open)s,%(pre_close)s,%(change_amount)s ,' \
                                 '%(change_rate)s,%(amplitude)s,%(turnover)s,%(volume)s,%(money)s,%(total_market)s,' \
                                 '%(circulate_market)s,%(syldt)s,%(sjl)s)'

# 申万二级行业成分股票
SQL_DELETE_STOCK_INDUSTRY_SW = 'delete from t_china_stock_industry_sw_dzb where hy_dm = %(hy_dm)s'
SQL_INSERT_STOCK_INDUSTRY_SW = 'insert into t_china_stock_industry_sw_dzb(hy_dm, symbol) values (%(hy_dm)s,%(symbol)s)'

# 申万二级行业
SQL_GET_STOCK_INDUSTRY_LIST_SW = 'select hy_dm  From t_china_stock_industry_sw s where lvl = %(lvl)s and not exists ' \
                                 '( select null from t_xt_logger_mx m  where m.security_type = \'stock\'' \
                                 ' and m.symbol = s.hy_dm	and m.operation = \'init_hy\' )  order by 1'

# 同花顺概念定义
SQL_DELETE_CONCEPTS_10JQKA = 'delete from t_china_stock_concept_10jqka'
SQL_INSERT_CONCEPTS_10JQKA = 'insert into t_china_stock_concept_10jqka(concept_dm, concept_name) values ' \
                                       '(%(concept_dm)s,%(concept_name)s)'

# 同花顺概念成分股票
SQL_DELETE_CONCEPT_STOCKS_10JQKA = 'delete from t_china_stock_concept_10jqka_dzb where concept_dm = %(concept_dm)s'
SQL_INSERT_CONCEPT_STOCKS_10JQKA = 'insert into t_china_stock_concept_10jqka_dzb(concept_dm, symbol) values' \
                                  '(%(concept_dm)s,%(symbol)s)'

# 同花顺概念列表
SQL_GET_STOCK_CONCEPTS_10JQKA = 'select concept_dm  From t_china_stock_concept_10jqka s where not exists ' \
                                 '( select null from t_xt_logger_mx m  where m.security_type = \'stock\'' \
                                 ' and m.symbol = s.concept_dm	and m.operation = \'init_concept\' )' \
                                '  order by 1'

# 写日志
SQL_INSERT_XT_LOGGER_MX = 'insert into t_xt_logger_mx (security_type,symbol,operation,status,business, create_date,' \
                       'batch_number,row_number,message ) values(%(security_type)s,%(symbol)s,%(operation)s,' \
                       '%(status)s ,%(business)s,%(create_date)s,%(batch_number)s,%(row_number)s,%(message)s)'

###################################持股信息####################################################
SQL_GET_STOCK_LIST_SHAREHOLDER = 'select l.symbol,t.market_lx||l.symbol pre_symbol from t_china_security_list l,' \
                     ' t_china_security_market t  ' \
                     'where 1=1 and substr(l.symbol,1,3) = t.pre_symbol and l.type = \'stock\'' \
                     ' and not exists (  select null from t_xt_logger_mx mx where mx.symbol = l.symbol' \
                     ' and mx.security_type = \'stock\' and mx.operation = \'init_shareholder\' )'
# 实际控制人
SQL_DELETE_STOCKS_SJKZR = 'delete from t_china_stock_shareholder_sjkzr where symbol = %(symbol)s '
SQL_INSERT_STOCKS_SJKZR = 'insert into t_china_stock_shareholder_sjkzr(symbol, sjkzr, cgbl) values' \
                                  '(%(symbol)s,%(sjkzr)s,%(cgbl)s)'
# 股东人数
SQL_DELETE_STOCKS_GDRS = 'delete from t_china_stock_shareholder_gdrs where symbol = %(symbol)s '
SQL_INSERT_STOCKS_GDRS = 'insert into t_china_stock_shareholder_gdrs(rq,symbol,gdrs,gdrs_jsqbh,cmjzd,gj,rjcgje,rjltg,' \
                         'rjltg_jsqbh,qsdgdcghj,qsdltgdcghj) values (%(rq)s,%(symbol)s,%(gdrs)s,%(gdrs_jsqbh)s,' \
                         '%(cmjzd)s,%(gj)s,%(rjcgje)s,%(rjltg)s,%(rjltg_jsqbh)s,%(qsdgdcghj)s,%(qsdltgdcghj)s)'
# 基金持股
SQL_DELETE_STOCKS_JJCG = 'delete from t_china_stock_shareholder_jjcg where symbol = %(symbol)s '
SQL_INSERT_STOCKS_JJCG = 'insert into t_china_stock_shareholder_jjcg(rq,jjdm,jjmc,cgs,cgsz,zzgbb,zltb,symbol) values' \
                                  '(%(rq)s,%(jjdm)s,%(jjmc)s,%(cgs)s,%(cgsz)s,%(zzgbb)s,%(zltb)s,%(symbol)s)'

# 十大股东
SQL_DELETE_STOCKS_SDGD = 'delete from t_china_stock_shareholder_sdgd where symbol = %(symbol)s '
SQL_INSERT_STOCKS_SDGD = 'insert into t_china_stock_shareholder_sdgd(rq,symbol,gdmc,gflx,cgs,zltgbcgbl) values' \
                                  '(%(rq)s,%(symbol)s,%(gdmc)s,%(gflx)s,%(cgs)s,%(zltgbcgbl)s)'



###################################财务数据####################################################
# 主要指标
SQL_GET_STOCK_LIST_FINANCE_MAIN = 'select l.symbol,t.market_lx||l.symbol pre_symbol from t_china_security_list l,' \
                     ' t_china_security_market t  ' \
                     'where 1=1 and substr(l.symbol,1,3) = t.pre_symbol and l.type = \'stock\'' \
                     ' and not exists (  select null from t_xt_logger_mx mx where mx.symbol = l.symbol' \
                     ' and mx.security_type = \'stock\' and mx.operation = \'init_finance_main\' )'

# 主要指标
SQL_DELETE_STOCKS_FINANCE_MAIN = 'delete from t_china_stock_finance_main where symbol = %(symbol)s '
SQL_INSERT_STOCKS_FINANCE_MAIN = 'INSERT INTO t_china_stock_finance_main(symbol, chzzts, rq, gsjlr, gsjlrgdhbzz,' \
                                 ' gsjlrtbzz, jbmgsy, jll, jqjzcsyl, jyxjlyysr, kfjlr, kfjlrgdhbzz, kfjlrtbzz,' \
                                 ' kfmgsy, ldbl, ldzczfz, mggjj, mgjyxjl, mgjzc, mgwfply, mll, mlr, sdbl, sjsl,' \
                                 ' tbjzcsyl, tbzzcsyl, xsmgsy, xsxjlyysr, yskyysr, yszkzzts, yyzsr, yyzsrgdhbzz,' \
                                 ' yyzsrtbzz, zcfzl, zzczzy) VALUES (%(symbol)s, %(chzzts)s, %(rq)s, %(gsjlr)s,' \
                                 ' %(gsjlrgdhbzz)s, %(gsjlrtbzz)s, %(jbmgsy)s, %(jll)s, %(jqjzcsyl)s, ' \
                                 '%(jyxjlyysr)s, %(kfjlr)s, %(kfjlrgdhbzz)s, %(kfjlrtbzz)s, %(kfmgsy)s,' \
                                 ' %(ldbl)s, %(ldzczfz)s, %(mggjj)s, %(mgjyxjl)s, %(mgjzc)s, %(mgwfply)s,' \
                                 ' %(mll)s, %(mlr)s, %(sdbl)s, %(sjsl)s, %(tbjzcsyl)s, %(tbzzcsyl)s,' \
                                 ' %(xsmgsy)s, %(xsxjlyysr)s, %(yskyysr)s, %(yszkzzts)s, %(yyzsr)s,' \
                                 ' %(yyzsrgdhbzz)s, %(yyzsrtbzz)s, %(zcfzl)s, %(zzczzy)s)'

# 杜邦指标
SQL_GET_STOCK_LIST_FINANCE_DUPONT = 'select l.symbol,t.market_lx||l.symbol pre_symbol from t_china_security_list l,' \
                     ' t_china_security_market t  ' \
                     'where 1=1 and substr(l.symbol,1,3) = t.pre_symbol and l.type = \'stock\'' \
                     ' and not exists (  select null from t_xt_logger_mx mx where mx.symbol = l.symbol' \
                     ' and mx.security_type = \'stock\' and mx.operation = \'init_finance_dupont\' )'
# 杜邦指标
SQL_DELETE_STOCKS_FINANCE_DUPONT = 'delete from t_china_stock_finance_dupont where symbol = %(symbol)s '
SQL_INSERT_STOCKS_FINANCE_DUPONT = 'INSERT INTO t_china_stock_finance_dupont(symbol, rq, cbze, ch, cqdtfy, cqgqtz,' \
                                   ' cwfy, cyzdqtz, dysdszc, fldzc, fzze, gdzc, glfy, gsmgsgddjlr, gyjzbdsy,' \
                                   ' hbzj, jlr, jyxjrzc, jzcsyl, kfzc, kgcsjrzc, ldzc, qjfy, qtfldzc, qtldzc, ' \
                                   'qtysk, qycs, sdsfy, srze, sy, tzsy, tzxfdc, wxzc, xsfy, yfzk, yszk, yycb, ' \
                                   'yyjlrl, yysjjfj, yysr, yywsr, yywzc, zcfzl, zcjzss, zcze, zjgc, zzcjll, ' \
                                   'zzczzl) VALUES (%(symbol)s, %(rq)s, %(cbze)s, %(ch)s, %(cqdtfy)s, %(cqgqtz)s,' \
                                   ' %(cwfy)s, %(cyzdqtz)s, %(dysdszc)s, %(fldzc)s, %(fzze)s, %(gdzc)s, %(glfy)s,' \
                                   ' %(gsmgsgddjlr)s, %(gyjzbdsy)s, %(hbzj)s, %(jlr)s, %(jyxjrzc)s, %(jzcsyl)s,' \
                                   ' %(kfzc)s, %(kgcsjrzc)s, %(ldzc)s, %(qjfy)s, %(qtfldzc)s, %(qtldzc)s, ' \
                                   '%(qtysk)s, %(qycs)s, %(sdsfy)s, %(srze)s, %(sy)s, %(tzsy)s, %(tzxfdc)s,' \
                                   ' %(wxzc)s, %(xsfy)s, %(yfzk)s, %(yszk)s, %(yycb)s, %(yyjlrl)s, %(yysjjfj)s,' \
                                   ' %(yysr)s, %(yywsr)s, %(yywzc)s, %(zcfzl)s, %(zcjzss)s, %(zcze)s, %(zjgc)s, ' \
                                   '%(zzcjll)s, %(zzczzl)s)'


###################################基金####################################################