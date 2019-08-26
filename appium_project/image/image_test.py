from image.image_auto import ImageAuto
import time, os

if __name__ == '__main__':
    ia = ImageAuto('./screenshot')
    # os.system(r'"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" http://localhost:8088/woniusales')
    os.system(r'start /b "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8088/woniusales')
    time.sleep(2)

    if not ia.check('username.png'):
        if ia.check('dologout.png'):
            ia.click('dologout.png')
            print("当前页面并不在登录界面，先进行注销.")
            time.sleep(2)
        # raise Exception

    ia.input('username.png', 'admin')
    ia.input('password.png', 'admin123')
    ia.input('verifycode.png', '0000')
    ia.click('dologin.png')
    time.sleep(2)

    if ia.check('checklogin.png'):
        print("登录成功")
    else:
        print("登录失败")
