from page.init import *
from page.login import *
from page.chooseService import *
from page.HSpage import *
from faker import Faker


class SmokingTest(AppInit, Login, ChooseService, HSpage):

    def testSmoking(self):
        fake = Faker("zh_CN")
        # self.click_allow('确定')
        self.clickContinue()
        # self.click_allow('确定')
        self.typeUsername('test3')
        self.typePassword('123456')
        self.clickConfirming
        # self.driver.start_activity('zhiyun.com.mirrorplusandroid.freeee',
        #                            'zhiyun.com.mirrorplusandroid.freeee.activity.FaceActivity')
        self.chooseHS()
        # self.click_allow('允许')
        self.start()
        self.type_phone_num(fake.phone_number())
        self.click_phone_continue()
        print(self.driver.get_window_size())
        time.sleep(3)
        self.sign(300 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920,
                  600 * self.dict['width'] / 1080, 1585 * self.dict['height'] / 1920)
        self.clickConfirmer()
        # self.clickCapture()
        # self.driver.push_file(r'C:\Users\Emotion\Desktop\be9c44f594cfb15026630056c89b2ac.jpg')
        # print(self.driver.get_cookies())
        self.driver.implicitly_wait(100)
        self.choose_sex("女")
        self.choose_random_age()
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
        self.choose_answer(1, 6)
        self.clickContinue()
        time.sleep(3)
        self.multi_random_choice_two(0, 5)
        self.clickContinue()
        time.sleep(10)
        # self.clickHealthCase()
        # self.driver.tap([(520, 1644)])
        # time.sleep(10)
        # self.driver.tap([(430, 287)])
        # # self.chooseRandomScheme()
        # time.sleep(30)
        print(self.driver.contexts)
        self.driver.switch_to.context('WEBVIEW_zhiyun.com.mirrorplusandroid.freeee')
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
