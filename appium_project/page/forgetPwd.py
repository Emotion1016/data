from base.base_page import *


class ForgetPwd(AppUI):
    '''忘记密码界面'''
    forget_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_forgot_pwd')   # 忘记密码键
    recoverUsername_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_name')       # 用户名
    storeCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_vendor')       # 厂家码
    recoverPwd_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_pwd')     # 设置密码
    recoverPwdAgain_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_recover_again_pwd')      # 确认密码
    doNotHaveCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_no_vendor')     # 我没有厂家码

    def clickForgetPage(self):
        self.findElement(*self.forget_loc).click()

    def typeRecUsername(self, rec_username):
        self.findElement(*self.recoverUsername_loc).send_keys(rec_username)

    def typeStoreCode(self, store_code):
        self.findElement(*self.storeCode_loc).send_keys(store_code)

    def typeRecPwd(self, rec_pwd):
        self.findElement(*self.recoverPwd_loc).send_keys(rec_pwd)

    def typeRecPwdAgain(self, rec_pwd):
        self.findElement(*self.recoverPwdAgain_loc).send_keys(rec_pwd)
