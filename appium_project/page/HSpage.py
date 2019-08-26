from base.base_page import *
import random


class HSpage(AppUI):

    '''中医健康状态辨识主界面'''
    start_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_all_diagnosis')       # 开始键
    playMusic_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/cb_music_start')     # 播放音乐键
    music_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_music_name')      # 音乐列表键
    preMusic_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_music_pre')        # 上一首
    nextMusic_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/iv_music_next')      # 下一首
    playVideo_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/start')          # 播放视频
    personalHistoryReport_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_personal_history')        # 个人历史报告
    storeHistoryReport_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_personal_history')       # 机构历史报告
    settings_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_all_setting')      # 设置键
    musicList_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_spinner_item')       # 音乐列表

    def start(self):
        self.findElement(*self.start_loc).click()

    def click_music_list(self):
        self.findElement(*self.music_loc).click()

    def music_list(self):
        return self.findElement(*self.musicList_loc)

    '''输入电话号码界面'''
    phonenum_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/edt_login_cellphone')  # 电话号码
    keyboard_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/view_keyboard_ground')  # 电话号码键盘
    continue_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_continue')  # 继续键
    back_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_title_back')  # 返回键

    def type_phone_num(self, phone_num):
        self.findElement(*self.phonenum_loc).send_keys(phone_num)

    def click_phone_continue(self):
        self.findElement(*self.continue_loc).click()

    '''知情同意书界面'''
    signature_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/signature_pad')      # 签名区域
    clear_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_clear_signature')     # 清除键

    def sign(self, x1, y1, x2, y2):
        # self.driver.swipe(333,2611,932,2619)
        self.driver.swipe(x1, y1, x2, y2)

    def clear(self):
        self.findElement(*self.clear_loc).click()

    '''面诊界面'''
    capture_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/capture')  # 拍照键

    def click_capture(self):
        # self.findElement(*self.capture_loc).click()
        # self.findElement(*self.capture_loc).send_keys(r'C:\Users\Emotion\Desktop\be9c44f594cfb15026630056c89b2ac.jpg')
        self.findElement(By.ID,
                         "zhiyun.com.mirrorplusandroid.freeee:id/iv_outside")\
            .send_keys(r'C:\Users\Emotion\Desktop\be9c44f594cfb15026630056c89b2ac.jpg')

    '''个人信息界面'''
    age = ['1——12岁', '13——18岁', '19——25岁', '26——35岁', '36——45岁', '46——60岁', '60岁以上']
    sex = ['男', '女']
    age_loc = (By.XPATH, f"//*[@text='{age[random.randint(0, len(age)-1)]}']")
    sex_loc = (By.XPATH, f"//*[@text='{sex[random.randint(0, len(sex)-1)]}']")
    extra_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/rg_pregnancy')
    Extra_loc = (By.CLASS_NAME, 'android.widget.CheckBox[0]')

    def choose_random_age(self):
        self.findElement(*self.age_loc).click()

    def choose_age(self, age):
        self.findElement(By.XPATH, f"//*[@text='{age}']").click()

    def choose_random_sex(self):
        self.findElement(*self.sex_loc).click()

    def choose_sex(self, sex):
        self.findElement(By.XPATH, f"//*[@text='{sex}']").click()

    def locate_extra(self):
        self.findElement(*self.extra_loc)

    def print_extra(self):
        '''女性额外选项'''
        self.findElement(*self.extra_loc)

    def click_extra(self, text):
        for i in range(1, 4):
            self.findElement(By.XPATH, f"//*[@text='{text}']").click()

    '''身高界面'''
    heightView_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/verticalScale')
    heightNum_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/bg_heart_icon')

    def swipe_height(self):
        # self.driver.swipe(1269, 1000, 1269, 1800)
        self.driver.swipe(1269*1080/1440, 1000*1920/2860, 1269*1080/1440, 1800*1920/2860)

    '''体重界面'''
    weightNum_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/show_weight_num')
    minus_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_delete_event')
    plus_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/tv_add_event')

    def swipe_weight(self):
        # self.driver.swipe(1240, 1516, 300, 1516)
        self.driver.swipe(940*1080/1440, 1516*1920/2860, 300*1080/1440, 1516*1920/2860)
        # self.driver.swipe(1240*self.dict['width']/1440,1516*self.dict['height']/2860,300*self.dict['width']/1440,1516*self.dict['height']/2860)
        '1240*1080/1440,1516*1920/2860,300*1080/1440,1516*1920/2860'

    def click_minus(self):
        self.findElement(*self.minus_loc).click()

    def click_plus(self):
        self.findElement(*self.plus_loc).click()

    '''单选题界面'''
    yes_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/rb_yes_diagnosis')
    no_loc = (By.ID, 'zhiyun.com.mirrorplusandroid.freeee:id/rb_no_diagnosis')

    def yes(self):
        res = self.findElement(*self.yes_loc).text
        print(res)

    def no(self):
        res = self.findElement(*self.no_loc).text
        print(res)

    def radio_question(self, start_num, end_num):
        for i in range(start_num, end_num):
            self.findElement(By.XPATH,
                             f"//android.widget.LinearLayout[{i}]/android.widget.RadioGroup/"
                             f"android.widget.RadioButton[{random.randint(1,2)}]").click()

    def radio_question_title(self):
        title_list = []
        for i in range(1, 8):
            title = self.findElement(By.XPATH,
                                     f"//android.widget.LinearLayout[{i}]/android.widget.TextView[1]").text
            title_list.append(title)
        return title_list

    '''多选题界面A'''
    def multi_choice_one(self, start_num, end_num):
        for i in range(start_num, end_num):
            self.findElement(By.XPATH,
                             f"//android.widget.LinearLayout[{i}]/android.support.v7.widget.RecyclerView/"
                             f"android.widget.CheckBox[1]").click()
            self.findElement(By.XPATH,
                             f"//android.widget.LinearLayout[{i}]/android.support.v7.widget.RecyclerView/"
                             f"android.widget.CheckBox[2]").click()

    def multi_choice_title(self):
        title_list = []
        for i in range(1, 7):
            title = self.findElement(By.XPATH, f"//android.widget.LinearLayout[{i}]/android.widget.TextView[1]").text
            title_list.append(title)
        return title_list

    '''女性单选题界面'''
    def choose_answer(self, start_num, end_num):
        for i in range(start_num, end_num):
            self.findElement(By.XPATH,
                             f"//android.widget.LinearLayout[{i}]/android.support.v7.widget.RecyclerView/"
                             f"android.widget.CheckBox[2]").click()

    def female_radio_choice_title(self):
        title_list = []
        for i in range(1, 6):
            title = self.findElement(By.XPATH, f"//android.widget.LinearLayout[{i}]/android.widget.TextView[1]").text
            title_list.append(title)
        return title_list

    '''多选题界面B'''
    def multi_random_choice_two(self, start_num, end_num):
        for i in range(start_num, end_num):
            self.findElement(By.XPATH,
                             f"//android.widget.LinearLayout/android.support.v7.widget.RecyclerView/"
                             f"android.widget.CheckBox[{random.randint(1,23)}]").click()

    def ergodic_click_each_choice(self):
        for i in range(0, 23):
            self.findElement(By.XPATH,
                             f"//android.widget.LinearLayout/android.support.v7.widget.RecyclerView/"
                             f"android.widget.CheckBox[{random.randint(1,23)}]").click()

    def ergodic_print_each_choice(self):
        disease_list = []
        for i in range(1, 24):
            word = self.findElement(By.XPATH,
                                    f"//android.widget.LinearLayout/android.support.v7.widget.RecyclerView/"
                                    f"android.widget.CheckBox[{i}]").text
            disease_list.append(word)
        return disease_list

    '''报告界面'''
    personalAllRe_loc = (By.XPATH, "//android.view.View[7]")
    knowledgeDB_loc = (By.XPATH, "//android.view.View[11]")
    printRe_loc = (By.XPATH, "//android.view.View[12]")
    healthCase_loc = (By.XPATH, "//android.view.View[15]")

    def click_personal_all_report(self):
        self.findElement(*self.personalAllRe_loc).click()

    def click_knowledge_database(self):
        self.findElement(*self.knowledgeDB_loc).click()

    def click_print_report(self):
        self.findElement(*self.printRe_loc).click()

    def click_health_case(self):
        self.findElement(*self.healthCase_loc).click()

    '''健康方案界面'''
    scheme = ["饮食调养", "茶饮养生", "经典药方", "穴位按压", "中医功法", "音乐养生", "起居指导", "保健原则"]
    scheme_loc = (By.XPATH, f"//*[@text='{scheme[random.randint(0, len(sex)-1)]}']")

    def choose_random_scheme(self):
        self.findElement(*self.scheme_loc).click()

    def choose_scheme(self, scheme):
        self.findElement(By.XPATH, f"//*[@text='{scheme}']").click()
