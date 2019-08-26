from page.init import *
from page.personalReport import PersonalRE
from parameterized import parameterized
from utils.readCsv import getCsvData

class PersonalReTest(AppInitMain,PersonalRE):

    @parameterized.expand(getCsvData(r'D:\appium_project\data\typePhone.csv'))
    def test_typePhone(self,phoneNum,exp):
        '''
        开始辨识后的手机验证测试
        :param phoneNum: 手机号
        :param exp: 预期结果
        '''
        self.clickPerHis()
        self.typePhoneNum(phoneNum)
        self.clickGetVerCode()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    @parameterized.expand(getCsvData(r'D:\appium_project\data\typeVerifyCode01.csv'))
    def test_typeVerifyCode01(self,phoneNum,verifyCode,exp):
        self.clickPerHis()
        self.typePhoneNum(phoneNum)
        self.typeVerifyCode(verifyCode)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res,exp)

    @parameterized.expand(getCsvData(r'D:\appium_project\data\typeVerifyCode02.csv'))
    def test_typeVerifyCode02(self,phoneNum,exp):
        self.clickPerHis()
        self.typePhoneNum(phoneNum)
        self.clickGetVerCode()
        verifyCode = self.logcat()
        self.typeVerifyCode(verifyCode)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res,exp)

    @parameterized.expand(getCsvData(r'D:\appium_project\data\clickHealthEventButton.csv'))
    def test_clickHealthEventButton(self,phoneNum,exp):
        self.clickPerHis()
        self.typePhoneNum(phoneNum)
        self.clickGetVerCode()
        verifyCode = self.logcat()
        self.typeVerifyCode(verifyCode)
        self.clickContinue()
        self.clickHealthEventButton()
        res = self.get_toast_text(exp)
        self.assertEqual(res,exp)

if __name__ == '__main__':
    unittest.main()