from page.init import *
from page.HSpage import HSpage
from page.typePhonenum import TypePhonenum
from parameterized import parameterized
from utils.readCsv import getCsvData

class TypePhoneNumTest(AppInitMain,HSpage,TypePhonenum):

    @parameterized.expand(getCsvData(r'D:\appium_project\data\TypePhoneNum.csv'))
    def test_start(self,phonenum,exp):
        '''
        健康状态辨识后的输入手机号测试
        :param phonenum: 手机号
        :param exp: 预期结果
        '''
        self.start()
        self.typePhonenum(phonenum)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res,exp)

if __name__ == '__main__':
    unittest.main()