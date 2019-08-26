from page.init import *
from page.register import Register
from parameterized import parameterized
from utils.readCsv import getCsvData

class RegisterTest(AppInit,Register):

    @parameterized.expand(getCsvData(r'D:\appium_project\data\storeCode_reg.csv'))
    def test_storeCode(self,storeCode,exp):
        '''
        注册界面前的厂家码测试
        :param storeCode: 厂家码
        :param exp: 期望结果
        '''
        self.enterRegister()
        self.typeStoreCode(storeCode)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res,exp)

    @parameterized.expand(getCsvData(r'D:\appium_project\data\register.csv'))
    def test_register(self, storeCode,regUsername,regPwd,regPwdAgain, exp):
        '''
        注册测试
        :param storeCode: 厂家码
        :param regUsername: 注册用户名
        :param regPwd: 注册密码
        :param regPwdAgain: 确认密码
        :param exp: 期望结果
        '''
        self.enterRegister()
        self.typeStoreCode(storeCode)
        self.clickContinue()
        self.typeRegUsername(regUsername)
        self.typeRegPwd(regPwd)
        self.typeRegPwdAgain(regPwdAgain)
        self.clickConfirm()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)



if __name__ == '__main__':
    unittest.main()