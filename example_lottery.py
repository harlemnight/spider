import spider_db as db
import spider_sql as sql
import spider_lottery as sl
import datetime as dt
import time
import example_logger as log


def insert_lottery(source, start):
    lt = sl.get_lottery_list(source,start)
    rownum = 0
    try:
        con = db.get_dbcon()
        cursor = con.cursor()
        params = {'ssq': start}
        if lt is not None:
            cursor.execute(sql.SQL_DELETE_LOTTERY, params)
            cursor.executemany(sql.SQL_INSERT_LOTTERY,lt)
            rownum += cursor.rowcount
        con.commit()
        return rownum
    except Exception as e:
        db.rollback(con)

        print('insert ' + str(rownum) + ' lottery failed' + str(e))
        return 0
    finally:
        db.close_dbcon(con)
    return 0


if __name__ == '__main__':
    rs = insert_lottery('500caipiao', '22028')
    print(rs)
    print('yes')