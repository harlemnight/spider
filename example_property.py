# https://www.jianshu.com/p/3bcb98dd2654
# https://blog.csdn.net/weixin_43174639/article/details/84643586?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# https://www.cnblogs.com/deartear/p/8616457.html
import spider_stock as sf
import spider_db as db
import spider_sql as sql
import datetime as dt
import time


def insert_logger(security_type, symbol, operation, status, business,
                  create_date, batch_number, row_number, message):
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {
                'security_type': security_type,
                'symbol': symbol,
                'operation': operation,
                'status': status,
                'business': business,
                'create_date': create_date,
                'batch_number': batch_number,
                'row_number': row_number,
                'message': message
        }
        cursor.execute(sql.SQL_INSERT_XT_LOGGER_MX, params)
        con.commit()
        print('insert logger ' + security_type + ' ' +
              symbol + ' ' + operation + ' ' + business + ' ' + status + ' row count ' + str(row_number))
    except Exception as e:
        db.rollback(con)
        print(e)
    finally:
        db.close_dbcon(con)


def insert_industry_stocks(hy_dm):
    res = sf.get_industry_stocks(hy_dm)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'hy_dm': hy_dm}
            cursor.execute(sql.SQL_DELETE_STOCK_INDUSTRY_SW, params)
            cursor.executemany(sql.SQL_INSERT_STOCK_INDUSTRY_SW, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            # print('insert hy_dm:' + hy_dm + ' successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            # print('insert hy_dm:' + hy_dm + ' failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        # print('hy_dm:' + hy_dm + ' is None')
        return None


def get_industry_list(lvl):
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'lvl': lvl}
        cursor.execute(sql.SQL_GET_STOCK_INDUSTRY_LIST_SW, params)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['hy_dm'] = row[0]
            res.append(data)
        if len(res) > 0:
            # print('get all industry ' + lvl + ' level successfully from database')
            return res
        else:
            return None
    except Exception as e:
        db.rollback(con)
        # print('get all industry ' + lvl + ' level failed :' + str(e))
        return None
    finally:
        db.close_dbcon(con)


def init_industry_stocks():
    res_data = get_industry_list('2')
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            hy_dm = res['hy_dm']
            rnt = insert_industry_stocks(hy_dm)
            status = 'y' if rnt else 'n'
            insert_logger('stock', hy_dm, 'init_hy', status, 'sw_hy', p_end_date, p_batch_number, rnt, 'init hy dzb')
            time.sleep(0.5)


def init_concept_stocks_10jqka():
    res_data = get_concept_list()
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            concept_dm = res['concept_dm']
            rnt = insert_concept_stocks(concept_dm)
            status = 'y' if rnt else 'n'
            insert_logger('stock', concept_dm, 'init_concept', status, '10jqka_concept', p_end_date, p_batch_number,
                          rnt, 'init concept dzb')
            time.sleep(0.5)


def insert_concept_stocks(concept_dm):
    res = sf.get_concept_stocks(concept_dm)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'concept_dm': concept_dm}
            cursor.execute(sql.SQL_DELETE_CONCEPT_STOCKS_10JQKA, params)
            cursor.executemany(sql.SQL_INSERT_CONCEPT_STOCKS_10JQKA, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            # print('insert concept_dm:' + concept_dm + ' successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            # print('insert concept_dm:' + concept_dm + ' failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        # print('concept_dm:' + concept_dm + ' is None')
        return None


def get_concept_list():
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        cursor.execute(sql.SQL_GET_STOCK_CONCEPTS_10JQKA)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['concept_dm'] = row[0]
            res.append(data)
        if len(res) > 0:
            # print('get all concept successfully from database')
            return res
        else:
            return None
    except Exception as e:
        db.rollback(con)
        # print('get all concept failed :' + str(e))
        return None
    finally:
        db.close_dbcon(con)


def init_concepts_10jqka():
    res = sf.get_concepts('10jqka')
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            cursor.execute(sql.SQL_DELETE_CONCEPTS_10JQKA)
            cursor.executemany(sql.SQL_INSERT_CONCEPTS_10JQKA, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert concept_dm all successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert concept_dm all failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        print('concept_dm all is None')
        return None


if __name__ == '__main__':
    init_industry_stocks() #初始化申万二级行业成份股 每周执行一次
    init_concepts_10jqka()    #初始化概念 每周执行一次
    init_concept_stocks_10jqka() #初始化概念成份股 每周执行一次

