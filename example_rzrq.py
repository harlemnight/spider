import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import spider_rzrq as sr
import example_logger as log


def get_all_ready_stocks_rzrq():
    try:
        security_type = 'stock'
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_RZRQ, params)
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


def insert_stock_rzrq(symbol):
    rzrqs = sr.get_stock_rzrq(symbol, 'eastmoney')
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'symbol': symbol}
        rownum = 0
        if rzrqs is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_RZRQ, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_RZRQ, rzrqs)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert ' + symbol + ' rzrq failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


def init_stock_rzrq():
    p_security_type = 'stock'
    res_data = get_all_ready_stocks_rzrq()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            p_symbol = res['symbol']
            rnt = insert_stock_rzrq(p_symbol)
            status = 'y' if rnt else 'n'
            log.insert_logger(p_security_type, p_symbol, 'init_stock_rzrq', status, 'rzrq',
                          p_end_date, p_batch_number, rnt, 'init stock rzrq')
            time.sleep(1)
    print('init stock rzrq end')


def insert_rzrq_list():
    rzrq_list = sr.get_rzrq_stocks('eastmoney', '2021-03-26')
    print(rzrq_list)
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = rzrq_list
        rownum = 0
        if rzrq_list is not None:
            cursor.execute(sql.SQL_DELETE_RZRQ_LIST)
            cursor.executemany(sql.SQL_INSERT_RZRQ_LIST, rzrq_list)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert rzrq list failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


if __name__ == '__main__':
    #insert_rzrq('000070')
    insert_rzrq_list()
    #init_stock_rzrq()
