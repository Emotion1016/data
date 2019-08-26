import cv2 as cv
from PIL import ImageGrab
import time, os
from pymouse import PyMouseMeta
from pykeyboard import PyKeyboard

class ImageAndroid:
    def __init__(self, folder, udid):
        self.mouse = PyMouseMeta()
        self.key = PyKeyboard()
        self.folder = folder
        self.udid = udid

    # 调用OpenCV的模板匹配功能查找图像的坐标位置
    def find_image(self, target):
        os.system('adb -s %s shell screencap -p /sdcard/myscreen.png' % self.udid)
        time.sleep(1)
        os.system('adb -s %s pull /sdcard/myscreen.png %s/myscreen.png' % (self.udid, self.folder))  # 对当前屏幕截图

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
        print(similarity)
        if similarity < 0.95:
            return (-1, -1)
        else:
            return (x, y)

    def click(self, target):
        x, y = self.find_image(target)
        os.system('adb -s %s shell input tap %d %d' % (self.udid, x, y))

    def input(self, target, value):
        x, y = self.find_image(target)
        os.system('adb -s %s shell input tap %d %d' % (self.udid, x, y))
        os.system('adb -s %s shell input tap %d %d' % (self.udid, x, y))
        os.system('adb -s %s shell input keyevent 67' % (self.udid))
        os.system('adb -s %s shell input text %s' % (self.udid, value))

    def check(self, target):
        x, y = self.find_image(target)
        if (x, y) == (-1, -1):
            return False
        else:
            return True

if __name__ == '__main__':
    ia = ImageAndroid('./screenshot', '127.0.0.1:62001')
    ia.click('number8.png')
    ia.click('plus.png')
    ia.click('number6.png')
    ia.click('equal.png')

    if ia.check('result.png'):
        print("测试成功")
    else:
        print("测试失败")