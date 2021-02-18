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




if __name__ == '__main__':
    auth('13908366866', '366866') #认证
    # 初始化地域成份股 每周执行一次
    for i in range(3):
        init_jqdata_swhy('sw_l'+str(i+1))

