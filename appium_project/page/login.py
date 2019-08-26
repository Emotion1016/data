from base.base_page import *
# import time
# from selenium import webdriver
# from appium import webdriver
from selenium.webdriver.common.by import By


class Login(AppUI):
    '''登录界面'''
    username_loc=(By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_username')      # 用户名
    password_loc=(By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_pwd')       # 密码
    confirm_loc=(By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_login_sure')      # 确认

    # 登录界面输入用户名
    def typeUsername(self, username):
        self.findElement(*self.username_loc).clear()
        self.findElement(*self.username_loc).send_keys(username)

    # 登录界面输入密码
    def typePassword(self, password):
        self.findElement(*self.password_loc).clear()
        self.findElement(*self.password_loc).send_keys(password)

    # 登录界面确定键
    @property
    def clickConfirming(self):
        self.findElement(*self.confirm_loc).click()

    '''忘记密码界面'''
    forget_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_forgot_pwd')  # 忘记密码键
    recoverUsername_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_name')  # 用户名
    storeCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_vendor')  # 厂家码
    recoverPwd_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_pwd')  # 设置密码
    recoverPwdAgain_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_again_pwd')  # 确认密码
    doNotHaveCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_no_vendor')  # 我没有厂家码

    def clickForgetPage(self):
        self.findElement(*self.forget_loc).click()

    def typeRecUsername(self, RecUsername):
        self.findElement(*self.recoverUsername_loc).send_keys(RecUsername)

    def typeStoreCode(self, storeCode):
        self.findElement(*self.storeCode_loc).send_keys(storeCode)

    def typeRecPwd(self, RecPwd):
        self.findElement(*self.recoverPwd_loc).send_keys(RecPwd)

    def typeRecPwdAgain(self, RecPwd):
        self.findElement(*self.recoverPwdAgain_loc).send_keys(RecPwd)


if __name__ == '__main__':
    l = Login(WebDriver)
    l.login('123', '123')
