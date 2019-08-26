from base.base_page import *


class PersonalRE(AppUI):
    '''个人历史报告手机号验证界面'''
    personalHistoryReport_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_personal_history')  # 个人历史报告
    phoneNum_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_cellphone')       # 输入手机号
    verifyCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_sms_code')      # 验证码
    getVerifyCode_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/btn_get_code')       # 获取验证码键
    healthEventButton_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_jump_event')      # 健康大事件键

    def clickPerHis(self):
        self.findElement(*self.personalHistoryReport_loc).click()

    def typePhoneNum(self, phoneNum):
        self.findElement(*self.phoneNum_loc).send_keys(phoneNum)

    def clickGetVerCode(self):
        self.findElement(*self.getVerifyCode_loc).click()

    def typeVerifyCode(self, verifyCode):
        self.findElement(*self.verifyCode_loc).send_keys(verifyCode)

    def clickHealthEventButton(self):
        self.findElement(*self.healthEventButton_loc).click()
