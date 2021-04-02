import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import spider_hsgt as sh
import example_logger as log


def get_all_ready_stocks_hsgt_tj():
    try:
        security_type = 'stock'
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_HSGT_TJ, params)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['symbol'] = row[0]
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


def get_all_ready_stocks_hsgt_mx():
    try:
        security_type = 'stock'
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_HSGT_MX, params)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['symbol'] = row[0]
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


def insert_hsgt_list():
    hsgts = sh.get_hsgt_list('eastmoney')
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        rownum = 0
        if hsgts is not None:
            cursor.execute(sql.SQL_DELETE_HSGT_LIST)
            cursor.executemany(sql.SQL_INSERT_HSGT_LIST, hsgts)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert hsgt list failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


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


def insert_stock_hsgt_mx(symbol,startdate,enddate):
    hsgts = sh.get_stock_hsgt_mx(symbol,'eastmoney',startdate,enddate)
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'symbol': symbol}
        rownum = 0
        if hsgts is not None:
            cursor.execute(sql.SQL_DELETE_STOCK_HSGT_MX, params)
            cursor.executemany(sql.SQL_INSERT_STOCK_HSGT_MX, hsgts)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert ' + symbol + ' hsgt mx failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


def init_stock_hsgt_tj():
    p_security_type = 'stock'
    res_data = get_all_ready_stocks_hsgt_tj()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            p_symbol = res['symbol']
            rnt = insert_stock_hsgt_tj(p_symbol)
            status = 'y' if rnt else 'n'
            log.insert_logger(p_security_type, p_symbol, 'init_stock_hsgt_tj', status, 'hsgttj',
                          p_end_date, p_batch_number, rnt, 'init stock hsgttj')
            time.sleep(1)
    print('init stock hsgttj end')


if __name__ == '__main__':
    #insert_hsgt_list()
    insert_stock_hsgt_tj('603300')
    insert_stock_hsgt_mx('603300','2021-03-01','2021-03-30')