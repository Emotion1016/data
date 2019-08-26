import pymysql
from pymysql.cursors import DictCursor


class Database:

    # 构造方法（实例化时初始调用的方法）
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '19931016', 'test', charset='utf8')
        self.cursor = self.db.cursor(DictCursor)

    def query_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def query_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def update_data(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        self.db.rollback()

    # 析构方法（收尾工作），什么时候收尾：Python高兴的时候
    def __del__(self):
        self.cursor.close()
        self.db.close()
        # print("清理工作完成...")


if __name__ == '__main__':
    db = Database()
    res = db.query_all('select * from student')
    print(res)



#
# if __name__=='__main__':
#     u = Utility()
#     # r1 = u.query_one('select * from job_register where job_regist_id = 2')
#     r2 = u.query_all('select * from job_register where job_regist_id = 2222')
#     # print(type(r2))
#     # print(r1)
#     print(r2)
