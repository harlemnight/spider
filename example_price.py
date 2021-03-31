# https://www.jianshu.com/p/3bcb98dd2654
# https://blog.csdn.net/weixin_43174639/article/details/84643586?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# https://www.cnblogs.com/deartear/p/8616457.html
import spider_price as sf
import spider_db as db
import spider_sql as sql
import time
import example_logger as log


def init_stocks():
    security_type = 'stock'
    res = sf.get_stocks()
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'type': security_type}
            cursor.execute(sql.SQL_DELETE_SECURITY_BY_TYPE, params)
            cursor.executemany(sql.SQL_INSERT_SECURITY, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert securities ' + security_type + ' successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert securities ' + security_type + ' failed :' + str(e))
            return 0
        finally:
            db.close_dbcon(con)
    else:
        print('securities ' + security_type + ' is None')
        return 0


def insert_stock_price(symbol, start_date, end_date):
    security_type = 'stock'
    res = sf.get_history_price(security_type, symbol, start_date, end_date)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            cursor.executemany(sql.SQL_INSERT_STOCK_HISTORY_PRICE, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert ' + security_type + ' price successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert ' + security_type + ' price failed :' + str(e))
            return 0
        finally:
            db.close_dbcon(con)
    else:
        print('security_type ' + security_type + ' is None')
    return 0


def get_all_security_list_by_type(security_type):
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'type': security_type}
        cursor.execute(sql.SQL_GET_STOCK_LIST_NET_EASY, params)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['symbol'] = row[0]
            data['neteasy_symbol'] = row[1]
            res.append(data)
        if len(res) > 0:
            print('get all ' + security_type + ' successfully from database')
            return res
        else:
            return None
    except Exception as e:
        db.rollback(con)
        print('get all ' + security_type + ' failed :' + str(e))
        return None
    finally:
        db.close_dbcon(con)


def insert_batch_current_price(security_type):
    res = sf.get_batch_current_price(security_type)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            cursor.execute(sql.SQL_DELETE_STOCK_CURRENT_PRICE)
            cursor.executemany(sql.SQL_INSERT_STOCK_CURRENT_PRICE, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert ' + security_type + ' current all price successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert ' + security_type + ' current all price failed :' + str(e))
            return 0
        finally:
            db.close_dbcon(con)
    else:
        print('security_type ' + security_type + ' is None')
    return 0


def init_history_stock_price(p_start_date, p_end_date):
    p_security_type = 'stock'
    res_data = get_all_security_list_by_type(p_security_type)
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            p_symbol_net_easy = res['neteasy_symbol']
            p_symbol = res['symbol']
            rnt = insert_stock_price(p_symbol_net_easy, p_start_date, p_end_date)
            status = 'y' if rnt else 'n'
            log.insert_logger(p_security_type, p_symbol, 'init_history_price', status, 'history_price',
                          p_end_date, p_batch_number, rnt, 'init stock price')
            time.sleep(0.5)
    print('init history stock price end')


if __name__ == '__main__':
    # 初始化标股票 每日4点执行
    init_stocks()
    #start_date = '20200101'
    #end_date = '20201231'
    # 补录历史行情
    #init_history_stock_price(start_date, end_date)
    # 记录当日股票收盘行情 4点后执行
    insert_batch_current_price('stock')

