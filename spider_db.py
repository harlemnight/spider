import psycopg2 as pg2

DATABASE = 'DB_FINANCE'
USER = 'finance'
PWD = 'gigi117zyd'
HOST = '127.0.0.1'
PORT = '5432'


def get_dbcon():
    conn = pg2.connect(database=DATABASE, user=USER, password=PWD, host=HOST, port=PORT)
    return conn


def close_dbcon(con):
    con.cursor().close()
    con.close()


def rollback(con):
    con.rollback()


