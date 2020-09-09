import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import spider_shareholder as sf
from example_spider import insert_logger


def get_all_ready_stocks_shareholders():
    try:
        security_type = 'stock'
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_SHAREHOLDER, params)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['symbol'] = row[0]
            data['pre_symbol'] = row[1]
            res.append(data)
        if len(res) > 0:
            print('get all ' + security_type + ' list successfully from database')
            return res
        else:
            return None
    except Exception as e:
        db.rollback(con)
        print('get all ' + security_type + ' list failed :' + str(e))
        return None
    finally:
        db.close_dbcon(con)


def insert_shareholders(symbol, pre_symbol):
    kggxs, gdrss, jjcgs ,sdgds = sf.get_shareholders(symbol, pre_symbol)
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'symbol': symbol}
        rownum = 0
        if kggxs is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_SJKZR, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_SJKZR, kggxs)
            rownum += cursor.rowcount
        if gdrss is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_GDRS, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_GDRS, gdrss)
            rownum += cursor.rowcount
        if jjcgs is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_JJCG, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_JJCG, jjcgs)
            rownum += cursor.rowcount
        if sdgds is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_SDGD, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_SDGD, sdgds)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert ' + symbol + ' shareholder failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


def init_shareholders():
    p_security_type = 'stock'
    res_data = get_all_ready_stocks_shareholders()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            p_symbol = res['symbol']
            p_pre_symbol = res['pre_symbol']
            rnt = insert_shareholders(p_symbol,p_pre_symbol)
            status = 'y' if rnt else 'n'
            insert_logger(p_security_type, p_symbol, 'init_shareholder', status, 'shareholder',
                          p_end_date, p_batch_number, rnt, 'init shareholders')
            time.sleep(1)
    print('init shareholder end')


if __name__ == '__main__':
    insert_shareholders('000002', 'SZ000002')
    #init_shareholders()