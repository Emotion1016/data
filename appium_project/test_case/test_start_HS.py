from page.init import *
from page.HSpage import HSpage
from parameterized import parameterized
from utils.readCsv import getCsvData
import time
from BeautifulReport import BeautifulReport


class StartHSTest(AppInitMain, HSpage):
    '''
    健康状态业务线
    '''

    # 开始辨识键测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\HSstartButton.csv'))
    def test_startHS(self, exp):
        time.sleep(3)
        self.start()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 手机号验证测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\TypePhoneNum.csv'))
    def test_phoneNum(self, phone_num, exp):
        self.start()
        self.type_phone_num(phone_num)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 同意书界面签名测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\sign.csv'))
    def test_sign(self, x1, y1, x2, y2, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        self.sign(x1, y1, x2, y2)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 同意书界面清除键测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\sign_clear.csv'))
    def test_sign_clear(self, x1, y1, x2, y2, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        self.sign(x1, y1, x2, y2)
        self.clear()
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 面诊测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\TypePhoneNum.csv'))
    def test_faceConsultation(self, phone_num, exp):
        self.start()
        self.type_phone_num(phone_num)
        pass

    # 个人信息界面选择男
    @parameterized.expand(getCsvData(r'D:\appium_project\data\PersonalInfoMale.csv'))
    def test_personalInfoMale(self, sex, age, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_age(age)
        self.choose_sex(sex)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 个人信息界面选择女
    @parameterized.expand(getCsvData(r'D:\appium_project\data\PersonalInfoFemale001.csv'))
    def test_personalInfoFemale_001(self, sex, age):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_age(age)
        self.choose_sex(sex)
        self.assertFalse(self.print_extra())
        # res = True
        # try:
        #     self.printExtra()
        # except:
        #     print('没找到元素,断言成功')
        #     res = False
        # if res is True:
        #     self.assertTrue(res, '断言错了,没找到元素')
        # else:
        #     self.assertTrue(res, '找到元素')

    @parameterized.expand(getCsvData(r'D:\appium_project\data\PersonalInfoFemale002.csv'))
    def test_personalInfoFemale_002(self, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    @parameterized.expand(getCsvData(r'D:\appium_project\data\PersonalInfoFemale003.csv'))
    def test_personalInfoFemale_003(self, age, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_age(age)
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 身高界面滑动条测试
    def test_height(self):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.assertTrue(self.swipe_height())

    # 体重界面滑动条测试
    def test_weight(self):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.clickContinue()
        self.swipe_height()
        self.clickContinue()
        self.assertTrue(self.swipe_weight())

    # 体重界面加号键测试
    def test_weight_plus(self):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.clickContinue()
        self.swipe_height()
        self.clickContinue()
        self.assertTrue(self.click_plus())

    # 体重界面减号键测试
    def test_weight_minus(self):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.clickContinue()
        self.swipe_height()
        self.clickContinue()
        self.assertTrue(self.click_minus())

    # 通用单选题界面测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\radiochoiceone.csv'))
    def test_radio_choice_one(self, start_num, end_num, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(start_num, end_num)
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 通用单选题界面题目校验测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\radio_choice_title.csv'))
    def test_radio_choice_title(self, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        time.sleep(3)
        res = self.radio_question_title()
        self.assertEqual(res, exp)

    # 通用多选题界面测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\multi_choice_one.csv'))
    def test_multi_choice_one(self, sex, start_num, end_num, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_sex(sex)
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(start_num, end_num)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 通用多选题界面题目校验测试
    # @parameterized.expand(getCsvData(r'D:\appium_project\data\multi_choice_title.csv'))
    def test_multi_choice_title(self, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_random_sex()
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        res = self.multi_choice_title()
        # print(res)
        self.assertEqual(res, exp)
        self.click_close()

    # 女性单选题界面测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\radio_choice_two.csv'))
    def test_radio_choice_two(self, start_num, end_num, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_age('19——25岁')
        self.choose_sex('女')
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(1, 7)
        self.choose_answer(start_num, end_num)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 女性单选题界面题目校验测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\female_radio_choice_title.csv'))
    def test_female_radio_choice_title(self, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_age('19——25岁')
        self.choose_sex('女')
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(1, 7)
        self.clickContinue()
        time.sleep(3)
        res = self.female_radio_choice_title()
        self.assertEqual(res, exp)
        self.click_close()

    # 病史界面多选题测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\multi_choice_two.csv'))
    def test_multi_choice_two(self, start_num, end_num, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_sex('男')
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(1, 7)
        self.clickContinue()
        self.multi_random_choice_two(start_num, end_num)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(res, exp)

    # 病史界面各个单选键测试
    def test_click_each_choice(self):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_sex('男')
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(1, 7)
        self.clickContinue()
        self.assertTrue(self.ergodic_click_each_choice())

    # 病史界面各个单选键文字验证测试
    @parameterized.expand(getCsvData(r'D:\appium_project\data\each_choice_text.csv'))
    def test_each_choice_text(self, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_random_age()
        self.choose_sex('男')
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(1, 7)
        self.clickContinue()
        time.sleep(3)
        res = self.ergodic_print_each_choice()
        self.assertEqual(res, exp)

    # 个人信息界面选择女性并选择孕期或哺乳期或绝经期
    @parameterized.expand(getCsvData(r'D:\appium_project\data\female_special.csv'))
    def test_female_special(self, text, exp):
        self.start()
        self.type_phone_num(self.fake.phone_number())
        self.clickContinue()
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        self.driver.implicitly_wait(100)
        self.choose_age('19——25岁')
        self.choose_sex('女')
        self.click_extra(text)
        self.clickContinue()
        time.sleep(3)
        self.swipe_height()
        self.clickContinue()
        time.sleep(3)
        self.swipe_weight()
        self.clickContinue()
        self.radio_question(1, 8)
        self.clickContinue()
        self.multi_choice_one(1, 7)
        self.clickContinue()
        res = self.get_toast_text(exp)
        self.assertEqual(exp, res)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    t1 = unittest.TestLoader().loadTestsFromName('test_start_HS.StartHSTest.test_female_radio_choice_title')
    suite.addTests(t1)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    result = BeautifulReport(suite)
    result.report(filename=time.ctime() + 'Report', description='UI自动化测试报告', log_path='reports')
