import pymysql.cursors
import datetime

now = datetime.datetime.now()
conn = pymysql.connect(host='localhost',
                     port=3306,
                     user='user',
                     passwd='passwd',
                     db='db',
                     charset='utf8')

def print_all():
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM test_table'
            cursor.execute(sql)
            for result in cursor.fetchall():
                print(result[0], result[1], result[2])
    finally:
        pass

def print_one(idx):
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM test_table WHERE idx=%s'
            cursor.execute(sql, idx)
            result = cursor.fetchone()
            print(result)
    finally:
        pass

def insert_table(time,masktxt):
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO test_table (datetime, no_mask) VALUES (%s, %s)'
            cursor.execute(sql, (time, masktxt))
            conn.commit()
    finally:
        pass


#insert_table(now, 'no')
print_all()

conn.close()