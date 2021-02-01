# https://www.jianshu.com/p/3bcb98dd2654
# https://blog.csdn.net/weixin_43174639/article/details/84643586?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# https://www.cnblogs.com/deartear/p/8616457.html
import spider_area as sa
import spider_db as db
import spider_sql as sql
import datetime as dt
import time
import example_logger as log


def init_area_stocks(source):
    res_data = get_area_list(source)
    p_end_date = dt.datetime.now().strftime('%Y%m%d')
    p_batch_number = time.time() * 10000000
    if res_data:
        for res in res_data:
            area_dm = res['area_dm']
            rnt = insert_area_stocks(source, area_dm)
            status = 'y' if rnt else 'n'
            log.insert_logger('stock', area_dm, 'init_'+source+'_area', status, 'init_'+source+'_area', p_end_date, p_batch_number,
                          rnt, 'init area dzb')
            time.sleep(0.5)


def insert_area_stocks(source, area_dm):
    res = sa.get_area_stocks(source, area_dm)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            params = {'area_dm': area_dm}
            if source == '10jqka':
                cursor.execute(sql.SQL_DELETE_AREA_STOCKS_10JQKA, params)
                cursor.executemany(sql.SQL_INSERT_AREA_STOCKS_10JQKA, res)
            else:
                cursor.execute(sql.SQL_DELETE_AREA_STOCKS_EASTMONEY, params)
                cursor.executemany(sql.SQL_INSERT_AREA_STOCKS_EASTMONEY, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            # print('insert area_dm:' + area_dm + ' successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            # print('insert area_dm:' + area_dm + ' failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        # print('area_dm:' + area_dm + ' is None')
        return None


def get_area_list(source):
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        if source == '10jqka':
            cursor.execute(sql.SQL_GET_STOCK_AREA_10JQKA)
        else:
            cursor.execute(sql.SQL_GET_STOCK_AREA_EASTMONEY)
        res = []
        for row in cursor.fetchall():
            data = {}
            data['area_dm'] = row[0]
            res.append(data)
        if len(res) > 0:
            # print('get all area successfully from database')
            return res
        else:
            return None
    except Exception as e:
        db.rollback(con)
        # print('get all area failed :' + str(e))
        return None
    finally:
        db.close_dbcon(con)


def init_areas(source):
    res = sa.get_areas(source)
    if res is not None:
        try:
            con = db.get_dbcon()
            cursor = con.cursor()
            if source == '10jqka':
                sql_delete = sql.SQL_DELETE_AREA_10JQKA
                sql_insert = sql.SQL_INSERT_AREA_10JQKA
            else:
                sql_delete = sql.SQL_DELETE_AREA_EASTMONEY
                sql_insert = sql.SQL_INSERT_AREA_EASTMONEY
            cursor.execute(sql_delete)
            cursor.executemany(sql_insert, res)
            rowcount = str(cursor.rowcount)
            con.commit()
            print('insert ' + source + ' area_dm all successfully rowcount: ' + rowcount)
            return rowcount
        except Exception as e:
            db.rollback(con)
            print('insert ' + source + ' area_dm all failed :' + str(e))
            return None
        finally:
            db.close_dbcon(con)
    else:
        print('area_dm all is None')
        return None


if __name__ == '__main__':
    #init_areas('eastmoney')    #初始化地域 每周执行一次
    init_area_stocks('eastmoney') #初始化地域成份股 每周执行一次

