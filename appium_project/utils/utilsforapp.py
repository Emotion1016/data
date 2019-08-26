import uiautomator2 as u2

class Utils:

    d = None

    @classmethod
    def connect(cls):
        if cls.d == None:
            # cls.d = u2.connect('3EP7N19401002574')
            # cls.d = u2.connect('41180608000090')
            cls.d = u2.connect('127.0.0.1:62001')
            # cls.d.app_start("zhiyun.com.mirrorplusandroid.freeee")
        return cls.d

    @classmethod
    def startApp(cls):
        cls.d = cls.connect()
        cls.d.app_start("zhiyun.com.mirrorplusandroid.freeee")

    def getToast(self):
        self.d = self.connect()
        # [Args]
        # 5.0: max wait timeout. Default 10.0
        # 10.0: cache time. return cache toast if already toast already show up in recent 10 seconds. Default 10.0 (Maybe change in the furture)
        # "default message": return if no toast finally get. Default None
        response = self.d.toast.get_message(10,10,"hello world")
        return response