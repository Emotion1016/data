import unittest
from selenium import webdriver as wd
from appium import webdriver as d
from app_config_b import CAPS as b
from app_config_a import CAPS as a
import sys
from faker import Faker
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class WebInit(unittest.TestCase):
    def setUp(self):
        self.driver = wd.Chrome()
        self.driver.maximize_window()
        self.driver.get('')

    def tearDown(self):
        self.driver.quit()


class AppInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = d.Remote("http://127.0.0.1:4723/wd/hub", a)
        cls.driver.implicitly_wait(10)
        cls.dict = cls.driver.get_window_size()

    # @classmethod
    def tearDown(self):
        self.driver.reset()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class AppInitMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake = Faker("zh_CN")
        cls.driver = d.Remote("http://127.0.0.1:4723/wd/hub", b)
        cls.driver.implicitly_wait(10)
        cls.dict = cls.driver.get_window_size()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
