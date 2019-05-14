import pymysql
import pymysql.cursors


class imsdb(object):
    """docstring for sql"""

    def __init__(self, host='148.70.3.154', user='imsdb', password='neoneoneo', port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = 'imsdb'
        self.charset = 'utf8'
        self.connect_init()

    def connect_init(self):
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                         port=self.port,
                                         charset=self.charset)

            # print("数据库连接成功!")
            connection.close()
        except:
            print("数据库连接失败!")

    def connect(self) -> pymysql.connections.Connection:
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port,
                                     charset=self.charset)
        return connection

    def execute(self, sql: str) -> tuple:
        con = self.connect()
        cur = con.cursor()
        try:
            count = cur.execute(sql)
            con.commit()
            if count != 0:
                return cur.fetchall()
            else:
                return None
        except:
            print("Error:"+sql)
        finally:
            # con.close()
            cur.close()


def execute(sql: str) -> tuple:
    #对imsdb进行sql语句查询
    con = imsdb()
    return con.execute(sql)

def add_del_update(sql:str)->bool:
    """
    执行无返回值的sql语句，用于增，删，改
    """
    if execute(sql) == ():
        req = True
    else:
        req = False
    return req

def search(sql:str)->tuple:
    pass
if __name__ == '__main__':
    sql = """
	UPDATE department SET department_no = "305", name = "信息安全系", tro_num = 0, class_num=3, collage_no = "3" WHERE department_no = "305" 
	"""
    print(execute(sql))