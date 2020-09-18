import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import spider_finance as sf
from example_spider import insert_logger


def get_all_ready_stocks_finance_main():
    try:
        security_type = 'stock'
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_FINANCE_MAIN, params)
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


def insert_finance_main(symbol, pre_symbol):
    res = sf.get_finance_main(symbol, pre_symbol)
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'symbol': symbol}
        rownum = 0
        if res is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_FINANCE_MAIN, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_FINANCE_MAIN, res)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert ' + symbol + ' finance main failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


def init_finance_main():
    p_security_type = 'stock'
    res_data = get_all_ready_stocks_finance_main()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            p_symbol = res['symbol']
            p_pre_symbol = res['pre_symbol']
            rnt = insert_finance_main(p_symbol,p_pre_symbol)
            status = 'y' if rnt else 'n'
            insert_logger(p_security_type, p_symbol, 'init_finance_main', status, 'finance',
                          p_end_date, p_batch_number, rnt, 'init finance main')
            time.sleep(1)
    print('init finance main end')


def get_all_ready_stocks_finance_dupont():
    try:
        security_type = 'stock'
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_FINANCE_DUPONT, params)
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


def insert_finance_dupont(symbol, pre_symbol):
    finance_mains = sf.get_finance_main(symbol, pre_symbol)
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'symbol': symbol}
        rownum = 0
        if finance_mains is not None:
            cursor.execute(sql.SQL_DELETE_STOCKS_FINANCE_DUPONT, params)
            cursor.executemany(sql.SQL_INSERT_STOCKS_FINANCE_DUPONT, finance_mains)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)
        print('insert ' + symbol + ' finance dupont failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


def init_finance_dupont():
    p_security_type = 'stock'
    res_data = get_all_ready_stocks_finance_dupont()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            p_symbol = res['symbol']
            p_pre_symbol = res['pre_symbol']
            rnt = insert_finance_dupont(p_symbol,p_pre_symbol)
            status = 'y' if rnt else 'n'
            insert_logger(p_security_type, p_symbol, 'init_finance_dupont', status, 'finance',
                          p_end_date, p_batch_number, rnt, 'init finance dupont')
            time.sleep(1)
    print('init finance dupont end')


if __name__ == '__main__':
    #insert_finance_main('000002', 'SZ000002')
    insert_finance_dupont('000002', 'SZ000002')