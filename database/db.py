import pymysql.cursors

#database 클래스와 접근하기위한 쿼리문에 관련된 함수들이 모여있는 파일입니다 
class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                     port=3306,
                     user='user',
                     passwd='passwd',
                     db='db',
                     charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()