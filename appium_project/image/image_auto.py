import cv2 as cv
from PIL import ImageGrab
import time, os
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class ImageAuto:
    def __init__(self, folder):
        self.mouse = PyMouse()
        self.key = PyKeyboard()
        self.folder = folder

    # 调用OpenCV的模板匹配功能查找图像的坐标位置
    def find_image(self, target):
        ImageGrab.grab().save(self.folder + '/myscreen.png')  # 对当前屏幕截图

        screen = cv.imread(self.folder + "/myscreen.png")  # 打开屏幕截图
        template = cv.imread('%s/%s' % (self.folder, target))  # 打开模板图片
        # 调用openCV自带的matchTemplate方法进行模板匹配
        result = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)
        # print(cv.minMaxLoc(result))
        pos_start = cv.minMaxLoc(result)[3]  # 获取匹配成功后的起始坐标
        # 计算匹配对象的中心坐标X和Y
        x = int(pos_start[0]) + int(template.shape[1] / 2)
        y = int(pos_start[1]) + int(template.shape[0] / 2)

        # 根据匹配度返回坐标，如果匹配度小于95%，则返回无效坐标(-1,-1)
        similarity = cv.minMaxLoc(result)[1]
        if similarity < 0.95:
            return (-1, -1)
        else:
            return (x, y)

    # 单击
    def click(self, target):
        x, y = self.find_image(target)
        if (x, y) == (-1, -1):
            print("找不到")
        else:
            self.mouse.click(x, y)
            print('在位置[%d, %d]处单击图片:%s.' % (x, y, target))

    # 双击
    def double_click(self, target):
        x, y = self.find_image(target)
        self.mouse.click(x, y, n=2)

    # 输入
    def input(self, target, value):
        x, y = self.find_image(target)
        self.clear(target)
        self.key.type_string(value)
        print('在位置[%d, %d]的图片:%s上输入%s.' % (x, y, target, value))

    # 清空
    def clear(self, target):
        self.double_click(target)
        self.key.press_key(self.key.backspace_key)

    # 下拉框处理，如何解决？
    def select(self, target, *args):
        pass

    # 断言
    def check(self, target):
        x, y = self.find_image(target)
        if (x, y) == (-1, -1):
            return False
        else:
            return True