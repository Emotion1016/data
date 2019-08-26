from base.base_page import *


class StoreRE(AppUI):
    '''机构历史报告界面'''
    storeHistoryReport_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_personal_history')  # 机构历史报告
    storePwd_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_sms_code')        # 机构密码
    forgetPwd_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_forget_pwd')      # 忘记密码
