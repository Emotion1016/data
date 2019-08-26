from base.base_page import *


class Register(AppUI):
    '''注册界面'''
    register_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/btn_user_register')   # 进入注册页面
    storeCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_auth')   # 厂家码
    continue_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_auth_continue')    # 继续键
    back_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_title_back')       # 返回键
    regUsername_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_register_name')    # 用户名
    regPwd_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_new_pwd')       # 设置密码
    regPwdAgain_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_again_pwd')        # 确认密码
    registerText_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_title')        # 上方标题注册

    def enterRegister(self):
        self.findElement(*self.register_loc)

    def typeStoreCode(self, storeCode):
        self.findElement(*self.storeCode_loc).send_keys(storeCode)

    def clickContinue(self):
        self.findElement(*self.continue_loc)

    def clickBack(self):
        self.findElement(*self.back_loc)

    def typeRegUsername(self, regUsername):
        self.findElement(*self.regUsername_loc).clear()
        self.findElement(*self.regUsername_loc).send_keys(regUsername)

    def typeRegPwd(self, regPwd):
        self.findElement(*self.regPwd_loc).clear()
        self.findElement(*self.regPwd_loc).send_keys(regPwd)

    def typeRegPwdAgain(self, regPwd):
        self.findElement(*self.regPwdAgain_loc).clear()
        self.findElement(*self.regPwdAgain_loc).send_keys(regPwd)

    def getRegText(self):
        return self.findElement(*self.registerText_loc).text
