from selenium.webdriver.support.expected_conditions import NoSuchElementException,presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import xml.dom.minidom


class Factory(object):
    def __init__(self, driver):
        self.driver = driver

    def createDriver(self, driver):
        if driver == 'web':
            return WebUI(self.driver)
        elif driver == 'app':
            return AppUI(self.driver)


class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        '''单个定位元素方法'''
        try:
            return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
        except:
            # print('Error Details {0}'.format(e.args[0]))
            return False

    def findsElement(self, *loc):
        '''多个定位元素方法'''
        try:
            return WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def get_toast_text(self, text, timeout=5, poll_frequency=0.01):
        """
        ########################################
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        ########################################
        """
        # text = re.compile('(.*?)').pattern
        # print(text)
        toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
        try:
            toast = WebDriverWait(self.driver, timeout, poll_frequency).\
                until(presence_of_element_located(toast_element))
            return toast.text
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))
            return False

    def click_allow(self, text):
        number = 2
        for i in range(number):
            loc = ("xpath", f"//*[@text='{text}']")
            try:
                WebDriverWait(self.driver, 3, 2).until(presence_of_element_located(loc)).click()
            except:
                pass

    def clickContinue(self):
        loc = ("xpath", "//*[@text='继  续']")
        try:
            WebDriverWait(self.driver, 3, 2).until(presence_of_element_located(loc)).click()
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def clickConfirmer(self):
        loc = ("xpath", "//*[@text='确  定']")
        try:
            WebDriverWait(self.driver, 3, 2).until(presence_of_element_located(loc)).click()
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def clickCancel(self):
        loc = ("xpath", "//*[@text='返  回']")
        try:
            WebDriverWait(self.driver, 3, 2).until(presence_of_element_located(loc)).click()
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def click_close(self):
        close_loc = (By.ID, "zhiyun.com.mirrorplusandroid.freeee:id/ic_close_all")
        self.findElement(*close_loc).click()

    def switch_h5(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.weizq"})

    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    def logcat(self):
        cmd_c = 'adb logcat -c'
        os.popen(cmd_c)         # 清除以前的日志
        for i in range(30):             # 30秒没有短信日志抛valueError
            try:
                cmd_d = 'adb logcat -d | findstr codeString'
                value = os.popen(cmd_d).read()      # 获取刚刚的短信验证码那一行日志信息
                code = value.split('验证码：')[1].split('，')[0]
                break
            except:
                pass
            time.sleep(1)
        else:
            raise ValueError
        return code

    def getXmlData(self, filename, value, num, val):
        '''
        获取xml单节点中的数据
        :param value: xml文件中单节点的名称
        '''
        dom = xml.dom.minidom.parse(filename)
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[num].getAttribute(val)
        return nameValue
        # return nameValue.findChild.data

    def getCsvData(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            d = f.readlines()
            print(f'文件内容为{d}')
            list = []
            for i in range(1, len(d)):
                newD = tuple(d[i].strip('\n').split(','))
                print(newD)
                list.append(newD)
            print(list)
            return list


class WebUI(WebDriver):
    def __str__(self):
        return 'WebUI'


class AppUI(WebDriver):
    def __str__(self):
        return 'AppUI'

# def is_toast_exist(WebDriver,text,timeout=30,poll_frequency=0.5):
#     '''is toast exist, return True or False
#     :Agrs:
#      - driver - 传driver
#      - text   - 页面上看到的文本内容
#      - timeout - 最大超时时间，默认30s
#      - poll_frequency  - 间隔查询时间，默认0.5s查询一次
#     :Usage:
#      is_toast_exist(driver, "看到的内容")
#     '''
#     try:
#         toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
#         WebDriverWait(driver, timeout, poll_frequency).until(presence_of_element_located(toast_loc))
#         return toast_loc
#     except:
#         return None
#
# def get_toast_text(text, timeout=5, poll_frequency=0.01):
#     """
#     ########################################
#     描述：获取Toast的文本信息
#     参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
#     返回值：返回与之匹配到的toast信息
#     异常描述：none
#     ########################################
#     """
#     toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
#     toast = WebDriverWait(WebDriver, timeout, poll_frequency).until(presence_of_element_located(toast_element))
#     return toast.text


if __name__ == '__main__':
    WebDriver(AppUI).getCsvData(r'D:\appium_project\data\login.csv')

