# https://www.jianshu.com/p/3bcb98dd2654
# https://blog.csdn.net/weixin_43174639/article/details/84643586?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# https://www.cnblogs.com/deartear/p/8616457.html
import spider_property as sf
import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import example_logger as log


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
            log.insert_logger('stock', hy_dm, 'init_hy', status, 'sw_hy', p_end_date, p_batch_number, rnt, 'init hy dzb')
            time.sleep(0.5)


def init_concept_stocks(source):
    res_data = get_concept_list(source)
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            concept_dm = res['concept_dm']
            rnt = insert_concept_stocks(concept_dm)
            status = 'y' if rnt else 'n'
            log.insert_logger('stock', concept_dm, 'init_concept', status, '10jqka_concept', p_end_date, p_batch_number,
                          rnt, 'init concept dzb')
            time.sleep(0.5)


def insert_concept_stocks(source, concept_dm):
    res = sf.get_concept_stocks(source, concept_dm)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'concept_dm': concept_dm}
            if source == '10jqka':
                cursor.execute(sql.SQL_DELETE_CONCEPT_STOCKS_10JQKA, params)
                cursor.executemany(sql.SQL_INSERT_CONCEPT_STOCKS_10JQKA, res)
            else:
                cursor.execute(sql.SQL_DELETE_CONCEPT_STOCKS_EASTMONEY, params)
                cursor.executemany(sql.SQL_INSERT_CONCEPT_STOCKS_EASTMONEY, res)
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


def get_concept_list(source):
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        if source == '10jqka':
            cursor.execute(sql.SQL_GET_STOCK_CONCEPTS_10JQKA)
        else:
            cursor.execute(sql.SQL_GET_STOCK_CONCEPTS_EASTMONEY)
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


def init_concepts(source):
    res = sf.get_concepts(source)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            if source == '10jqka':
                sql_delete = sql.SQL_DELETE_CONCEPTS_10JQKA
                sql_insert = sql.SQL_INSERT_CONCEPTS_10JQKA
            else:
                sql_delete = sql.SQL_DELETE_CONCEPTS_EASTMONEY
                sql_insert = sql.SQL_INSERT_CONCEPTS_EASTMONEY
            cursor.execute(sql_delete)
            cursor.executemany(sql_insert, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert ' + source + ' concept_dm all successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert ' + source + ' concept_dm all failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        print('concept_dm all is None')
        return None


if __name__ == '__main__':
    # init_industry_stocks() #初始化申万二级行业成份股 每周执行一次
    # 10jqka概念基本被废弃
    init_concepts('eastmoney')    #初始化概念 每周执行一次
    init_concept_stocks('eastmoney') #初始化概念成份股 每周执行一次

