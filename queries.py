import sqlite3
from sqlite3 import Error


def create_connection(path):

    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(e)

    return conn


def create_telex_table(path):
    conn = create_connection(path)
    c = conn.cursor()
    sql = '''
            CREATE TABLE IF NOT EXISTS news (
                id integer PRIMARY KEY,
                title text NOT NULL,
                LINK text type UNIQUE
            )
    '''
    try:
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def add_news(path, news):
    conn = create_connection(path)
    c = conn.cursor()
    sql = '''
            INSERT OR IGNORE INTO news (title, link) VALUES (?,?)
    '''
    try:
        c.execute(sql, news)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
