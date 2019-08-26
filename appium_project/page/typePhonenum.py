from base.base_page import *


class TypePhonenum(AppUI):
    '''输入电话号码界面'''
    phonenum_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_login_cellphone')     # 电话号码
    keyboard_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/view_keyboard_ground')    #  电话号码键盘
    continue_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_continue')     # 继续键
    back_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_title_back')       # 返回键

    # 输入电话号码
    def typePhonenum(self, phonenum):
        self.findElement(*self.phonenum_loc).send_keys(phonenum)

    def clickPhoneContinue(self):
        self.findElement(*self.continue_loc).click()
