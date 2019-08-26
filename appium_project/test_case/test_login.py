from page.init import *
from page.login import Login
from parameterized import parameterized
from utils.readCsv import getCsvData


class LoginTest(AppInit, Login):

    @parameterized.expand(getCsvData(r'D:\appium_project\data\login.csv'))
    def test_Login_001(self, username, password, exp):
        '''
        登录测试
        :param username: 用户名
        :param password: 密码
        :param exp: 期望结果
        '''
        self.typeUsername(username)
        self.typePassword(password)
        self.clickConfirm
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
