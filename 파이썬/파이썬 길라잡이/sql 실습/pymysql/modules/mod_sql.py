#sql 모듈 생성
# 1. cplass 생성 이름: Database
# 2. class 생성 시 pymysql.connect 변수, cursor 생성
# 3. init을 제외한 함수 3개 생성
# 4. execute() -> sql, value를 받아서 sql문을 실행
# 5. executeAll() -> sql, value를 받아서 sql문을 실행, 결과값 return
# 6. commit() -> commit 하는 함수 생성
import pymysql

class Databse():
    def __init__(self):
        self._db = pymysql.connect(
              user = 'root',
              passwd = 'qwer1234',
              host = 'localhost',
              db = 'ubion'
              )
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)
    
    def execute(self,sql,value={}):
        self.cursor.execute(sql,value)

    def executeAll(self,sql,value={}):
        self.cursor.execute(sql,value)
        self.result = self.cursor.fetchall()
        return self.result
    
    def commit(self):
        self._db.commit()
        # self._db.close()

    
    

