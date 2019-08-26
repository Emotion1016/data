from page.init import *
from page.forgetPwd import *
from parameterized import parameterized
from utils.readCsv import getCsvData

class ForgetPwdTest(AppInit,ForgetPwd):

    @parameterized.expand(getCsvData(r'D:\appium_project\data\forgetPwd.csv'))
    def test_ForgetPwd(self,RecUsername,storeCode,RecPwd,RecPwdAgain,exp):
        '''
        忘记密码功能测试
        :param RecUsername: 输入用户名
        :param RecPwd: 输入密码
        :param exp: 期望结果
        '''
        self.clickForgetPage()
        self.typeRecUsername(RecUsername)
        self.typeStoreCode(storeCode)
        self.typeRecPwd(RecPwd)
        self.typeRecPwdAgain(RecPwdAgain)
        self.clickConfirm()
        res = self.get_toast_text(exp)
        self.assertEqual(res,exp)

if __name__ == '__main__':
    unittest.main()