import spider_jqdata_swhy as jqhy
import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import example_logger as log
from jqdatasdk import *


def init_jqdata_swhy(swhylevel):
    res = jqhy.get_jqdata_swhy(swhylevel)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'swhylevel': swhylevel}
            sql_delete = sql.SQL_DELETE_STOCK_JQDATA_SWHY
            sql_insert = sql.SQL_INSERT_STOCK_JQDATA_SWHY
            cursor.execute(sql_delete, params)
            cursor.executemany(sql_insert, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert jqdata swhy all successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert jqdata swhy all failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        print('jqdata swhy all is None')
        return None


def init_jqdata_swhy_stocks():
    res_data = get_jqdata_swhy_list()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            swhy_dm = res['swhy_dm']
            rnt = insert_jqdata_swhy_stocks(swhy_dm)
            status = 'y' if rnt else 'n'
            log.insert_logger('stock', swhy_dm, 'init_jqdata_swhy', status, 'init_jqdata_swhy', p_end_date, p_batch_number,
                          rnt, 'init jqdata swhy dzb')
            time.sleep(0.5)


def insert_jqdata_swhy_stocks(swhy_dm):
    res = jqhy.get_jqdata_swhy_stocks(swhy_dm)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'swhy_dm': swhy_dm}
            cursor.execute(sql.SQL_DELETE_STOCK_JQDATA_INDUSTRY_SWHY, params)
            cursor.executemany(sql.SQL_INSERT_STOCK_JQDATA_INDUSTRY_SWHY, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            # print('insert jqdata swhy_dm:' + swhy_dm + ' successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            # print('insert jqdata swhy_dm:' + swhy_dm + ' failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        # print('jqdata swhy_dm:' + swhy_dm + ' is None')
        return None


def get_jqdata_swhy_list():
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        cursor.execute(sql.SQL_GET_STOCK_JQDATA_INDUSTRY_SWHY)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['swhy_dm'] = row[0]
            res.append(data)
        if len(res) > 0:
            # print('get jqdata_swhy successfully from database')
            return res
        else:
            return None
    except Exception as e:
        db.rollback(con)
        # print('get jqdata_swhy failed :' + str(e))
        return None
    finally:
        db.close_dbcon(con)


if __name__ == '__main__':
    auth('13908366866', '366866') #登录认证
    #初始化聚宽申万1-3级行业以及成份股 每周执行一次
    #    init_jqdata_swhy('sw_l'+str(i+1))
    init_jqdata_swhy_stocks()
