from base.base_page import *


class ChooseService(AppUI):

    '''选择服务界面'''
    physiqueIdentification_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_cm_body_type')   # 体质辨识
    healthStatus_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_cm_intelligence')      # 健康状态
    diseaseManagement_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_cm_chronic_disease')      # 病理

    # 选择中医体质辨识
    def choosePI(self):
        self.findElement(*self.physiqueIdentification_loc).click()

    # 选择健康状态辨识
    def chooseHS(self):
        self.findElement(*self.healthStatus_loc).click()

    # 选择病理
    def chooseDM(self):
        self.findElement(*self.diseaseManagement_loc).clcik()
