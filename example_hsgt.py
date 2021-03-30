import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import spider_hsgt as sh
import example_logger as log


def insert_stock_hsgt_tj(symbol):
    hsgts = sh.get_stock_hsgt_tj(symbol, 'eastmoney')
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'symbol': symbol}
        rownum = 0
        if hsgts is not None:
            cursor.execute(sql.SQL_DELETE_STOCK_HSGT_TJ, params)
            cursor.executemany(sql.SQL_INSERT_STOCK_HSGT_TJ, hsgts)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert ' + symbol + ' hsgt tj failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


if __name__ == '__main__':
    insert_stock_hsgt_tj('002185')
