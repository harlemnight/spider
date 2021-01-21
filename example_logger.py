import spider_db as db
import spider_sql as sql


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
