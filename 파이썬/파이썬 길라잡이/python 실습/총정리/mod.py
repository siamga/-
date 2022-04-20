import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(
            user = 'root',
            password = 'qwer1234',
            host = 'localhost',
            db = 'ubion'
            )

        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self,sql,value={}):
        self.cursor.execute(sql,value)
    
    def executeAll(self,sql,value={}):
        self.cursor.execute(sql,value)
        self.result = self.cursor.fetchall()
        return self.result
    
    def commit(self):
        self.db.commit()
        self.db.close()