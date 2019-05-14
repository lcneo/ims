from ims.model_struct import *
from ims.db import execute



class m_account:
    """docstring for account"""

    def __init__(self):
        self.user = struct_account('None', 'None')

    def login(self, account: str, password: str) -> bool:
        sql = """SELECT * FROM user WHERE account='{account}'
		""".format(account=account)
        req = execute(sql)
        if req and account != "None":
            if req[0][2] != password:
                return False
            self.user = struct_account(req[0][1], req[0][2])
            return True
        else:
            return False

    def uni_ac(self, ac: str) -> bool:
        """
        Verify account uniqueness
        uniquet True else Flase
        """
        sql = """
		SELECT * FROM user WHERE account="{ac}"
		""".format(ac=ac)
        req = execute(sql)
        if not req:
            return True
        return False

    def register(self, ac: str, pw1: str, pw2: str) -> int:
        """
        flag = 0 权限不足
        flag = 1 账号重复或格式错误
        flag = 2 两次密码不一致或格式错误
        flag = 9 注册成功
        """
        flag = None
        sql = """INSERT INTO user(account, password) VALUES("{ac}","{pw}")""".format(ac=ac, pw=pw1)
        if self.user.account != "admin":
            flag = 0
        else:
            if (len(ac) > 16) | (not self.uni_ac(ac)):
                flag = 1
            else:
                if (len(pw1) > 16) | (pw1 != pw2):
                    flag = 2
                else:
                    execute(sql)
                    flag = 9
        return flag

    def change_pw(self, pw: str, pw1: str, pw2: str) -> int:
        """
        flag = 0 权限不足
        flag = 1 密码格式有误
        flag = 9 修改成功
        """
        flag = None
        sql = """
		UPDATE user SET password='{pw}' WHERE account='{ac}' 
		""".format(pw=pw1, ac=self.user.account)
        if self.user.account == 'None':
            flag = 0
        else:
            if pw != self.user.password:
                flag = 1
            else:
                if (len(pw1) > 16) | (pw1 != pw2):
                    flag = 2
                else:
                    execute(sql)
                    flag = 9
        return flag

    def logout(self):
        self.__init__()


if __name__ == '__main__':
    c = m_account()
    print("login:", c.login("neo", "neoneoneo"))
    print(c.user.account)
    c.logout()
    print(c.user.account)
# print(c.change_pw("12333","neoneoneo","neoneoneo"))
# print(c.register('None','None','None'))

