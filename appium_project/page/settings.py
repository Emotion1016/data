from base.base_page import *


class Settings(AppUI):
    settings_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_all_setting')  # 设置键
    wifi_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_wifi_setting')     # wifi
    prefer_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_prefer_setting')     # 偏好设置
    secure_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_secure_setting')     # 安全设置
    about_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_about_setting')       # 关于我们
    sound_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_volume_setting')      # 音量
    resetPwd = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_reset_setting')        # 修改密码
    upgrade_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_upgrade_setting')       # 在线升级
    version_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_version_setting')       # 当前版本
    switchService_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_switch_service_setting')      # 切换服务
    light_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_light_setting')       # 灯带设置
    logout_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_exit_login')     # 退出当前账号
